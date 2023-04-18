from utils.utils import sort_data
from utils.utils import filter_data

def test_sort_data(test_data):
    sorted_data = sort_data(test_data)
    assert [x['date'] for x in sorted_data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2018-06-30T02:08:58.425572']
    assert [x['id'] for x in sorted_data] == [441945886, 41428829, 939719570]

def test_filter_data(test_data):
    filt_date = filter_data(test_data)
    assert [x['state'] for x in filt_date] == ['EXECUTED', 'EXECUTED', 'EXECUTED']