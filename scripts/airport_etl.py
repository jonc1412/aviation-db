import pandas as pd
import boto3

df = pd.read_csv("data/csv/iata-icao.csv", keep_default_na=False, quotechar='"')

print(df.head())
print(df.info())

print('Null value check')
print(df.isnull().sum())

print(f'Number of duplicate values: {df.duplicated().sum()}')

df.to_parquet('data/parquet/airport_data.parquet', index=False)

s3 = boto3.client('s3')
s3.upload_file('data/parquet/airport_data.parquet', 's3-aviation-db', 'aviation_data/airport_data.parquet')