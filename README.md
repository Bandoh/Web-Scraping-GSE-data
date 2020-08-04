# GHANA STOCKS EXCHANGE API

The Ghana stocks exchange api is a simple and easy to use application programming interface, providing data taken from [Ghana Stock exchange website](http://gse.com.gh). There are currently 5 endpoints in the api providing response in JSON format.


# End Points

  - GET /gse/index
  - GET /gse/live
  - GET /gse/live/"somecompany"
  - POST /gse/historical
  - GET /gse/profile/"company"
  - GET /gse/equities

# GET /gse/index
This endpoint provides live composite index of Ghana stocks as well as top gainers, top losers , top value, top volume and more
>GET request to https://gse-gh.herokuapp.com/gse/index

>Response
 ```json
{
    "data": [
        {
            "CompIndexSeries": [
                {
                    "CLOSE": 2118.9002,
                    "TIME_SERIES": "04-23-2020 10:00:11.268375"
                },
                {
                    "CLOSE": 2142.5937,
                    "TIME_SERIES": "04-23-2020 10:08:27.930191"
                },
                {
                    "CLOSE": 2166.2871,
                    "TIME_SERIES": "04-23-2020 10:08:27.964129"
                }
            ],
            "FinIndexSeries": [
                {
                    "CLOSE": 1894.5739,
                    "TIME_SERIES": "04-23-2020 10:00:11.271613"
                },
                {
                    "CLOSE": 1894.5739,
                    "TIME_SERIES": "04-23-2020 10:12:19.367810"
                },
                {
                    "CLOSE": 1854.4188,
                    "TIME_SERIES": "04-23-2020 14:37:18.758906"
                }
            ],
            "TopGainers": [
                {
                    "CHGE_PRICE": 0.696,
                    "CLSE_PRICE": 7,
                    "N": 1,
                    "RANK": 1,
                    "STATS_DATE": "23-APR-20",
                    "SYMBOL": "EGH",
                    "TURNOVER": 16100
                },
                {
                    "CHGE_PRICE": 0.029,
                    "CLSE_PRICE": 0.69,
                    "N": 1,
                    "RANK": 2,
                    "STATS_DATE": "23-APR-20",
                    "SYMBOL": "MTNGH",
                    "TURNOVER": 193000
                }
            ],
            "TopLossers": [],
            "TopValue": [
                {
                    "CHGE_PRICE": 0.029,
                    "CLSE_PRICE": 0.69,
                    "N": 1,
                    "RANK": 1,
                    "STATS_DATE": "23-APR-20",
                    "SYMBOL": "MTNGH",
                    "TURNOVER_VALUE": 132900
                },
                {
                    "CHGE_PRICE": 0.696,
                    "CLSE_PRICE": 7,
                    "N": 1,
                    "RANK": 2,
                    "STATS_DATE": "23-APR-20",
                    "SYMBOL": "EGH",
                    "TURNOVER_VALUE": 112630
                },
                {
                    "CHGE_PRICE": 0,
                    "CLSE_PRICE": 2.8,
                    "N": 1,
                    "RANK": 3,
                    "STATS_DATE": "23-APR-20",
                    "SYMBOL": "TOTAL",
                    "TURNOVER_VALUE": 280
                }
            ],
            "TopVolume": [
                {
                    "CHGE_PRICE": 0.029,
                    "CLSE_PRICE": 0.69,
                    "N": 1,
                    "RANK": 1,
                    "STATS_DATE": "23-APR-20",
                    "SYMBOL": "MTNGH",
                    "TURNOVER": 193000
                },
                {
                    "CHGE_PRICE": 0.696,
                    "CLSE_PRICE": 7,
                    "N": 1,
                    "RANK": 2,
                    "STATS_DATE": "23-APR-20",
                    "SYMBOL": "EGH",
                    "TURNOVER": 16100
                },
                {
                    "CHGE_PRICE": 0,
                    "CLSE_PRICE": 2.8,
                    "N": 1,
                    "RANK": 3,
                    "STATS_DATE": "23-APR-20",
                    "SYMBOL": "TOTAL",
                    "TURNOVER": 100
                }
            ],
            "exchange_indicators": [
                {
                    "DOWN": 0,
                    "ENTRY_DATETIME": "23-APR-20",
                    "EQUAL": 33,
                    "TRADES": 9,
                    "UP": 2,
                    "VALUE": 245810,
                    "VOLUME": 209200
                }
            ],
            "fin_ind_wk": [
                {
                    "CLOSE": 2152.6479,
                    "HIGH": 2166.2871,
                    "LOW": 2118.9002,
                    "OPEN": 2097.1368,
                    "RNK": 2,
                    "TRADES": 9,
                    "TRUNC(ENTRY_DATETIME)": "23-APR-20",
                    "VALUE": 245810,
                    "VOLUME": 209200
                }
            ]
        }
    ]
}
```

# GET /gse/live
This endpoint provides the daily shares data for all company on the stock market
Example
>GET request to https://gse-gh.herokuapp.com/gse/live

>Response
 ```json
{
    "data": [
        {
            "closing_bid_price": "",
            "closing_offer_price": "",
            "closing_price": "0.81",
            "isn": "GH9999911",
            "last_trans_price": "0.51",
            "opening_price": "0.51",
            "prev_closing_price": "0.31",
            "price_change": "0",
            "share_code": "SOMESHARECODE",
            "total_shares": "0",
            "total_value": "0",
            "year_high": "0.11",
            "year_low": "0.11"
        },
        {
            "closing_bid_price": "",
            "closing_offer_price": "",
            "closing_price": "0.81",
            "isn": "GH9999900",
            "last_trans_price": "0.59",
            "opening_price": "0.59",
            "prev_closing_price": "0.11",
            "price_change": "0",
            "share_code": "SOMESHARECODE",
            "total_shares": "0",
            "total_value": "0",
            "year_high": "0.31",
            "year_low": "0.31"
        },
    ]
```
# GET /gse/live/"somecompany"
This endpoint provides the daily shares data for the requested company. Replace "somecompany" in the url with the company of your choice, it will be displayed only if it is listed on the Ghana stocks website
Example: Assuming cat is a company
>GET request to https://gse-gh.herokuapp.com/gse/live/cat

>Response
 ```json
{
    "data": {
        "closing_bid_price": "0.19",
        "closing_offer_price": "",
        "closing_price": "0.18",
        "isn": "GHFJKL9990",
        "last_trans_price": "0.19",
        "opening_price": "0.13",
        "prev_closing_price": "0.43",
        "price_change": "0.01",
        "share_code": "CAT",
        "total_shares": "787878",
        "total_value": "111255",
        "year_high": "0.4",
        "year_low": "0.1"
    }
```


# POST /gse/historical
This endpoint provides the historcal shares data of the requested company.
Example
>POST request to https://gse-gh.herokuapp.com/historical

FORM DATA
| FIELD      | DESCRIPTION |
| ---------- | ----------- |
| company    | The name of the company (string)                          |
| date_from  | The date from where to start collecting the data (date) -> format(MM/DD/YYYY) |
| date_to    | The date from where to end  (date) -> format(MM/DD/YYYY)                      |

>Response
 ```json
{
    "company": "SOMECOMPANY",
    "data": [
        {
            "daily_date": "2018-09-05",
            "year_high": "0.11",
            "year_low": "0.15",
            "prev_closing_price": "0.23",
            "opening_price": "0.112",
            "closing_price": "0.41",
            "price_change": "0.1",
            "closing_bid_price": "0.22",
            "closing_offer_price": "",
            "total_shares": "1000220",
            "total_value": "",
            "last_trans_price": "122"
        },
        {
            "daily_date": "2018-09-06",
            "year_high": "0.25",
            "year_low": "0.25",
            "prev_closing_price": "0.25",
            "opening_price": "0.25",
            "closing_price": "0.25",
            "price_change": "0.00",
            "closing_bid_price": "0.25",
            "closing_offer_price": "",
            "total_shares": "0",
            "total_value": "",
            "last_trans_price": "0.25"
        }
        ]
}
```
# GET /gse/profile/"company"
This endpoint provides the profile of the requested company
Example
>GET request to https://gse-gh.herokuapp.com/gse/profile/somecompany

>Response
 ```json
{
    "data": [
        {
            "Comments": "",
            "Company Name": "SOME company",
            "Date Incorporated": "",
            "Date Listed": "15 November 2001",
            "Directors": "Kofi Danso - Board Chairman,\nJose More - Chief Marketing Officer",
            "Email": "",
            "Fax": "Fax: +233 (0) 000 0000",
            "Issued Shares(GH) (mil.)": "",
            "Nature of Business": "Mine",
            "Postal Address": "Some Address",
            "Registered Office": "",
            "Security": "",
            "Stated Capital": "GHS843,100",
            "Telephone": "Tel: +233 (0) 111 111 111",
            "Types of Traded Securities": "",
            "Website": "www.somewebsite.com"
        }
    ]
}
```

# GET /gse/equities
This endpoint provides the equities data for all company on the stock market
Example
>GET request to https://gse-gh.herokuapp.com/gse/equities

>Response
 ```json
{
    "data": [
        {
            "last_year_dps": "0",
            "dividend_yield": "0",
            "eps": "1.1",
            "eps_period": "1 MTHS- 1/03/2007p",
            "equities": "COMPANY",
            "issued_shares": "100.95",
            "market_capitalization": "122.63",
            "nrf_investment_holdings": "",
            "p/e_ratio": "1",
            "session": "5782"
        },
        {
            "last_year_dps": "0",
            "dividend_yield": "0",
            "eps": "1.1",
            "eps_period": "1 MTHS- 1/03/2007p",
            "equities": "COMPANY",
            "issued_shares": "100.95",
            "market_capitalization": "122.63",
            "nrf_investment_holdings": "",
            "p/e_ratio": "1",
            "session": "5782"
        },
        ]
    }
```
