name = input("Name?\n")
sales = float(input("Sales?\n"))

commission = (sales * 13)/100

print(f"Hey {name}, you have sold ${sales} and you'll get ${round(commission,2)}.") 