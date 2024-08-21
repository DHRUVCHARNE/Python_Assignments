'''
import os
from bs4 import BeautifulSoup
import pandas as pd

# Directory containing HTML files
directory = '/content/bpharma/found'

# Initialize a list to store the scraped data
data = []

# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".html"):  # Ensure it's an HTML file
        file_path = os.path.join(directory, filename)

        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            file_data = file.read()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(file_data, 'html.parser')

        # Extract relevant elements
        div_1 = soup.find("div", {"class": "cont_outer"})
        if div_1:
            table = div_1.find("table", {"class": "cont_DIV_UN"})
            if table:
                div_2 = table.find("div", {"id": "midd_part_UN"})
                if div_2:
                    table_2 = div_2.find("table")
                    if table_2:
                        td_all = table_2.findAll("td", {"class": "border1"})

                        # Corrected index and length checks
                        sgpa = None
                        cgpa = None
                        if len(td_all) >= 6:
                            sgpa = td_all[-6].text.replace("SGPA", "").strip()
                        if len(td_all) >= 4:
                            cgpa = td_all[-4].text.replace("CGPA", "").strip()

                        # Append the scraped data to the list
                        data.append({
                            "file_name": filename,
                            "sgpa": sgpa,
                            "cgpa": cgpa
                        })
                    else:
                        print(f"Table 2 not found in {filename}.")
                else:
                    print(f"Div with id 'midd_part_UN' not found in {filename}.")
            else:
                print(f"Table with class 'cont_DIV_UN' not found in {filename}.")
        else:
            print(f"Div with class 'cont_outer' not found in {filename}.")

# Convert the list of dictionaries to a DataFrame
if data:  # Only create a DataFrame if there's data
    df = pd.DataFrame(data)

    # Clean up SGPA and CGPA columns, if needed
    df['sgpa'] = df['sgpa'].replace(r'\D', '', regex=True).replace('', None)
    df['cgpa'] = df['cgpa'].replace(r'\D', '', regex=True).replace('', None)

    # Save the cleaned data to a new CSV file
    output_csv_path = '/content/bpharma_clean.csv'
    df.to_csv(output_csv_path, index=False)

    print(f"Data scraping and cleaning complete. Results saved to '{output_csv_path}'.")
else:
    print("No data was found to scrape.")
'''
import os
from bs4 import BeautifulSoup
import pandas as pd

# Directory containing HTML files
directory = '/content/btech/found'

# Initialize a list to store the scraped data
data = []

# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".html"):  # Ensure it's an HTML file
        file_path = os.path.join(directory, filename)

        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            file_data = file.read()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(file_data, 'html.parser')

        # Extract relevant elements
        div_1 = soup.find("div", {"class": "cont_outer"})
        if div_1:
            table = div_1.find("table", {"class": "cont_DIV_UN"})
            if table:
                div_2 = table.find("div", {"id": "midd_part_UN"})
                if div_2:
                    table_2 = div_2.find("table")
                    if table_2:
                        td_all = table_2.findAll("td", {"class": "border1"})

                        # Corrected index and length checks
                        sgpa = None
                        cgpa = None
                        if len(td_all) >= 6:
                            sgpa = td_all[-6].text.replace("SGPA", "").strip()
                        if len(td_all) >= 4:
                            cgpa = td_all[-4].text.replace("CGPA", "").strip()

                        # Append the scraped data to the list
                        data.append({
                            "file_name": filename,
                            "sgpa": sgpa,
                            "cgpa": cgpa
                        })
                    else:
                        print(f"Table 2 not found in {filename}.")
                else:
                    print(f"Div with id 'midd_part_UN' not found in {filename}.")
            else:
                print(f"Table with class 'cont_DIV_UN' not found in {filename}.")
        else:
            print(f"Div with class 'cont_outer' not found in {filename}.")

# Convert the list of dictionaries to a DataFrame
if data:  # Only create a DataFrame if there's data
    df = pd.DataFrame(data)

    # Clean up SGPA and CGPA columns, if needed
    df['sgpa'] = df['sgpa'].replace(r'\D', '', regex=True).replace('', None)
    df['cgpa'] = df['cgpa'].replace(r'\D', '', regex=True).replace('', None)

    # Save the cleaned data to a new CSV file
    output_csv_path = '/content/btech_clean.csv'
    df.to_csv(output_csv_path, index=False)

    print(f"Data scraping and cleaning complete. Results saved to '{output_csv_path}'.")
else:
    print("No data was found to scrape.")