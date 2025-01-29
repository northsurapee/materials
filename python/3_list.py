# Create a List
list = ["abc", 34, True, 40, 34, "male"]
print(list)

# List length
print(len(list))

# Indexing (start from 0)
print(list[1])

# Negative Indexing
print(list[-1])

# Range of indexes
print(list[1:3])

# Check if Item Exists
if "abc" in list:
    print("'abc' is in the list!")

# Change Item Value
list[1] = 99
print(list)

# Append Items
list.append(0)
print(list)

