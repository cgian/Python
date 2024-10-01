# extracting, scraping the list of largest companies in US by revenue from wikipedia using Beautiful Soup in Python;
# then, saving the data in a CSV file using Pandas

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table', class_ = "wikitable sortable")

table_columns_strings = table.find_all('th')

table_columns = [title_names.text.strip() for title_names in table_columns_strings]

import pandas as pd

# creating dataframe

df = pd.DataFrame(columns = table_columns)

companies_data = table.find_all('tr')

for row in companies_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    # insert each row in dataframe
    df.loc[len(df)] = individual_row_data

print(df)

df.to_csv("Top 100 US Companies by revenue.csv", index = False)

