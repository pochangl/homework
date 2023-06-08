values = input().split()

while values:
    values = map(int, values)
    total = sum(values)
    print('total:', total)
    values = input().split()

    if not values:
        print('沒啦')
