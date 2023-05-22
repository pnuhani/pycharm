import gspread
import os
import sys
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
from oauth2client.service_account import ServiceAccountCredentials
from pyspark.sql import SparkSession

Key_file_path = 'C:\\app\\gsheets-387514-a4e452dc1b25.json'

# Set up credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name(Key_file_path, [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
])

# Create a gspread client
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open('demo')

# Get the first worksheet
worksheet = sheet.get_worksheet(0)

# Read all data as a list of lists
data = worksheet.get_all_values()

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Convert data to a PySpark DataFrame
df = spark.createDataFrame(data, schema=data[0])

# Display the DataFrame
df.show()