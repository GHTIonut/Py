def filter_func(x):
    return x % 2 != 0

numbers = list(range(0, 10))

print(list(filter(filter_func, numbers)))

print(list(filter(lambda x: x % 2 != 0, numbers)))
