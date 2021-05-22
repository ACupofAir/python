def maxProfit(prices):
      if not prices:
           return 0

      n = len(prices)
      f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
      for i in range(1, n):
          f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
          f[i][1] = f[i - 1][0] + prices[i]
          f[i][2] = max(f[i - 1][1], f[i - 1][2])

      return max(f[n - 1][1], f[n - 1][2])

lst_length = input()
line = input()
lst_test = list(map(int, line.split()))
print(maxProfit(lst_test))