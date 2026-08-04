
# ! First Program

print("First Program")

# ! print is a python built in function



"""
! In Python, a built-in function is a function that is already provided by Python itself, so you can use it directly without importing any module.

! Built-in functions are ready-to-use functions provided by Python to make programming easier and faster.

"""

# --------------------------------------------------
# 1. PRINT FUNCTION
# --------------------------------------------------
print("1. PRINT FUNCTION")
print("Hello, Python Built-in Functions!\n")


# --------------------------------------------------
# 2. INPUT FUNCTION
# --------------------------------------------------
print("2. INPUT FUNCTION")
# Uncomment below lines to test input
# name = input("Enter your name: ")
# print("Your name is:", name)
print("input() takes input from the user\n")


# --------------------------------------------------
# 3. TYPE CHECKING FUNCTIONS
# --------------------------------------------------
print("3. TYPE CHECKING FUNCTIONS")
x = 10
y = 3.5
z = "Python"

print(type(x))   # int
print(type(y))   # float
print(type(z))   # str
print()


# --------------------------------------------------
# 4. TYPE CONVERSION FUNCTIONS
# --------------------------------------------------
print("4. TYPE CONVERSION FUNCTIONS")
a = int("100")
b = float("12.5")
c = str(500)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print()


# --------------------------------------------------
# 5. MATHEMATICAL BUILT-IN FUNCTIONS
# --------------------------------------------------
print("5. MATHEMATICAL FUNCTIONS")
numbers = [10, 20, 30, 40]

print("Absolute:", abs(-25))
# Definition: abs() returns the absolute (positive) value of a number.
# It removes the negative sign, if present.

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Power:", pow(2, 3))
print()


# --------------------------------------------------
# 6. LENGTH FUNCTION
# --------------------------------------------------
print("6. LENGTH FUNCTION")
text = "Python"
items = [1, 2, 3, 4]

print(len(text))
print(len(items))
print()


# --------------------------------------------------
# 7. RANGE FUNCTION
# --------------------------------------------------
print("7. RANGE FUNCTION")
for i in range(1, 6):
    print(i)
print()


# --------------------------------------------------
# 8. SORTED FUNCTION
# --------------------------------------------------
print("8. SORTED FUNCTION")
unsorted_list = [5, 2, 9, 1]
sorted_list = sorted(unsorted_list)

print("Original:", unsorted_list)
print("Sorted:", sorted_list)
print()


# --------------------------------------------------
# 9. BOOLEAN FUNCTIONS
# --------------------------------------------------
print("9. BOOLEAN FUNCTIONS")
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print()


# --------------------------------------------------
# 10. ISINSTANCE FUNCTION
# --------------------------------------------------
print("10. ISINSTANCE FUNCTION")
num = 50
print(isinstance(num, int))
print(isinstance(num, str))
print()


# --------------------------------------------------
# 11. ENUMERATE FUNCTION
# --------------------------------------------------
print("11. ENUMERATE FUNCTION")
# it provide index on iterable set of data
languages = ["Python", "Java", "C++"]

for index, value in enumerate(languages):
    print(index, value)
print()


s = "Ansh"
for index , i in enumerate(s):
    print(index, i)


print()
d = {
    "A" : "a",
    "B" : "b",
    "C" : "c",
}
for index , i in enumerate(d):
    print(index, i)


# --------------------------------------------------
# 12. ZIP FUNCTION
# --------------------------------------------------
print("12. ZIP FUNCTION")
# zip() is a built-in function that combines corresponding elements from two or more iterables into tuples.
# "zip() pairs corresponding elements and returns them as tuples."

names = ["A", "B", "C"]
marks = [80,  90, 85]

# ! this will print separate
for n, m in zip(names, marks):
    print(n, m)
print()

z = list(zip(names, marks))
print(z) # [('A', 80), ('B', 90), ('C', 85)] same as using (a,b)
print()
# Then why write a, b?
    # Because a comprehension lets you modify or transform the values before producing the output.
    # Example 1: Convert names to uppercase
# res = [(a.upper(), b) for a, b in zip(names, marks)]
# ! in a list items
res = list((a.upper(),b) for a,b in zip(names, marks))
print(res) # [('A', 80), ('B', 90), ('C', 85)]   

# as stirng
s = [f"{a} : {b}" for a, b in zip(names, marks)]
print(s)
# --------------------------------------------------
# 13. HELP FUNCTION
# --------------------------------------------------
print("13. HELP FUNCTION")
print("Use help() to get documentation of any built-in function")
# Example:
# help(print)
# import math
# help(math)
# print()


# --------------------------------------------------
# SUMMARY
# --------------------------------------------------
print("SUMMARY")
print("Built-in functions are pre-defined functions in Python.")
print("They help perform common tasks without writing extra code.")
print("Examples: print(), len(), type(), max(), min(), sum(), range()")


"""
END OF FILE
"""


