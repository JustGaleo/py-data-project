import etl
print('Starting the extract phase')
etl.log("ETL Job Started")
etl.log("Extract phase Started")
extracted_data = etl.extract()
print(extracted_data.head())
etl.log("Extract phase Ended")

print('Starting the transform phase')
etl.log("Transform phase Started")
transformed_data = etl.transform(extracted_data)
print(transformed_data.head())
etl.log("Transform phase Ended")

print('Starting the load phase')
etl.log("Load phase Started")
etl.load("transformed_data.csv",transformed_data)
etl.log("Load phase Ended")
print("FINISH")



