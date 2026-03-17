from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

#Header for request
HEADERS = ({'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36', 'Accept-Language':'en-US, en;q=0.5'})

#HTTP Request
Webpage = requests.get(url, headers=HEADERS)

#Parse the HTML content
soup = BeautifulSoup(Webpage.text, 'html.parser')

# print soup
soup

# Return all tables
soup.find_all('table')

# Return a specific class of table 
table_headers = soup.find_all('tr', class_ = 'static-row-header')

# Remove excess spaces and extract from specific line
table_headers_cleaned = [header.text.strip() for header in table_headers][0]

# Remove irrelevant characters
column_headers = table_headers_cleaned.split("\n")

import re
column_headers = [
    re.sub(r"\[.*?\]", "", header).strip()
    for header in column_headers
    if header.strip() != ""
]

# add the column header in a column DataFrame
df = pd.DataFrame(columns=column_headers)

# Extract and clean the rows data
all_rows = []

for row in soup.find_all("tr"):
    cols = row.find_all("td")
    row_data = [col.get_text(strip=True) for col in cols]

    if len(row_data) == len(column_headers):
        all_rows.append(row_data)

df = pd.DataFrame(all_rows, columns=column_headers)

# Print the Table
df

#Export the table to csv file
df.to_csv(r"C:\Users\DELL\OneDrive\Attachments\world_bank.csv", index = False)







