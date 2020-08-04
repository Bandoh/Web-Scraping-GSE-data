from bs4 import BeautifulSoup
import json
import requests

# weekly composite index url https://gse.com.gh/compositeindexhp/compositeindexhp/

# live composite index https://gse.com.gh/comp_index.json


def home_live_data():
    url = "https://gse.com.gh/comp_index.json"
    x={"data":[]}
    x['data'].append(requests.get(url).json()[0])

    return x
