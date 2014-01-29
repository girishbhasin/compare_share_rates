import csv
from collections import OrderedDict, namedtuple

class share:
    def compare_rates(self):
        with open('data.csv') as f:
            reader = csv.reader(f)
            tup = namedtuple('tup', ['price', 'year', 'month'])
            d = OrderedDict()
            names = next(reader)[2:]
            for name in names:
                d[name] = tup(0, 'year', 'month')
            for row in reader:
                year, month = row[:2]
                for name, price in zip(names, map(int, row[2:])):
                    if d[name].price < price:
                        d[name] = tup(price, year, month)        
        while d:
            key, value = d.popitem()
            print key + ',' + value[1] + ',' + value[2] + ',' + `value [0]`
            
if __name__ == "__main__":
    share().compare_rates()
