from bs4 import BeautifulSoup
import json
import requests

def index_creator():
    url = 'https://gse.com.gh/listed-company/'
    x = requests.get(url)
    soup = BeautifulSoup(x.text, 'html.parser')
    t_rows = soup.findAll('tr')
    t_rows.pop(0)
    allData = {"data":{}}
    for row in t_rows:
        cells = row.findAll('td')
        allData['data'].update({(cells[0].text.strip()).lower():cells[6].a['href'].split("/")[4].strip()})
    return allData

def save_file(path,data):
    with open(path+"sym2name.json",'w') as source:
        json.dump(data,source)
    pass

data = index_creator()
save_file("./data/",data)