"""
#Q1
arr = [0,1,2,3,4]

print(arr)

arr.append(5)
print(arr)

Q2
arr2 = []
decide=True
while(decide):
   if(decide):
      num = int(input("Enter a Number"))
      arr2.append(num);
      print(arr2);
   decide = input("Do you want to continue (y/n)? ")
   if decide.lower()!='y':
      break

#Q3
import requests
import json

url="https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

response = requests.get(url)

data = response.json()

title = data.get("title","No Title Available")
explanation = data.get("explanation","No Explanation Available")
#json file in full
for i in data :
    print(i,":",data[i])
    print("\n")
print("Title:",title)
print("\nExplanation:",explanation)

#Q4
import requests
url="http://api.open-notify.org/iss-now.json"

response = requests.get(url)

if response.status_code == 200:
    print("Request Successful")
    data = response.json()
    print("Response Data:\n",data)

else:
    print("Request Failed")

#Q5
import requests

   url="http://api.open-notify.org/iss-now.json"

   response = requests.get(url)

if response.status_code == 200:
    print("Request Successful")
    data = response.json()
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timeStamp = data['timestamp']
    print(f"The International Space Station is currently at {latitude} latitude and {longitude} longitude at {timeStamp}")

else:
    print("Request Failed")


"""
#Q6
import requests
import pandas as pd
import time
from datetime import datetime
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

url = "http://api.open-notify.org/iss-now.json"

# Configure retry strategy
retry_strategy = Retry(
    total=5,  # Number of total retries
    backoff_factor=1,  # Delay between retries
    status_forcelist=[500, 502, 503, 504],  # Status codes to retry on
)

# Create an adapter with the retry strategy
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("http://", adapter)

data_list = []

for i in range(100):
    try:
        response = http.get(url, timeout=10)  # Set a timeout for the request
        if response.status_code == 200:
            print("Request Successful")
            data = response.json()

            # Capture the timestamp of the request
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            iss_loc = {
                'timestamp': timestamp,
                'latitude': data['iss_position']['latitude'],
                'longitude': data['iss_position']['longitude']
            }
            data_list.append(iss_loc)
        else:
            print(f"Request Failed with status code: {response.status_code}")
            break
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        break

    time.sleep(10)  # Wait for 10 seconds before the next request

# Create a DataFrame
df = pd.DataFrame(data_list)

# Save to CSV
df.to_csv('iss_location_data.csv', index=False)

print("Data has been written to 'iss_location_data.csv'")

