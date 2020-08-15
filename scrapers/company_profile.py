from bs4 import BeautifulSoup
import json
import requests
from scrapers.read_symbol import read_symbol_json
from scrapers.current_gse import current_per_company
def profile_per_company(symbol):
    company_name = ""
    data = read_symbol_json()
    company_name = data['data'][symbol.lower()]

    print(company_name)
    url = 'https://gse.com.gh/listed-company/{}/'.format(company_name)
    print(url)
    x = requests.get(url)
    soup = BeautifulSoup(x.text, 'html.parser')
    t_rows = soup.findAll('tr')
    t_rows.pop(0)
    allData = {"data":[{"info":{}}]}
    for row in t_rows:
        if row.td.a and row.th.text.lower() in "email":
            email = decodeEmail(row.td.a['data-cfemail'])
            allData['data'][0]['info'].update({row.th.text:email})
        else:
            allData['data'][0]['info'].update({row.th.text:row.td.text})

        if row.th.text.lower() in 'directors':
            break

        pass
    return allData

def decodeEmail(e):
    de = ""
    k = int(e[:2], 16)

    for i in range(2, len(e)-1, 2):
        de += chr(int(e[i:i+2], 16)^k)

    return de

def equities():
    columns = ["session","equities","issued_shares","market_capitalization","nrf_investment_holdings","eps_period","last_year_dps","dividend_yield","eps","p/e_ratio"]
    url = 'https://gse.com.gh/profile-of-listed-companies/'
    x = requests.get(url)
    soup = BeautifulSoup(x.text, 'html.parser')
    t_rows = soup.findAll('tr')
    headers = t_rows.pop(0)
    headers = list(headers)
    allData = {"data":[]}
    for row in t_rows:
        d = {}
        for index, data in enumerate(row):
            d.update({columns[index]:data.text})
        pass
        allData['data'].append(d)   
    return allData
