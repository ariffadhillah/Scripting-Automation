import requests
from bs4 import BeautifulSoup
import json

url = "https://www.cdph.ca.gov/Programs/CHCQ/LCP/CalHealthFind/Pages/SearchResult.aspx"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {}

    # scraping data
    table = soup.find('table', {'class': 'ms-listviewtable'})
    print(table)
    # rows = table.find_all('tr')

    # for row in rows:
    #     cols = row.find_all('td')
    #     if len(cols) == 4:
    #         name = cols[0].text.strip()
    #         address = cols[1].text.strip()
    #         city = cols[2].text.strip()
    #         phone = cols[3].text.strip()
    #         data[name] = {'address': address, 'city': city, 'phone': phone}

    # convert data to JSON format
    # json_data = json.dumps(data)
    # print(json_data)
else:
    print("Failed to retrieve data")
