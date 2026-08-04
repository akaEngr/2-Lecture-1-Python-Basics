# ===============================================
# Python Variables, Memory, and References
# # ===============================================
# Easy Definition (Remember)

# ! CPython is the official and most widely used Python interpreter. It is written in the C programming language and is the interpreter that executes your Python code.

# ? interview : I use CPython, the official Python interpreter written in C.



# ! 2. What is Cache?
# Simple Definition
# ? A cache is a small storage area where frequently used objects are kept so they can be reused instead of creating them again.
# The goal of a cache is:
# ? ✅ Save memory
# ? ✅ Improve speed

# ! Python is a dynamically types language

# ! variable
# ? A variable is a name (reference) that points to an object in memory.
# ! Identifier
# ? An identifier is a user-defined name given to identities like class, functions, variables, modules, or any other object in Python.

# ! if age is indentifier then what is varaible ?
# ? so age is identifier but then you bind vlaue/object to this then it called variable

# * Correct Statement
  # Objects are stored in memory (heap memory).
  # Variables (identifiers) are stored in a namespace and refer to those objects.

# ! python(python interpreter) creates an object

"""
          Object in Memory
      +-----------------------+
      | Value : 10            |
      | Type  : int           |
      | ID    : 0x7fa123...   |  ← Memory address (identity)
      +-----------------------+




      Variable Table

x
│
▼
+-----------------------+
| Value : 10            |
| Type  : int           |
| ID    : 0x7fa123...   |
+-----------------------+
"""
# ? The variable name is called an identifier

"""
!
“In Python, a variable is an identifier that refers to an object stored in memory.”
When an assignment happens, Python creates (or reuses) an object and binds the identifier to that object.
The object has a unique identity, and the identifier accesses the object, not a raw memory address.

!
An identifier is just a name with no object bound to it.
When an identifier is assigned an object, it becomes a variable.

!
Two different identifiers can have the same id() because they both refer to the same object in memory.
This commonly happens with immutable objects, which Python safely reuses (interns).

Python reuses immutable objects in memory, so multiple identifiers can safely point to the same object.

*!
"""

name = "A"
age = 12


# ===============================================
# Assigning Values to Variables
# ===============================================

# ? When a value is assigned to a variable:
# ? 1. Python creates an object in memory to store the value.
# ? 2. That object has a unique memory address.
# ? 3. The variable name is just a reference (label) that points to that memory address.
# ? So, the variable doesn't hold the value itself; it points to the memory location where the value is stored.

x = 10

# Accessing the variable
print(x) # 10

# Checking memory address with id()
print(id(x)) # unique memory address of the object 10


# ===============================================
# Reference Example: Multiple Variables Pointing to Same Object
# ===============================================

x = 10
y = x  # y references the same object as x

print(id(x), id(y))  
# ✅ Both have the same memory address → they point to the same object in memory.



print("---------")
x = 10
y = 10
print(id(x), id(y))  
# 140703694497176 140703694497176 -> Same id
# 140703694497176 140703694497176 -> after run 
# Why IDs are same?
# This is due to integer interning, NOT immutability alone.
# Python pre-creates and reuses small integers:
# ! Typically: -5 to 256
x = 1000
y = 1000
print(id(x), id(y))  
# 1768705733104 1768705733104
# 2503696364016 2503696364016

print("---------")
p = [1,2,3]
q = [1,2,3]
print(id(p), id(q))  
# 1448157755072 1448157638528  -> Different id's
# 2694935852736 2694935736192 -> after run again

"""
| Object    | Same run           | Next run      |
| --------- | ------------------ | ------------- |
| List      | different ids      | different ids |
| Small int | same id (interned) | maybe same    |
| Large int | often different    | different     |
"""

"""
# ! ✅ Because memory allocation is fresh per run
✔ IDs change
✔ This is normal
❌ Not because lists are mutable
"""
# ===============================================
# Key Idea About References
# ===============================================

"""
? An object in memory can have multiple labels (variable names) pointing to it.
? Each label is just a reference to the same memory address.
? The object itself exists only once in memory.
"""

x = 10
y = x
z = x


# Visualization:

# x ──┐
# y ──┤──► [ object: 10 ]  (memory address: 1001)
# z ──┘


# ===============================================
# Important Notes
# ===============================================

"""
? Immutable objects (numbers, strings, tuples) → can not be changed.
  All labels see the same object but it cannot be modified.
"""
print("---------")
x = 10
y = 10
print(id(x), id(y))  
# 140703694497176 140703694497176 -> Same id
# 140703694497176 140703694497176 -> after run 
# Why IDs are same?
# This is due to integer interning, NOT immutability alone.
# Python pre-creates and reuses small integers:
# ! Typically: -5 to 256
x = 1000
y = 1000
print(id(x), id(y))  
# 1768705733104 1768705733104
# 2503696364016 2503696364016

"""
? Mutable objects (lists, dictionaries) → can be changed.
  Changing via one label affects all labels pointing to the same object.
"""




# ===============================================
# Step-by-Step Summary
# ===============================================

