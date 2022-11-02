students = ["yeasin", "Rafee", "Inka"]

# for student in students:
#     id = students.index(student) + 1
#     print(f" Id {id}: {student}")

numbers = [3, 45, 2, 7, 23, 9, 23, 21]
sum = 0

# for num in numbers:
#     sum = sum + num
#
# print(sum)

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 5, 7, 8]
sum_of_even = 0
sum_of_odd = 0

for num in list_numbers:
    if num % 2 == 0:
        sum_of_even = sum_of_even + num
    else:
        sum_of_odd = sum_of_odd + num

print(sum_of_even)
print(sum_of_odd)