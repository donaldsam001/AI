from sympy import symbols
from sympy.logic.boolalg import to_dnf, simplify_logic

# 1. Define the boolean variables
a, b, c = symbols('a b c')

# 2. Define the expressions using Python's bitwise operators for logic
# ~ is NOT, & is AND, | is OR
VT = (~a) & (~b | c)
# VP = (a & b) | (~b) | c

VP = (a & b ) | c
# 3. Analyze VT
print("--- VT Analysis ---")
print("Original VT:  ", VT)
print("Expanded VT:  ", to_dnf(VT)) # Expands to Sum of Products

# 4. Analyze VP
print("\n--- VP Analysis ---")
print("Original VP:  ", VP)
print("Expanded VP:  ", to_dnf(VP))
print("Simplified VP:", simplify_logic(VP)) # Simplifies redundant logic