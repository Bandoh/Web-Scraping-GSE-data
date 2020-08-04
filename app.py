from flask import Flask, request, send_file
from scrapers.current_gse import current_per_company,current_gse
from scrapers.historical_gse import historical_per_company
from scrapers.company_profile import profile_per_company, equities
from scrapers.hompage import home_live_data
import json
app = Flask(__name__)

@app.route('/gse/index')
def hello_world():
    return home_live_data()

@app.route('/doc')
def helpp():
    return send_file("index.html")

@app.route('/gse/live/<company>', methods=['GET'])
def get_company_current(company):
    return current_per_company(company)


@app.route('/gse/live',methods=['GET'])
def get_all_current():
    return current_gse()

@app.route('/gse/historical', methods=['POST'])
def get_historical():
    # print(dir(request))
    data = request.data.decode("utf-8").replace("'", '"')
    data  = json.loads(data)
    return historical_per_company(data['company'],data['date_from'],data['date_to'])

@app.route('/gse/profile/<company>', methods=['GET'])
def get_profile(company):
    return profile_per_company(company)

@app.route('/gse/equities', methods=['GET'])
def get_equities():
    return equities()

if __name__ == "__main__":
    app.run()
    pass