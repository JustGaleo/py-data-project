import glob
import pandas as pd
from datetime import datetime

def read_exchangeRate():
    df = pd.read_csv("exchange_rates.csv", index_col=0)
    exchange_rate = df.loc['GBP'].loc['Rates'] 
    return exchange_rate

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe

def extract():
    extracted_data = pd.DataFrame(columns=['Name','Market Cap (US$ Billion)'])
    for jsonfile in glob.glob("bank_market_cap_1.json"):
        extracted_data = extracted_data._append(extract_from_json(jsonfile), ignore_index=True)
    return extracted_data

def transform(data):
    data['Market Cap (US$ Billion)'] = round(data['Market Cap (US$ Billion)'] * read_exchangeRate(), 3)
    data.rename(columns = {'Market Cap (US$ Billion)':'Market Cap (GBP$ Billion)'}, inplace = True)
    return data

def load(targetfile,data_to_load):
    data_to_load.to_csv(targetfile)

def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')