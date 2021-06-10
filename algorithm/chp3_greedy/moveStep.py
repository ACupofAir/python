#%%
def moveStep(lst):
  oddNum, evenNum = 0, 0
  for elm in lst:
    if (elm % 2 == 0):
      evenNum += 1
    else:
      oddNum += 1
  return min(evenNum, oddNum)

#%%
lenLst = input()
line = input()
lst_test = list(map(int, line.split()))
print(moveStep(lst_test))
# %%
