def paperNum(money_value):
  money_nums = []
  money = [25, 10, 5, 1]
  for money_i in money:
    money_i_num = money_value // money_i
    money_nums.append(money_i_num)
    money_value %= money_i
  sum = money_nums[0]*25 + money_nums[1]*4 + money_nums[2]*2 + money_nums[3]*1
  return sum % 1000000007

def waysToChange(n):
     mod = 10**9 + 7
     coins = [25, 10, 5, 1]

     f = [1] + [0] * n
     for coin in coins:
         for i in range(coin, n + 1):
             f[i] += f[i - coin]
     return f[n] % mod

def wayToChange(n):
    coins = [1, 5, 10, 25]
    dp = [0] * (n + 1) 
    dp[0] = 1
    for coin in coins :
        for i in range(coin, n + 1) :
            dp[i] = (dp[i] + dp[i - coin])

    return dp[n] % 1000000007


caseNum = int(input())
print(paperNum(caseNum))
print(waysToChange(caseNum))
print(wayToChange(caseNum))