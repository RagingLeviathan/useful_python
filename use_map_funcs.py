def multiply(n):
    return n * n


list = (1, 2, 3)
result = map(multiply, list)
print(tuple(result))  # {1, 4, 9}
