from email import header
from importlib.resources import contents
from bs4 import BeautifulSoup
from matplotlib.cbook import strip_math
import requests
import csv

source=requests.get('https://www.hcpcsdata.com/Codes')
source.raise_for_status()

soup=BeautifulSoup(source.text,'html.parser')

rows=soup.find('tbody').find_all('tr',class_="clickable-row") 
with open('data.csv','w',encoding='utf8',newline='') as csv_file:
    writer=csv.writer(csv_file)
    header=['HCPCS Codes','Count','Description']
    writer.writerow(header) 
      
    for row in rows:
        cells=row.find_all('td')
        hcpcs=cells[0].get_text(strip=True)
        count=cells[1].get_text(strip=True)
        description=cells[2].get_text(strip=True)

        data=[hcpcs,count,description]
        print(data)
        writer.writerow(data)
