from flask import Flask, request
from current_gse import current_per_company,current_gse
from historical_gse import historical_per_company
from company_profile import profile_per_company, equities
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

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