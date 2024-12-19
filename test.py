items = [
    {"num": 1, "num1": 1},
    {"num": 3, "num1": 1},
    {"num": 2, "num1": 1},
    {'num': 2, "num1": 3},
    {'num': 2, "num1": 2}
]

def my_sort(a, b):
    print(a, b)
    if a['num'] > b['num']:
        return 1
    elif a['num'] < b['num']:
        return -1
    else:
        if a['num1'] > b['num1']:
            return 1
        elif a['num1'] < b['num1']:
            return -1
        else:
            return 0
# print(sorted(items))
new_items = sorted(items, key=lambda x: [x['num'], x['num1']])
print(new_items)

ls = [
    [1, 2, 1],
    [1, 1, 1],
    [1, 3, 1],
    [1, 2, 3],
    [1, 2, 2]
]
print(sorted(ls))
print(sorted(ls, key=lambda x: [x[0], x[1]]))