
# ! Operators

# ! 1. Arithmetic Operators

"""
| Operator | Use                    | Example  | Result |
| -------- | ---------------------- | -------- | ------ |
| `+`      | Addition               | `5 + 3`  | `8`    |
| `-`      | Subtraction            | `10 - 4` | `6`    |
| `*`      | Multiplication         | `6 * 3`  | `18`   |
| `/`      | Division (float)       | `7 / 2`  | `3.5`  |
| `//`     | Floor Division         | `7 // 2` | `3`    |
| `%`      | Modulus (remainder)    | `7 % 3`  | `1`    |
| `**`     | Exponentiation (power) | `2 ** 3` | `8`    |

"""

# ! 2. Comparison (Relational) Operators

"""
| Operator | Use              | Example  | Result |
| -------- | ---------------- | -------- | ------ |
| `==`     | Equal to         | `5 == 5` | `True` |
| `!=`     | Not equal to     | `5 != 3` | `True` |
| `>`      | Greater than     | `7 > 2`  | `True` |
| `<`      | Less than        | `3 < 8`  | `True` |
| `>=`     | Greater or equal | `5 >= 5` | `True` |
| `<=`     | Less or equal    | `4 <= 6` | `True` |

"""

# ! 3. Logical Operators

"""
| Operator | Use                       | Example               | Result  |
| -------- | ------------------------- | --------------------- | ------- |
| `and`    | True if both true         | `(5 > 2) and (3 < 4)` | `True`  |
| `or`     | True if at least one true | `(5 < 2) or (3 < 4)`  | `True`  |
| `not`    | Negates condition         | `not (5 > 2)`         | `False` |

"""

# ! 4. Assignment Operators

"""
| Operator | Use                   | Example   | Equivalent To | Result    |
| -------- | --------------------- | --------- | ------------- | --------- |
| `=`      | Assign value          | `x = 5`   | –             | `x = 5`   |
| `+=`     | Add & assign          | `x += 3`  | `x = x + 3`   | `x = 8`   |
| `-=`     | Subtract & assign     | `x -= 2`  | `x = x - 2`   | `x = 6`   |
| `*=`     | Multiply & assign     | `x *= 2`  | `x = x * 2`   | `x = 12`  |
| `/=`     | Divide & assign       | `x /= 2`  | `x = x / 2`   | `x = 6.0` |
| `//=`    | Floor divide & assign | `x //= 2` | `x = x // 2`  | `x = 3`   |
| `%=`     | Modulus & assign      | `x %= 2`  | `x = x % 2`   | `x = 1`   |
| `**=`    | Exponent & assign     | `x **= 2` | `x = x ** 2`  | `x = 1`   |

"""

# ! 5. Bitwise Operators

"""
| Operator | Use                 | Example                  | Result (Binary) |          |       |              |
| -------- | ------------------- | ------------------------ | --------------- | -------- | ----- | ------------ |
| `&`      | AND                 | `5 & 3` → `0101 & 0011`  | `0001` → `1`    |          |       |              |
| `        | `                   | OR                       | `5              | 3`→`0101 | 0011` | `0111` → `7` |
| `^`      | XOR                 | `5 ^ 3` → `0101 ^ 0011`  | `0110` → `6`    |          |       |              |
| `~`      | NOT (bit inversion) | `~5` → flips bits        | `-6`            |          |       |              |
| `<<`     | Left shift          | `5 << 1` → `0101 → 1010` | `10`            |          |       |              |
| `>>`     | Right shift         | `5 >> 1` → `0101 → 0010` | `2`             |          |       |              |

"""

# ! 6. Identity Operators

"""
| Operator | Use                                          | Example      | Result                      |
| -------- | -------------------------------------------- | ------------ | --------------------------- |
| `is`     | Checks if two variables point to same object | `x is y`     | `True` if same object       |
| `is not` | Opposite of `is`                             | `x is not y` | `True` if different objects |

"""

x = [1,2,3]
y = x
z = [1,2,3]
print(x is y)   # True (same object)
print(x is z)   # False (same value but different objects)


# ! 7. Membership Operators

"""
| Operator | Use                           | Example            | Result |
| -------- | ----------------------------- | ------------------ | ------ |
| `in`     | Checks if element present     | `3 in [1,2,3]`     | `True` |
| `not in` | Checks if element not present | `5 not in [1,2,3]` | `True` |

"""
# Membership Operators Examples

# Example with list
numbers = [1, 2, 3, 4, 5]

print(3 in numbers)      # True (3 is present in the list)
print(10 in numbers)     # False (10 is not in the list)
print(7 not in numbers)  # True (7 is not present)

# Example with string
text = "Hello World"

print("H" in text)       # True (H exists in the string)
print("z" in text)       # False (z not in string)
print("World" in text)   # True (substring found)
print("world" in text)   # False (case-sensitive)

# Example with dictionary (checks only keys by default)
student = {"name": "Seth", "age": 21}

print("name" in student)     # True (key present)
print("Seth" in student)     # False (value not checked)
print("age" not in student)  # False (key exists)


"""
True
False
True
True
False
True
False
True
False
"""


# ! ✅ Summary
"""
# ! Arithmetic → Math ops
# ! Comparison → Relational check
# ! Logical → Boolean logic
# ! Assignment → Shorthand assignments
# ! Bitwise → Binary-level ops
# ! Identity → Object comparison
# ! Membership → Check in sequences
"""

print(2%3) # 2
print(3%2) # 1