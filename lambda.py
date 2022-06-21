# Squareing the list with lamda
my_list = [1, 2, 3]
print(list(map(lambda x: x*x, my_list)))

# Sorting with Lambda keys
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(a, key=lambda i: i[1]))
