# dicts.py

mydict = {"give_name": "Benson", "family_name": "Lee", "age": 16}

print(mydict)

# Accessing data in a dictionary
givenName = mydict["give_name"]
print(givenName)

# dictionaries do NOT store keys in any particular order
dictItems = mydict.item()
print(dictItems)

# Iterating over a dict
for k, v in mydict.items():
    print(f"Key: {k}\Value: {v}")

for k in mydict.keys():
    print(f"Key: {k}")

for v in mydict.values():
    print(f"Value: {v}")

hasKey = "given_name" in mydict
print(hasKey)


# Accessing data in a dictionary
givenName = mydict["give_name"]
print(givenName)
# NOT SAFE
# middleName = mydict["middle_name"]
# print(middleName)

givenName = mydict.get("given_name")
print(givenName)
middleName = mydict.get("middle_name")
print(middleName)
familyName = mydict.get("family_name")
print(familyName)

mydict.clear()
print(mydict)

mydict["one"] = 1
mydict["two"] = 2
print(mydict)

del mydict["one"]
print(mydict)
