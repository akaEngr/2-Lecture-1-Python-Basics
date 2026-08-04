
# ! Type Conversion 
# ? there are two types of conversion

# ! Type Conversion
# ? python interpreter do automatically itself

a = 2
b = 3.3
c = a+b
print(c) #! 5.3
print(type(c)) #! <class 'float'>


# print(type("3"+6))  #! can only concatenate str (not "int") to str
# print(type(None+6)) #! unsupported operand type(s) for +: 'NoneType' and 'int'


# ! Type Casting 
# ? we did it manually

a = int("2")
b = int(3.3)
x = a+b
print(x) #! 5
print(type(x)) #! <class 'int'>


