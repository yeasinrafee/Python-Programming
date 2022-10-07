from asyncio import run_coroutine_threadsafe


x = 4
y = 2

print(f"Sum of {x} and {y} is {x+y}")
print(f"Sub of {x} and {y} is {x-y}")
print(f"Mul of {x} and {y} is {x*y}")
print(f"Div of {x} and {y} is {x/y}")
print(f"Mod of {5} and {y} is {x%y}")
print(f"Power of {x} and {y} is {x**y}")
print(f"Squre Root of {x} is {x**0.5}")

#Rounding values:
print(round(10/3, 2))

num =10.67676767
print(round(num))
print(round(5 ** 0.5, 4))  