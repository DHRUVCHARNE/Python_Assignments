import pandas as pd
import requests
import json
from datetime import datetime, timedelta

# Define the date range
start_date = datetime.strptime("2024-05-01", "%Y-%m-%d")
end_date = datetime.strptime("2024-06-30", "%Y-%m-%d")

# Initialize a list to store the data
js_arr = []

# Loop through each date in the specified range
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d")
    url = f"https://vegetablemarketprice.com/api/dataapi/market/himachalpradesh/daywisedata?date={date_str}"

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }

    data = requests.get(url, headers=header)
    js_data = json.loads(data.text)

    for api in js_data["data"]:
        veg_name = api.get("vegetablename", "N/A")
        price = api.get("price", "N/A")
        retail_price = api.get("retailprice", "N/A")
        unit = api.get("units", "N/A")
        mall_price = api.get("shopingmallprice", "N/A")
        veg_image = api.get("vegetableimage", "N/A")

        new_js = {
            "date": date_str,
            "state_name": "Himachal Pradesh",
            "veg_name": veg_name,
            "price": price,
            "retail_price": retail_price,
            "mall_price": mall_price,
            "unit": unit,
            "veg_image": veg_image
        }
        js_arr.append(new_js)

    current_date += timedelta(days=1)

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame(js_arr)
df.to_csv("Himachal_Pradesh_Vegetable_Data_May_June_2024.csv", index=False)

print("Data scraping and saving completed.")