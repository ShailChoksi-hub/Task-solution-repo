# Input
a = "Hello"
b = "World"

# Swapping
a = a + b
b = a[:len(a) - len(b)]
a = a[len(b):]

# Print
print("Strings after swap: a =", a, "and b =", b)
