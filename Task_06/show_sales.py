from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(argv) > 1:
        if len(argv) == 3:
            sale = (list(i.strip() for i in f))[int(argv[1]):int(argv[2])]
            print(*sale)
        if len(argv) == 2:
            sale = (list(i.strip() for i in f))[int(argv[1]):]
            print(*sale)
    if len(argv) <= 1:
        print(f.read())
