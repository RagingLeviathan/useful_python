def rotate(arr, d):
    return arr[d: ] + arr[:d]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    arr = rotate(arr, 2)
    print(arr)  # [3, 4, 5, 1, 2]
