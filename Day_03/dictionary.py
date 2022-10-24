# customer = {"name": "Rafee", "dept.": "Computer Science", "height": 5.9, "weight": 52}
# print(customer)
# print(customer["dept."])

# dict = {1: 50, 2: [20, 10, 30], 3: {'s1': 100, 's2': 200, 's3': 300}, 'all': 'Numbers', 4: 'As big as I can do'}
# print(dict)

# dict = {"k1": ["e", "s", 'u'], "k2": ['t', 'w', 'm']}
# cap = dict["k2"][1].upper()
# print(cap)
# print(dict.keys())
# print(dict.values())
# print(dict.items())

my_dict = {'name': 'Yeasin', 'surname': 'Rafee', 'age': 22, 'occupation': 'student'}
print(my_dict)

my_dict['age'] = 30
my_dict['occupation'] = 'editor'
my_dict['country'] = 'Bangladesh'
print(my_dict)

my_dict2 = {"value_1": {"v1": 2, "v2": 4}, "points": {"p1": 34, "p2": [3, 4, 5]}}
print(my_dict2['points']['p2'][2])