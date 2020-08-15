from bs4 import BeautifulSoup
import json
import requests
columns = ["daily_date","year_high","year_low","prev_closing_price","opening_price","closing_price","price_change","closing_bid_price","closing_offer_price","total_shares","total_value","last_trans_price"]
strColumns = ""

url = 'https://gse.com.gh/daily-shares-and-etfs-trades/'
def historical_per_company(company,from_date,to_date):
    company = company.upper()
    print(from_date)
    postData = {"tr_share_codes":company,"tr_value_fields":strColumns+",".join(columns),"tr_from_date":from_date,"tr_to_date":to_date,"advanced_query_generate":"Generate"}
    x = requests.post(url, data = postData)
    soup = BeautifulSoup(x.text, 'html.parser')
    a = soup.findAll('tr')
    a.pop(0)
    a.pop(0)
    companyName = company
    allData = {"company":companyName,"data":[]}
    for row in a:
        d = {}
        for index,data in enumerate(row):
            d.update({columns[index]:data.text})
            pass
        allData['data'].append(d)
        pass
    # print(allData)
    return allData