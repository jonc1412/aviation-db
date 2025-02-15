import pandas as pd
import boto3
import os 
from pathlib import Path

df = pd.read_csv("data/csv/iata-icao.csv", keep_default_na=False, quotechar='"')

df.drop(columns=['icao'], inplace=True)

for col, nul_count in df.isnull().sum().items():
    if col == 0:
        print(f'Null value found in {col}: {nul_count}')

if df.duplicated().sum() > 0:
    print(f'Number of duplicate values: {df.duplicated().sum()}')


p_file_path = 'data/parquet/airport_data.parquet'
if os.path.exists(p_file_path):
    print('File already exists')
else:
    df.to_parquet('data/parquet/airport_data.parquet', index=False)

s3 = boto3.client('s3')
s3.upload_file('data/parquet/airport_data.parquet', 's3-aviation-db', 'aviation_data/airport_data.parquet')