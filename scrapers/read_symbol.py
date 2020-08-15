import json

def read_symbol_json():
    data = []
    with open("./data/sym2name.json") as source:
        data = json.load(source)
    return data