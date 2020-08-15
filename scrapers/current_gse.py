from bs4 import BeautifulSoup
import json
import requests
from scrapers.read_symbol import read_symbol_json
columns = ["isn","share_code","year_high","year_low","prev_closing_price","opening_price","closing_price","price_change","closing_bid_price","closing_offer_price","volume","total_value","last_trans_price"]
strColumns = ""

url = 'https://gse.com.gh/daily-shares-and-etfs-trades/'
def current_gse():
    sym_data = read_symbol_json()
    x = requests.get(url)
    soup = BeautifulSoup(x.text, 'html.parser')
    t_rows = soup.findAll('tr')
    t_rows.pop(0)
    allData = {"data":[]}
    for row in t_rows:
        company_name=""
        d = {}
        for index,data in enumerate(row):
            d.update({columns[index]:data.text})
            pass
            if columns[index] in 'share_code':
                try:
                    company_name = sym_data['data'][data.text.lower()].replace("-"," ").capitalize()
                    pass
                except :
                    print(data.text)
                    pass
        d.update({"name":company_name})
        allData['data'].append(d)
        pass
    return allData


def real_time():
    sym_data = read_symbol_json()
    allData = {"data":[]}
    url = "https://gsestockfeed.com/"
    x = requests.get(url)
    soup = BeautifulSoup(x.text,"html.parser")
    a = soup.findAll('li')
    a.pop(0)
    for i in a:
        d = i.find('p')
        d  = d.text.replace(",","")
        so = d.split()
        try:
            allData['data'].append({"name":sym_data['data'][so[0].lower()].replace("-"," ").capitalize(),"share_code":so[0],"price":so[1],"price_change":so[2]})
        except :
            print(so[0])
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



if __name__ == "__main__":
    real_time()