from bs4 import BeautifulSoup
import json
import requests


def profile_per_company(company):
    url = 'https://gse.com.gh/listed-company/{}/'.format(company)
    x = requests.get(url)
    soup = BeautifulSoup(x.text, 'html.parser')
    t_rows = soup.findAll('tr')
    t_rows.pop(0)
    allData = {"data":[{}]}
    for row in t_rows:
        allData['data'][0].update({row.th.text:row.td.text})
        pass
    return allData


def equities():
    url = 'https://gse.com.gh/profile-of-listed-companies/'
    x = requests.get(url)
    soup = BeautifulSoup(x.text, 'html.parser')
    t_rows = soup.findAll('tr')
    headers = t_rows.pop(0)
    headers = list(headers)
    allData = {"data":[{}]}
    for row in t_rows:
        d = {}
        for index, data in enumerate(row):
            d.update({headers[index].text:data.text})
        pass
        allData['data'].append(d)   
    return allData
