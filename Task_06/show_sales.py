from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as r_sum:
    if len(argv) > 1:
        if len(argv) == 3:
            sl = (list(i.strip() for i in r_sum))[int(argv[1]):int(argv[2])]
            print(*sl)
        if len(argv) == 2:
            sl = (list(i.strip() for i in r_sum))[int(argv[1]):]
            print(*sl)
    if len(argv) <= 1:
        print(r_sum.read())
