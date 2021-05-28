def isSubsequence(s, t):
    n, m = len(s), len(t)
    i = j = 0
    while i < n and j < m:
         if s[i] == t[j]:
             i += 1
         j += 1
    return i == n


s_parent = input()
t_son = input()
# print(isSubsequence(t, s))
if isSubsequence(t_son, s_parent):
  print('true')
else:
  print('false')
