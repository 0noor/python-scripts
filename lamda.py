my_list = [5, 4, 3]
print(list(map(lambda item: item*item, my_list)))

# sorting

a = [(0, 2), (4, 3), (9, 9), (10, -1)]


a.sort(key=lambda tup: tup[1])
print(a)
