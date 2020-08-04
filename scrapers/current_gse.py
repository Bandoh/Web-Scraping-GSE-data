from bs4 import BeautifulSoup
import json
import requests
columns = ["isn","share_code","year_high","year_low","prev_closing_price","opening_price","closing_price","price_change","closing_bid_price","closing_offer_price","total_shares","total_value","last_trans_price"]
strColumns = ""

url = 'https://gse.com.gh/daily-shares-and-etfs-trades/'
def current_gse():
    x = requests.get(url)
    soup = BeautifulSoup(x.text, 'html.parser')
    t_rows = soup.findAll('tr')
    t_rows.pop(0)
    allData = {"data":[]}
    for row in t_rows:
        d = {}
        for index,data in enumerate(row):
            d.update({columns[index]:data.text})
            pass
        allData['data'].append(d)
        pass
    return allData

def current_per_company(company):
    company = company.upper()
    x = requests.get(url)
    soup = BeautifulSoup(x.text, 'html.parser')
    a = soup.findAll('tr')
    a.pop(0)
    allData = {"company":company,"data":[]}
    d = {}
    for row in a:    
        if company in row.text:
            print("HI")
            for index,data in enumerate(row):
                d.update({columns[index]:data.text})
                pass
            break
        allData['data'] = d
        pass
    return allData