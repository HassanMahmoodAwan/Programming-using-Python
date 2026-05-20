"""
Variables: 
1. A variable is something which store a value.
2. Stored value in Memory Location.
3. Reusable and can be changed.

Naming Convention:
1. Meaningful and well descriptive name.
2. Starts with char or underscore.
3. Can contain char, digits and underscores. No Space allowed
4. Case Sensitive and not be any reserved keyword.
5. Lower Camel Case, like myVar, isConflict, idx, etc.
6. Constants always UPPERCASE, like PI, GRAVITY, etc.

Python is a Dynamically Typed language, so picks type automatically based on variable.
We optionally can specify type of variable.
"""

num01 = 10
num02 = 3.14
myName = "Hassan"
singleChar = 'A'
isFlag = True


student_name: str = "Hassan"
math_score: int = 90
english_score: float = 85.5
TOTAL_MARKS: int = 200
is_passed: bool = True


# ******* Type Conversion ********
num01 = str(num01)
num02 = int(num02)
isFlag = bool(singleChar)


# ******* Multiple Assignment ********
a, b, c = 1, 2.5, "Hello"

a = 1, 

