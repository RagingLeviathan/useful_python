def most_frequent(list):
    return max(set(list), key=list.count)


numbers = [1, 2, 3, 2, 4, 3, 1, 3]
print(most_frequent(numbers))  # 3
