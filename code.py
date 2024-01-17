def order_food(lst):
    d = {}
    for i in lst:
        if i['meal'] in d:
            d[i['meal']] += 1
        else:
            d[i['meal']] = 1
    return d
