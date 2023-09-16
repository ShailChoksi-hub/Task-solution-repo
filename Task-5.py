# Input values as strings
a_str = "10"
b_str = "50"

# Convert str to int
a = int(a_str)
b = int(b_str)

# Swap
a = a + b
b = a - b
a = a - b

# Convert the integers back to strings for output
a_str = str(a)
b_str = str(b)

# Output
print("Strings after swap: a =", a_str, "and b =", b_str)