"""
| Step | Explanation                                            |
| ---- | ------------------------------------------------------ |
| 1    | Value (`10`) is created in memory.                     |
| 2    | Memory location is assigned to that value.            |
| 3    | Variable name (`x`) points to that memory address.    |
| 4    | When accessed, Python fetches the value from that address. |
"""




# ===============================================
# Another Details About Variables
# ===============================================

# ! 🔹 1. What is a Variable?
# ? A variable is a named storage location in memory that holds some data.

# ? It has:
# - Name → Identifier you use in code (x, age, price)
# - Value → The actual data it stores (10, "Hello", 3.14)
# - Type → The kind of data (int, float, string, bool)

# ? Think of it like a box with a label:
# ? the label = variable name, inside box = value.

x = 10         # Example variable
name = "Alice" # Example variable
pi = 3.14      # Example variable


# ! 🔹 2. Where is a Variable Stored?
# ? Variable references are stored in stack frames, while the actual objects they refer to are stored in the heap. Both are in RAM.

# ! 2.1 Stack Memory
# ? Stores local variables (created inside functions)
# ? Organized like a stack: Last In, First Out (LIFO)
# ? Automatically allocated when function runs, destroyed when function ends
# ? Fast but limited in size

def fun():
    x = 10  # stored in stack
    print(x)

# ! 2.2 Heap Memory
# ! definition : Heap is a dedicated area of RAM that programs use to allocate memory dynamically.

# * imp : So heap is not an object, dictionary, or data structure.
# * It is simply one part (region) of RAM.

# ? Stores dynamically allocated variables (objects in Python)
# ? Allocation/deallocation is handled by Python’s garbage collector
# ? Bigger but slower than stack

my_list = [1, 2, 3]  # allocated in heap


# ! 2.3 Data Segment (Global/Static) not exist in python (c/c++ concept)
# ? Stores global and static variables
# ? Exists for the entire program runtime

global_var = 100  # global variable


# ! 2.4 CPU Registers (sometimes)
# ? Compiler may put small/fast variables in CPU registers instead of RAM for optimization
register_var = 5  # Conceptual example


# ! 🔹 3. How is a Variable Stored in Memory?
# ? When you declare a variable:
# 1. Python allocates a memory address for the object
# 2. The value is stored in that memory location
# 3. The variable name acts as a reference (label) to that memory address

a = 10  # Example


# ! 🔹 4. How is a Variable Accessed After Storage?
# ? When you use a variable, Python fetches the value from the memory address it points to.
# ? If you assign a new value, Python updates the object reference.

a = 10
print(a)  # Access value

a = 30  # Update value
print(a)


# ! 🔹 4.1 Example with memory address and reference in Python
print(id(a))  # Shows memory address of the object a points to

b = a        # b references the same object as a
print(id(b)) # Same memory address as a


# ! 🔹 4.2 Pointers Concept (C/C++ analogy)
# ? In languages like C/C++, you can directly access memory addresses using pointers

# C/C++ style (Python does not use pointers this way):
# int a = 10;
# int *p = &a;  // p stores the address of a
# *p → accesses the value at that address (10)


l = [1,2,3]
l = [1,2,3]

# reassignment happens in mutable obejct so it creates new object with new id

a = 10
a = 10
# python resue object becuaes of small integer


# ! imp :
"""
! What is String Interning?
Simple Definition

String interning is an optimization where Python stores one copy of identical strings and lets multiple variables reference that same string object.

In simple words:

If two strings have the same value, Python may store only one string object in memory and let both variables point to it.

Example
a = "python"
b = "python"

print(id(a))
print(id(b))

Output (conceptually)

1400
1400









# --------------------------------


| Storage            | Permanent? | Stores                                                |
| ------------------ | ---------- | ----------------------------------------------------- |
| **RAM (Memory)**   | ❌ No       | Objects, variables, function calls while program runs |
| **Disk (SSD/HDD)** | ✅ Yes      | `.py` files, databases, images, documents, etc.       |

"""









