# Loops
# * While Loop
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count += 1
else:
    print('Count is over range')

# * For Loop
# ** iterator of list, string, tuple, dictionary, set
# *** for iterator in lst:
# ***     code goes here
numbers = [0, 1, 2, 3, 4]
for i in numbers:
    print(i)

# ** range(start, end, step)
lst = list(range(0, 11, 2))
print(lst)
for num in range(0, 9, 3):
    print(num)  # 0,3,6
else:
    print('Number is out the range of 0~8')

# ** pass (do nothing)
for n in range(11):
    pass
