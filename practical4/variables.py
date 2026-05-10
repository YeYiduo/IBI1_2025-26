# Week 4 Practical: Variables, Conditionals, and Boolean Logic
# Student: YeYiduo

# Population data points
a = 5.08
b = 5.33
c = 5.55

# Calculate population growth increments
d = b - a
e = c - b

print("d =", d)
print("e =", e)
print("d >= e =", d >= e)

# Determine if population growth is accelerating or decelerating
if d >= e:
    print("the population is decelerating")
else:
    print("the population is accelerating")

# ----------------------
# Boolean variables and logical operations
# ----------------------
X = True
Y = False

# Perform logical OR operation
W = X or Y
print("W =", W)

# Truth table for OR operation (as required)
# | X     | Y     | X OR Y |
# |-------|-------|--------|
# | True  | True  | True   |
# | True  | False | True   |
# | False | True  | True   |
# | False | False | False  |
