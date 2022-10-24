# my_tuple = (1, 2, (5, 6, 7), 9, 0)
# print(my_tuple[2][2])
#
# my_tuple2 = (5, [7, 9], 0, 2, 5)
# print(my_tuple2)
#
# print(my_tuple2.count(5))
# print(my_tuple.index(9))

my_tuple = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(my_tuple.count(2))
print(len(my_tuple))

my_list = list(my_tuple)
print(my_list)

my_tuple2 = (5, 6, 7, 8)
a, b, c, d = my_tuple2
print(a, b, c, d)
