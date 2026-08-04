
# ! Practice lecture - 1

# ! WAP to input 2 numbers and print their sum
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))

"""
print(sum(a,b))
! ❌ Issue:

sum() is a built-in Python function, but it does not take two separate numbers as arguments.

Its syntax is:

sum(iterable, start=0)


iterable → a list, tuple, or other iterable of numbers

start → optional starting value

Example:
sum((1,2))
sum([1, 2, 3])       # returns 6
sum([1, 2, 3], 10)   # returns 16

"""

# ! CORRECT WAY
# sum = a+b 
# print(sum)
# ! i said correct way but is also worong keyword can not used as identifier
# total = a+b
# print(total)


# ! WAP to input side of a square and print it's area
# side_of_a_square = float(input("Enter side of a square : "))
# area_of_square = side_of_a_square**2
# print(area_of_square)



# ! WAP to input 2 flaoting point numbers and print their average
# a = float(input("Enter first number : "))
# b = float(input("Enter second number : "))
# avg = (a+b)/2
# print(avg) #! 2.5



# ! WAP to input 2 int numbers , a and b . print True if a is greater than or equal to b . if not print False.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print(a>=b)
