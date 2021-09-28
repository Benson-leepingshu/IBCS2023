# integer
myvar = 7
print(myvar)

# float
myvar = 7.3
print(myvar)

# string
myvar = "Now I'm a string"
print(myvar)

myvar = "I'm another string"
print(myvar)

myvar = """
This is a very long string
**************************
**************************
"""
print(myvar)

a, b = 5, 10
print(f"a: {a}\t b: {b}")
a, b = b, a
print(f"a: {a}\t b: {b}")
print("stuff")

myvar = 20
mytype = type(myvar)
print(mytype)

myvar = 3.5
mytype = type(myvar)
print(mytype)

myvar = "I am string"
mytype = type(myvar)
print(mytype)

# Some Operators are overloaded
a, b = 4, 6
result = a + b
print(result)

a, b = 4, 6.8
result = a + b
print(result)

a, b = "Number", 6
result = a + str(b)
result = f"{a}{b}"
print(result)
print(f"{a}{b}")

a, b = "3", 5
result = float(a) + b
print(result)
result = int(a) + b
print(result)
