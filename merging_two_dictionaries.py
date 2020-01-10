dict_1 = {'apple': 9, 'banana': 6}
dict_2 = {'banana': 4, 'orange': 8}

combined_dict = {**dict_1, **dict_2}

print(combined_dict)
# Output
# {'apple': 9, 'banana': 4, 'orange': 8}


# returning functional params as tuple
def foo(*args):
    for a in args:
        print(a)


foo(1, 2, 3)


# syntax for merging dictionaries
def bar(**kwargs):
    for a in kwargs:
        print(a, kwargs[a])


bar(name='one', age=27)

