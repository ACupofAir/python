# Lists

## Create
### using build-in function lst = list()
### using square brackers, []

## Unpacking List Items
lst = ['item', 'item2', 'item3', 'item4', 'item5']
first, second, third, *rest = lst
print(first)
print(second)
print(third)
print(rest)  # Output: ['item4','item5']

## Slicing Items from a List
### Syntax [start:end:step]
### Default start=0, end=len(lst)-1, step=1
all_item = lst[0:5:1]
print(all_item)

## Modifying Lists
### Adding Items
lst.append('item6')
print(lst)

### Inserting Items
lst.insert(2,'item3_new')
print(lst)

### Removing Items
#### Removing by item
lst.remove('item3_new')
print(lst)
#### Removing by pop()
lst.pop(2)
print(lst)

### Copying a List
lst_copy = lst.copy()
print(lst_copy)

### Clearing List
lst.clear()
print(lst)
lst.append('item0')

### Joining Lists
#### Plus Operator(+)
lst_join = lst + lst_copy
print(lst_join)

#### Using extend()
lst.extend(lst_copy)
print(lst)

### Reversing a List
lst.reverse()
print(lst)

### Sorting List Items
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)