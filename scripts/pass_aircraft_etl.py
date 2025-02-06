import pandas as pd
import boto3

# There was an issue with pandas defaulting carrier code: "NA" into NaN, so use keep_default_na=False
df = pd.read_csv("data/csv/International_Report_Passengers_20250205.csv", keep_default_na=False)

df.columns = df.columns.str.lower()
df.rename(columns={'data_dte': 'date', 'airlineid': 'airline_id', 'carriergroup': 'carrier_group'}, inplace=True)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df.drop(columns=['year', 'month'], inplace=True)

# Checking for null values
print(df.isnull().sum())

# Checking for duplicate values
print(f'Number of duplicate values: {df.duplicated().sum()}')

df.to_parquet('data/parquet/passenger_aircraft_data.parquet', index=False)

s3 = boto3.client('s3')
s3.upload_file('data/parquet/passenger_aircraft_data.parquet', 's3-aviation-db', 'aviation_data/passenger_aircraft_data.parquet')