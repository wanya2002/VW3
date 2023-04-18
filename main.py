from utils import get_data
from utils import filter_data
from utils import sort_data
import datetime

def main():
    '''Получение данных'''
    data = get_data()
    '''Фильтрация данных'''
    data = filter_data(data)
    '''Сортировка данных'''
    data = sort_data(data)

    for el in data:
        time = el['date']
        time_red = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = el["description"]
        where_to = el['to']
        amount = el["operationAmount"]['amount']
        curr = el["operationAmount"]["currency"]['name']
        if 'from' in el:
            where_from = el['from'].split()
            check = where_from[-1]
            where_from.pop(-1)
            card = "".join(where_from)
            print(f'{time_red} {description}\n{card} {check[0:4]} {check[5:7]}** **** {check[-4:]}'
                  f' -> **{where_to[-4:]}\n{amount} {curr} \n')
        else:
            print(f'{time_red} {description}\n'
                  f' -> **{where_to[-4:]}\n{amount} {curr}\n')





if __name__ == '__main__':
       main()


