import json

def get_data():
   with open('oprations.json', 'r', encoding="utf-8") as file:
       data = json.load(file)
   return data


def filter_data(data):
    data_filtr = []
    for el in data:
        if 'state' in el and el['state'] == 'EXECUTED':
            data_filtr.append(el)
    return data_filtr

def sort_data(data):
    data = sorted(data, key = lambda x: x['date'], reverse=True)
    return data[:5]