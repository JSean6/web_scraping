import requests
from bs4 import BeautifulSoup
import csv

result = requests.get('http://github.com/')
google = requests.get('https://www.google.com')

# print(result.status_code)
# print(google.status_code)
# print(google.text)

src = google.content
# print(src)
soup = BeautifulSoup(src, 'lxml')
links = soup.find_all('a')
# print(links)
for link in links:
    url = link.get('href')
    if 'google' in url:
        link_text = link.text
        print(f'Link Text: {link_text}')