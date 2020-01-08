n = 3  # number of repetitions

my_string = "abcd"
my_list = [1, 2, 3]

print(my_string * n)
# abcdabcdabcd

print(my_list * n)
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

# An interesting use case of this could be to define a list with a constant value — let’s say zero.
n = 4
my_list = [0]*n  # n denotes the length of the required list
print(my_list)
# [0, 0, 0, 0]
