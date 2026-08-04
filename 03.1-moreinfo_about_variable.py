# """
# Purpose: Demonstrate all important concepts about variables in Python
# """

# print("\n========== 1. IDENTIFIER vs VARIABLE ==========")

# # identifier only (not a variable yet)
# # x   ❌ this alone is just a name, no object bound

# x = 10   # now x is a VARIABLE (identifier + object binding)
# print("x =", x)


# print("\n========== 2. VARIABLE REFERS TO AN OBJECT ==========")

# a = 100
# b = a

# print("a =", a)
# print("b =", b)
# print("id(a) =", id(a))
# print("id(b) =", id(b))  # same object


# print("\n========== 3. DYNAMIC TYPING ==========")

# x = 10
# print("x =", x, "type:", type(x))

# x = "hello"
# print("x =", x, "type:", type(x))


# print("\n========== 4. REASSIGNMENT ==========")

# x = 10
# print("Before reassignment:", x, "id:", id(x))

# x = 20
# print("After reassignment :", x, "id:", id(x))


# print("\n========== 5. MUTABLE vs IMMUTABLE ==========")

# # Immutable example
# a = 10
# b = a
# b = 20

# print("Immutable:")
# print("a =", a)
# print("b =", b)

# # Mutable example
# lst1 = [1, 2, 3]
# lst2 = lst1
# lst2.append(4)

# print("\nMutable:")
# print("lst1 =", lst1)
# print("lst2 =", lst2)


# print("\n========== 6. MODIFICATION vs REASSIGNMENT ==========")

# nums = [1, 2]
# print("Original nums:", nums, "id:", id(nums))

# nums.append(3)   # modification
# print("After modification:", nums, "id:", id(nums))

# nums = [10, 20]  # reassignment
# print("After reassignment :", nums, "id:", id(nums))


# print("\n========== 7. VARIABLE SCOPE ==========")

# x = "global x"

# def demo_scope():
#     x = "local x"
#     print("Inside function:", x)

# demo_scope()
# print("Outside function:", x)


# print("\n========== 8. MULTIPLE ASSIGNMENT ==========")

# a, b, c = 1, 2, 3
# print("a =", a, "b =", b, "c =", c)


# print("\n========== 9. SAME VALUE, DIFFERENT VARIABLES ==========")

# x = 5
# y = 5
# print("x id:", id(x))
# print("y id:", id(y))

# # Immutable objects can be shared; mutable objects must be copied or newly created.
# # If objects are immutable, Python can store a single object in memory and let multiple identifiers refer to it.

# print("\n========== 10. DELETING A VARIABLE ==========")

# x = 50
# print("x =", x)
# del x
# # print(x)  # ❌ NameError if uncommented


# print("\n========== SUMMARY ==========")
# print("""
# 1. Identifier is just a name
# 2. Variable = identifier bound to an object
# 3. Variables refer to objects, not memory locations
# 4. Python is dynamically typed
# 5. Mutable and immutable types behave differently
# 6. Scope controls where variables are accessible
# """)


# ! ---------------
x = 5
y = 5

print(x == y)   # True
print(x is y)   # True (same interned object)


a = [1, 2]
b = [1, 2]

print(a == b)   # True  (same data)
print(a is b)   # False (different objects)


