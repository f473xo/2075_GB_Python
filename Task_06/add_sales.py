from sys import argv


sales = argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as f:
    print(sales, file=f)