"""

===============================================================================
                       PYTHON CONCEPTS STUDY SHEET
===============================================================================

STUDY_NOTES = 
1. ZIP()
-------------------------------------------------------------------------------
* Definition:
  Combines corresponding elements from multiple iterables into tuples.
* Returns:
  A zip object (iterator).
* Behavior:
  Stops automatically at the shortest iterable provided.
* Usage Examples:
  - Materialize results using list(zip(...)).
  - Works with list, tuple, string, dictionary, set, etc.

2. ENUMERATE()
-------------------------------------------------------------------------------
* Definition:
  Returns (index, value) tuples while iterating over an iterable.
* Parameters:
  `start=` specifies the starting index (default is 0).
* Compatibility:
  Works with all iterables.
* Dictionary Behavior:
  enumerate(dict) yields (index, key) pairs.

3. GENERATOR / LIST COMPREHENSION WITH ZIP()
-------------------------------------------------------------------------------
* Unpacking:
  `for a, b in zip(...)` unpacks the paired elements.
* Expression Output:
  `(a, b)` forms the generated output element.
* Why `a, b` Appears Twice:
  Once in the output expression `(a, b)` and once in the loop construct `for a, b in ...`.
* Choosing standard `list(zip(...))` vs. Comprehensions:
  - `list(zip(...))` is sufficient when simply pairing elements as-is.
  - Comprehensions are useful when you need to transform, calculate, or filter values.

4. ASCII CHARACTER SET
-------------------------------------------------------------------------------
* Definition:
  American Standard Code for Information Interchange; a character encoding standard.
* History & Purpose:
  Created to standardize text representation across different computers and devices.
* Range:
  0–127 (7-bit encoding, totaling 128 characters).
* Control Characters:
  Codes 0–31 and 127 (e.g., newline `\\n`, tab `\\t`, null `\\0`).
* Printable Characters:
  Codes 32–126 (includes letters, digits, punctuation, and space).
* ASCII vs. Unicode:
  ASCII is limited to standard English characters (128 total), whereas Unicode covers 
  virtually all world languages and symbols.

5. UNICODE
-------------------------------------------------------------------------------
* Inclusivity:
  Unicode fully includes the ASCII character set as its first 128 code points.
* Scope:
  Supports virtually all international writing systems, scripts, symbols, and emojis.

6. OBJECTS VS. VARIABLES
-------------------------------------------------------------------------------
* Objects:
  The actual data structures stored in heap memory.
* Variables (Identifiers):
  Names defined in a namespace.
* References:
  Variables do not store the actual data/objects; they store references (memory addresses) 
  pointing to the objects in the heap.

7. OBJECT IDENTITY (id())
-------------------------------------------------------------------------------
* Definition:
  `id(obj)` returns the unique identity (memory address in CPython) of an object.
* Key Principles:
  - The ID belongs exclusively to the object, not to the variable name.
  - Same object -> same ID.
  - Different objects -> different IDs.

8. MUTABLE VS. IMMUTABLE MEMORY BEHAVIOR
-------------------------------------------------------------------------------
* Reassignment:
  Reassigning a variable creates a brand-new object with a new ID.
* In-Place Modification:
  Modifying a mutable object in-place (e.g., list.append()) retains the same object and ID.
* Scenarios:
  - Immutable types (int, str, tuple): Operations create new objects.
  - Mutable types (list, dict, set): In-place updates mutate existing objects.

9. CPYTHON SMALL INTEGER CACHE
-------------------------------------------------------------------------------
* Mechanism:
  CPython pre-allocates and caches small integers (typically from -5 to 256).
* Effect:
  Multiple variables assigned numbers within this range point to the exact same object and share an ID.
* Note:
  This is an internal implementation optimization of CPython, not a guaranteed feature of the 
  Python language specification itself.

10. STRING INTERNING
-------------------------------------------------------------------------------
* Definition:
  Reusing single instances of immutable string objects to save memory and speed up comparisons.
* Purpose:
  Improves runtime performance and minimizes duplicate string creation.
* Mechanics:
  Multiple variables with identical interned strings point to the same single string object.
* Interning vs. Copying:
  Interning reuses existing memory references; copying allocates distinct new objects.
* Interned String Table:
  An internal global lookup table maintained by the Python interpreter.
* Memory Architecture:
  Variables in the namespace store references pointing to entries mapped inside the 
  Interned String Table residing in Heap Memory.

11. SYS MODULE
-------------------------------------------------------------------------------
* Definition:
  A standard built-in Python module providing functions and variables used to interact 
  directly with the Python interpreter.
* Function `sys.intern()`:
  Explicitly forces a string to be added to the internal interned string table.
* Usage Tip:
  Calling `sys.intern()` on a string once is enough; subsequent identical literals automatically 
  reuse the interned reference.

12. INTERNAL INTERNED STRING TABLE
-------------------------------------------------------------------------------
* Contents:
  Stores pointers/references to string objects, not duplicate raw data.
* Lifecycle:
  Exists only while the Python interpreter process is actively running.
* Destruction:
  Completely cleared and freed when the Python interpreter exits.

13. MEMORY DIAGRAMS CONCEPTUAL SUMMARY
-------------------------------------------------------------------------------
* Namespace:
  Maps variable names to memory addresses.
* Heap Memory:
  Stores the actual instances of objects.
* References:
  Pointers connecting namespace variables to heap memory locations.
* Interned String Table:
  An optimized index inside heap memory holding canonical references for shared strings.
* Multiple Variables -> One Object:
  Occurs during string interning, small int caching, or direct variable assignment (b = a).


    
Overall Topics Covered Today
✅ zip()
✅ enumerate()
✅ List/Generator comprehension with zip()
✅ ASCII
✅ Unicode
✅ Heap Memory
✅ Namespace
✅ Object vs Variable
✅ References
✅ id()
✅ Mutable vs Immutable memory behavior
✅ Small Integer Cache
✅ String Interning
✅ sys module
✅ sys.intern()
✅ Internal Interned String Table
✅ Memory diagrams and object sharing

These topics fit into the broader Python fundamentals section on memory management, built-in functions, iterables, and interpreter optimizations.


"""