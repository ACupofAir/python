# Dictionary
# > A dictionary is a collection of unordered, modifiable, paired data type

# Creating
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct)

# Accessing Dictionary Items
print(dct['key1'])

# Adding Items
dct['key5'] = 'value5'
print(dct)

# Modifying Items
dct['key1'] = 'value_one'
print(dct)

# Removing Key and Value Pairs from a Dictionary
# * pop(key)
# * popitem() removing the last item
# * del
dct.pop('key1')
dct.popitem()
del dct['key2']
print(dct)

# Changing Dictionary to a List of Items
print(dct.items())

# Copy a Dictionary
dct_copy = dct.copy()
print(dct_copy)

# Clearing a Dictionary
print(dct.clear())

# Deleting a Dictionary
del dct

# Getting Dictionary Keys as a List
keys = dct_copy.keys()
print(keys)

# Getting Dictionary Values as a List
values = dct_copy.values()
print(values)
