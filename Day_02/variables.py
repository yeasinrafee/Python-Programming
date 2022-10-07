from ast import Num


name = input("Enter your name: ")
birthYear =int(input("Enter your Birth Year: "))
age = 2022 - birthYear
job = input("Enter What do you do: ")

print(f"{name} is {age} years old. He is a {job}.")