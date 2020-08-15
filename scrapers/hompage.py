from bs4 import BeautifulSoup
import json
import requests
import datetime as dt

# weekly composite index url https://gse.com.gh/compositeindexhp/compositeindexhp/

# live composite index https://gse.com.gh/comp_index.json


def home_live_data():
    url = "https://gse.com.gh/compositeindexhp/compositeindexhp/"
    x={"data":{}}
    data = requests.get(url).json()
    for i in range( len(data['x_axis'])):
        data["x_axis"][i] = data["x_axis"][i].split("<br>")[1]
        pass
    x['data'].update({"composite":data})
    url = "https://gse.com.gh/comp_index.json?{}".format(int(dt.datetime.now().timestamp() *1000))
    data = requests.get(url).json()
    x['data'].update({"top_gainers":data[0]['TopGainers']})
    x['data'].update({"top_value":data[0]['TopValue']})
    x['data'].update({"top_volume":data[0]['TopVolume']})
    return x