"""


! -----------------------------------------------------------------

#include <stdio.h>

int x = 0;

void func() {
    x++;
    printf("global x = %d\n", x);
}

int main() {
    func();
    func();
}

* my version : 
* means in global when function incremtn a value then in incremtn in memory it does not matter what is showing value in code menas x = 0 shoig but internally x become 1

? Correct version :

Even though the code shows int x = 0, when a function increments x, the value is changed in memory, and the code line does not “reset” it again.

! Why x = 0 does NOT run again
int x = 0;

This line runs once, when the program is loaded
Memory is allocated and initialized once

? After that:
    The program never comes back to this line
    Only the memory value changes


    
!----------------------------

! THEORY: How variables work in memory (in C language but same logics for python applied)
! 1 Program memory layout (simplified)

When a C program runs, memory is divided like this:

┌───────────────┐
│ Stack         │  ← local variables, function calls
├───────────────┤
│ Heap          │  ← dynamic memory (malloc)
├───────────────┤
│ Data Segment  │  ← global & static variables
├───────────────┤
│ Code Segment  │  ← instructions
└───────────────┘


=========================================================
THEORY + PRACTICAL:
How variables work in memory (Python perspective)
=========================================================

IMPORTANT NOTE:
---------------
Python does NOT expose low-level memory segments
(stack, data segment, heap) like C/C++.

But we can UNDERSTAND Python behavior using the SAME
CONCEPTUAL MODEL.

---------------------------------------------------------
CONCEPTUAL MEMORY MODEL (for understanding)
---------------------------------------------------------

1. Code Segment
   - Contains compiled bytecode (not important here)

2. Data Segment (Conceptual)
   - Global variables
   - Static-like variables
   - Exist for entire program lifetime

3. Stack (Conceptual)
   - Function call frames
   - Local variables
   - Created on function call
   - Destroyed when function returns

4. Heap
   - All Python objects (int, list, dict, etc.)
   - Managed by Python (GC + reference counting)

---------------------------------------------------------
RULE SUMMARY (VERY IMPORTANT)
---------------------------------------------------------
- Global variables persist across function calls
- Local variables are recreated every function call
- Static-like variables persist but have limited scope
- Code line `x = 0` does NOT re-run unless scope is re-entered

# =========================================================
# EXAMPLE 1: GLOBAL VARIABLE
# =========================================================

print("======== GLOBAL VARIABLE EXAMPLE ========")

# Global variable (module-level)
x = 0
THEORY:
-------
- `x` is created ONCE when the program starts
- Stored in a long-lived memory area (conceptually data segment)
- Every function uses the SAME `x`

def global_func():
    global x
    THEORY:
    ------
    - This function does NOT create a new x
    - It accesses the SAME global memory
    x += 1
    print("global x =", x)

# Function calls
global_func()   # x = 1
global_func()   # x = 2
global_func()   # x = 3

MEMORY WALKTHROUGH:
-------------------
Program start:
    x = 0

After first call:
    x = 1

After second call:
    x = 2

After third call:
    x = 3

IMPORTANT:
----------
The line `x = 0` in source code is only INITIALIZATION.
It does NOT reset x on every function call.

# =========================================================
# EXAMPLE 2: LOCAL VARIABLE
# =========================================================

print("\n======== LOCAL VARIABLE EXAMPLE ========")

def local_func():
    THEORY:
    ------
    - `x` is LOCAL to this function
    - Created every time the function is called
    - Destroyed when function returns
    x = 0
    x += 1
    print("local x =", x)

local_func()   # x = 1
local_func()   # x = 1
local_func()   # x = 1

MEMORY WALKTHROUGH:
-------------------
First call:
    stack frame created
    x = 0 -> 1
    stack frame destroyed

Second call:
    NEW stack frame
    x = 0 -> 1

IMPORTANT:
----------
Even if memory address looks same internally,
the variable is NEW each time.
Old value does NOT exist anymore.

# =========================================================
# EXAMPLE 3: STATIC-LIKE VARIABLE (FUNCTION ATTRIBUTE)
# =========================================================

print("\n======== STATIC-LIKE VARIABLE (FUNCTION ATTRIBUTE) ========")

def static_like_func():
    THEORY:
    ------
    Python has NO 'static' keyword.
    But function attributes behave like static variables.
    if not hasattr(static_like_func, "x"):
        static_like_func.x = 0   # initialized ONLY ONCE

    static_like_func.x += 1
    print("static-like x =", static_like_func.x)

static_like_func()   # 1
static_like_func()   # 2
static_like_func()   # 3

MEMORY WALKTHROUGH:
-------------------
- static_like_func.x lives as long as function object exists
- Function object lives for entire program
- Value is preserved between calls

SCOPE:
------
- Accessible ONLY via this function
- Not global

# =========================================================
# EXAMPLE 4: STATIC-LIKE USING DEFAULT ARGUMENT
# =========================================================

print("\n======== STATIC-LIKE VARIABLE (DEFAULT ARGUMENT) ========")

def default_static_func(x=[0]):
    THEORY:
    ------
    Default arguments are evaluated ONLY ONCE.
    This list is created at function definition time.
    x[0] += 1
    print("default-static x =", x[0])

default_static_func()   # 1
default_static_func()   # 2
default_static_func()   # 3

IMPORTANT WARNING:
------------------
This behavior is often a BUG source in Python.
Use carefully.

# =========================================================
# EXAMPLE 5: id() PROOF (MEMORY IDENTITY)
# =========================================================

print("\n======== ID() PROOF ========")

def id_demo():
    x = 0
    print("local x id:", id(x))

id_demo()
id_demo()

OBSERVATION:
------------
- Local x may reuse memory address
- But value is re-initialized
- Address reuse ≠ same variable

# =========================================================
# FINAL SUMMARY (READ THIS CAREFULLY)
# =========================================================

FINAL TRUTH:
------------

1. Global variables
   - Created once at program start
   - Stored in long-lived memory (conceptually data segment)
   - Changes persist across function calls

2. Local variables
   - Created on every function call
   - Stored in short-lived memory (conceptually stack)
   - Destroyed when function returns
   - Value does NOT persist

3. Static-like variables (Python technique)
   - Created once
   - Persist for program lifetime
   - Scope is limited to function

4. Source code vs Memory
   - `x = 0` in source code is ONLY initialization
   - It does NOT re-run unless scope is re-entered
   - CPU always works with MEMORY, not source text

---------------------------------------------------------
MENTAL MODEL (MOST IMPORTANT)
---------------------------------------------------------

- Code defines INITIAL state
- Memory holds CURRENT state
- Functions modify MEMORY
- Lifetime decides whether changes persist

---------------------------------------------------------
ONE-LINE TAKEAWAY:
---------------------------------------------------------

Global variables persist because they live in permanent memory,
local variables reset because their memory is destroyed,
static-like variables persist because they are created once.

---------------------------------------------------------
YOU NOW UNDERSTAND:
---------------------------------------------------------
✓ Stack vs data lifetime
✓ Why local resets but global increments
✓ Why code text does not reset values
✓ How Python simulates static behavior
✓ How memory changes across calls

END OF FILE
=========================================================






! ----------------------------------------------------------------------------------

=========================================================
PYTHON MEMORY MODEL — WHAT IS STORED WHERE (COMPLETE)
=========================================================

IMPORTANT TRUTH (READ FIRST):
-----------------------------
Python does NOT expose real OS stack/heap directly.
But Python STILL follows the SAME LOGICAL MODEL.

RULE:
-----
- OBJECTS are stored on the HEAP
- NAMES (variables) are stored in NAMESPACES
- FUNCTION CALLS create STACK FRAMES (conceptually)

---------------------------------------------------------
CONCEPTUAL MEMORY AREAS (PYTHON VIEW)
---------------------------------------------------------

1. STACK (Conceptual)
   - Function call frames
   - Local variable NAMES (references)
   - Destroyed after function returns

2. HEAP
   - ALL Python objects:
     int, float, str, list, dict, tuple, set, class, function
   - Managed by Python (GC + ref counting)

3. GLOBAL NAMESPACE (Module-level)
   - Global variable NAMES
   - Exists for entire program

---------------------------------------------------------
CRITICAL RULE (MOST IMPORTANT):
---------------------------------------------------------
VARIABLES DO NOT STORE VALUES
VARIABLES STORE REFERENCES TO OBJECTS
OBJECTS STORE DATA

# =========================================================
# EXAMPLE 1: INTEGER (IMMUTABLE)
# =========================================================

print("======== INTEGER EXAMPLE ========")

x = 10

MEMORY EXPLANATION:
-------------------
- Object 10 is created on the HEAP
- Name `x` is stored in GLOBAL namespace
- `x` points (references) to object 10

GLOBAL NAMESPACE:
    x  --->  HEAP OBJECT (int 10)

print("x =", x, "| id(x) =", id(x))

# =========================================================
# EXAMPLE 2: LIST (MUTABLE)
# =========================================================

print("\n======== LIST EXAMPLE ========")

lst = [1, 2, 3]

VERY IMPORTANT:
---------------
LIST IS ALWAYS STORED ON THE HEAP

- The LIST OBJECT lives on HEAP
- The NAME `lst` lives in GLOBAL namespace
- Elements inside list are REFERENCES to objects

GLOBAL NAMESPACE:
    lst  --->  HEAP OBJECT (list)
                    |
                    |---> int 1 (heap)
                    |---> int 2 (heap)
                    |---> int 3 (heap)

print("lst =", lst, "| id(lst) =", id(lst))

lst.append(4)

Mutation happens IN PLACE:
--------------------------
- SAME list object
- SAME id
- Contents changed

print("lst after append =", lst, "| id(lst) =", id(lst))

# =========================================================
# EXAMPLE 3: LOCAL VARIABLE (STACK FRAME)
# =========================================================

print("\n======== LOCAL VARIABLE (STACK) ========")

def local_example():
    x = 5
    MEMORY:
    -------
    - `x` NAME is in FUNCTION LOCAL namespace (stack frame)
    - Object 5 is on HEAP
    print("inside function x =", x, "| id(x) =", id(x))

local_example()
local_example()

IMPORTANT:
----------
- Function call creates NEW local namespace
- Name `x` is destroyed after return
- Object may remain if referenced elsewhere

# =========================================================
# EXAMPLE 4: LIST INSIDE FUNCTION
# =========================================================

print("\n======== LIST INSIDE FUNCTION ========")

def list_example():
    lst = [10, 20]
    MEMORY:
    -------
    - NAME `lst` is LOCAL (stack frame)
    - LIST OBJECT is on HEAP
    print("inside lst =", lst, "| id(lst) =", id(lst))

list_example()
list_example()

KEY OBSERVATION:
----------------
- List object created EACH call
- Different heap objects
- Local name destroyed after call

# =========================================================
# EXAMPLE 5: GLOBAL LIST MODIFIED INSIDE FUNCTION
# =========================================================

print("\n======== GLOBAL LIST MODIFICATION ========")

glist = [100]

def modify_global_list():
    glist.append(200)
    MEMORY:
    -------
    - `glist` NAME is global
    - Same list object modified
    print("inside glist =", glist, "| id(glist) =", id(glist))

modify_global_list()
modify_global_list()

WHY IT PERSISTS:
----------------
- Global name exists entire program
- Same heap object modified

# =========================================================
# EXAMPLE 6: IMMUTABLE REBINDING
# =========================================================

print("\n======== IMMUTABLE REBINDING ========")

def immutable_example():
    x = 10
    print("before x =", x, "| id =", id(x))
    x = x + 1
    print("after  x =", x, "| id =", id(x))

immutable_example()

IMPORTANT:
----------
- int is IMMUTABLE
- x + 1 creates NEW object
- Name `x` is rebound

# =========================================================
# EXAMPLE 7: MUTABLE VS IMMUTABLE SUMMARY
# =========================================================

MUTABLE OBJECTS (stored on HEAP):
--------------------------------
- list
- dict
- set
- bytearray
- custom objects

→ Can change IN PLACE
→ Same id

IMMUTABLE OBJECTS (stored on HEAP):
----------------------------------
- int
- float
- str
- tuple
- frozenset

→ Cannot change
→ New object created on modification

# =========================================================
# FINAL MASTER TABLE (READ THIS)
# =========================================================

WHERE IS WHAT STORED?
--------------------

NAME (variable):
- Stored in namespace (global/local)
- Think of it as STACK / DICTIONARY ENTRY

OBJECT (data):
- ALWAYS stored on HEAP

LIST:
- List object → HEAP
- Variable name → namespace

INT:
- Int object → HEAP
- Variable name → namespace

FUNCTION CALL:
- Local namespace → stack frame
- Destroyed after return

GLOBAL VARIABLE:
- Namespace exists entire program

---------------------------------------------------------
ONE-LINE FINAL TRUTH (MOST IMPORTANT):
---------------------------------------------------------

In Python, EVERYTHING is an object on the HEAP.
The STACK only holds REFERENCES (names) and CALL FRAMES.

=========================================================
END OF FILE — YOU NOW UNDERSTAND PYTHON MEMORY
=========================================================












































"""