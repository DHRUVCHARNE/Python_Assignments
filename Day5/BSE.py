import requests
import os
import csv
from datetime import datetime, timedelta

# Function to download file
def download_file(code, group, from_date, to_date):
    # Specify download location
    download_dir = "/workspaces/Python_Assignments/downloads"  # Use a directory within the workspace
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Construct the URL
    url = f'https://api.bseindia.com/BseIndiaAPI/api/StockPriceCSVDownload/w?pageType=0&rbType=D&Scode={code}&FDates={from_date}&TDates={to_date}&Seg={group}'

    try:
        # Download the file using requests
        filename = os.path.join(download_dir, f"{code}_{from_date}_{to_date}.csv")
        response = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"File {code}_{from_date}_{to_date}.csv downloaded successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Function to read stock codes and groups from CSV files
def read_stock_codes(file_paths):
    stock_codes = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                stock_codes.append({
                    'code': row['Security Code'],
                    'group': row['Group']
                })
    return stock_codes

# Example usage:
file_paths = ['/workspaces/Python_Assignments/Day5/downloads/Commercial_Papers.csv',
               '/workspaces/Python_Assignments/Day5/downloads/Debentures_and_Bonds.csv',
               '/workspaces/Python_Assignments/Day5/downloads/EQT0.csv',
               '/workspaces/Python_Assignments/Day5/downloads/EQT1.csv',
               '/workspaces/Python_Assignments/Day5/downloads/HS.csv',
               '/workspaces/Python_Assignments/Day5/downloads/MB.csv',
               '/workspaces/Python_Assignments/Day5/downloads/MF.csv',
               '/workspaces/Python_Assignments/Day5/downloads/Preference_Shares.csv',
               '/workspaces/Python_Assignments/Day5/downloads/SSE.csv'
               
               ]  # Add your CSV file paths here
stock_codes = read_stock_codes(file_paths)

start_date = datetime(2015, 1, 1)
end_date = datetime(2024, 6, 30)


    
for stock_code in stock_codes:
    download_file(stock_code['code'], stock_code['group'], start_date, end_date)
    