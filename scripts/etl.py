import pandas as pd
import boto3

df = pd.read_csv("data\International_Report_Passengers_20250205.csv")

df.columns = df.columns.str.lower()
df.rename(columns={'data_dte': 'date', 'airlineid': 'airline_id', 'carriergroup': 'carrier_group'}, inplace=True)
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Checking for null values
print(df.isnull().sum())
df['carrier'].fillna('UNKNOWN', inplace=True)

# Checking for duplicate values
print(f'Number of duplicate values: {df.duplicated().sum()}')

df.to_parquet('aviation_data.parquet', index=False)

s3 = boto3.client('s3')
s3.upload_file('aviation_data.parquet', 's3-aviation-db', 'processed/aviation_data.parquet')