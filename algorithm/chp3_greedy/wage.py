#%%
def paperNum(wage):
  num = 0
  money = [100, 50, 10, 5, 2, 1]
  for money_i in money:
    money_i_num = wage // money_i
    num += money_i_num
    wage %= money_i
  return num

# %%
caseNum = input()
line = input()
lst_test = list(map(int, line.split()))
sum = 0
for case in lst_test:
  sum += paperNum(case)

# %%
print(sum)

# %%
