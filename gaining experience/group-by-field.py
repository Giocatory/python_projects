# У вас есть последовательность словарей или экземпляров, и вы хотите
# итерировать по данным, сгруппированным по значению конкретного поля
# (например, на дате).
from operator import itemgetter
from itertools import groupby


rows = [
    {'address': '5412 N CLARK', 'date': '17/04/2022'},
    {'address': '5148 N CLARK', 'date': '07/04/2022'},
    {'address': '5800 E 58TH', 'date': '07/06/2013'},
    {'address': '2122 N CLARK', 'date': '08/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2009'},
    {'address': '1060 W ADDISON', 'date': '07/02/2009'},
    {'address': '4801 N BROADWAY', 'date': '07/10/2023'},
    {'address': '1039 W GRANVILLE', 'date': '07/10/2023'},
]

# Сначала сортируем по нужным полям
rows.sort(key=itemgetter('date'))

# Итерируем в группах
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

# 07/02/2009
#   {'address': '5645 N RAVENSWOOD', 'date': '07/02/2009'}
#   {'address': '1060 W ADDISON', 'date': '07/02/2009'}
# 07/04/2022
#   {'address': '5148 N CLARK', 'date': '07/04/2022'}
# 07/06/2013
#   {'address': '5800 E 58TH', 'date': '07/06/2013'}
# 07/10/2023
#   {'address': '4801 N BROADWAY', 'date': '07/10/2023'}
#   {'address': '1039 W GRANVILLE', 'date': '07/10/2023'}
# 08/03/2012
#   {'address': '2122 N CLARK', 'date': '08/03/2012'}
# 17/04/2022
#   {'address': '5412 N CLARK', 'date': '17/04/2022'}