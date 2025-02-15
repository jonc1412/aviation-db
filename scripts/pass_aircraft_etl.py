import pandas as pd
import boto3
import os 
from pathlib import Path

# There was an issue with pandas defaulting carrier code: "NA" into NaN, so use keep_default_na=False
df = pd.read_csv("data/csv/International_Report_Passengers_20250205.csv", keep_default_na=False)

df.columns = df.columns.str.lower()
df.rename(columns={'data_dte': 'date', 'airlineid': 'airline_id', 'carriergroup': 'carrier_group'}, inplace=True)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df.drop(columns=['year', 'month', 'usg_apt_id', 'fg_apt_id', 'airline_id', 'type', 'usg_wac', 'fg_wac'], inplace=True)

for col, nul_count in df.isnull().sum().items():
    if col == 0:
        print(f'Null value found in {col}: {nul_count}')

if df.duplicated().sum() > 0:
    print(f'Number of duplicate values: {df.duplicated().sum()}')

p_file_path = 'data/parquet/passenger_aircraft_data.parquet'
if os.path.exists(p_file_path):
    print('File already exists')
else:
    df.to_parquet(p_file_path, index=False)

s3 = boto3.client('s3')
s3.upload_file('data/parquet/passenger_aircraft_data.parquet', 's3-aviation-db', 'aviation_data/passenger_aircraft_data.parquet')