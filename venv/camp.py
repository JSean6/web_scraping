import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.freecodecamp.org/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')

    links = soup.find_all('a', href=True)

    all_urls = []

    for link in links:
        url = link.get('href')

        if url and 'camp'in url:
            all_urls.append(url)

    if url:
        absolute_url = 

    else:
        print("NO URLS")
