from iteration_utilities import deepflatten
# this module needs to be installed ... type 'pip install iteration-utilities' in terminal


# if you only have one depth nested_list, use this
def flatten(l):
    return [item for sublist in l for item in sublist]


l = [[1, 2, 3], [3]]
print(flatten(l))
# [1, 2, 3, 3]

# if you don't know how deep the list is nested
l = [[1, 2, 3], [4, [5], [6, 7]], [8, [9,[10]]]]

print(list(deepflatten(l, depth=3)))
