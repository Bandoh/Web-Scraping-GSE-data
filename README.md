# GHANA STOCKS EXCHANGE API

The Ghana stocks exchange api is a simple and easy to use application programming interface, providing data taken from [Ghana Stock exchange website](http://gse.com.gh). There are currently 5 endpoints in the api providing response in JSON format.


# End Points

  - GET /gse/live
  - GET /gse/live/"somecompany"
  - POST /gse/historical
  - GET /gse/profile/"company"
  - GET /gse/equities

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
            "Div. per share for last fin. year GH(\u00a2)": "0",
            "Div. yield %": "0",
            "EPS GH(\u00a2)": "1.1",
            "EPS and PE ratios are based on results for the period": "1 MTHS- 1/03/2007p",
            "Equities": "COMPANY",
            "Issued Shares (mil.)": "100.95",
            "Market Capt. GH(\u00a2) million": "122.63",
            "NRF Investors' Holdings %": "",
            "P/E Ratio": "1",
            "Session": "5782"
        },
        {
            "Div. per share for last fin. year GH(\u00a2)": "0",
            "Div. yield %": "0",
            "EPS GH(\u00a2)": "0.1769",
            "EPS and PE ratios are based on results for the period": "6 MTHS- 30/06/2020p",
            "Equities": "ADB",
            "Issued Shares (mil.)": "300.8",
            "Market Capt. GH(\u00a2) million": "1,522.04",
            "NRF Investors' Holdings %": "",
            "P/E Ratio": "29",
            "Session": "5782"
        },
        ]
    }
```

