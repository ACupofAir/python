#%%
def maxEncoder(num):
  max = num
  for i in range(2, num+1):
    if num % i == 0:
      base = num / i
      pow = i
      temp = base ** pow
      if temp > max:
        max = temp 
  return max


num_test = int(input())
print(int(maxEncoder(num_test)))
# %%
for i in range(1, 10):
  print(i)

# %%
