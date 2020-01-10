from functools import reduce
import math


def gcd(numbers):
    return reduce(math.gcd, numbers)


print(gcd([24,108,90]))  # 6
