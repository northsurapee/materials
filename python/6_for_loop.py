# Loop through list items
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop through list index
for i in range(len(thislist)):
    print(thislist[i])

# Loop through dictionary key-value
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for this_is_key, this_is_value in thisdict.items():
    print(this_is_key, this_is_value)

# Break statement
for x in range(6):
    if x == 3:
        break
    print(x)

# Continue statement
for x in range(6):
    if x == 3:
        continue
    print(x)