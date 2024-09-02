from math import sqrt

a = 6
b = -5 
c = 1

q = sqrt(b**2 - 4*a*c)

x1 = (-b - q)/(2*a)
x2 = (-b + q)/(2*a)

print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")

"""
python3 kjoreeksempel.py
x1 = 0.33, x2 = 0.50
"""


