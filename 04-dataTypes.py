# ! data Types

print(type("A")) #! <class 'str'>
print(type(12)) #! <class 'int'>
print(type(1.2)) #! <class 'flaot'>
print(type(True)) #! <class 'bool'>
print(type(None)) #! <class 'NoneType'>

# ! type() is a python built in function 


# Checking for None (IMPORTANT)

# Always use is, not ==:

# if x is None:
#     print("No value yet")

# Correct final statement (remember this)

# None means a variable is assigned to a special object that represents the absence of a meaningful value.


# ! == → Value Equality
a = [1, 2]
b = [1, 2]

a == b   # True (same content)

# ! is → Identity Equality
a is b   # False (different objects)