# %%
def cut_first(lst):
  right_scope = min(4, len(lst))
  first_cut_node = []
  for i in range(1, right_scope):
    before_part = int(lst[0:i])
    if (int(lst[i]) != 0) and (before_part > 0) and (before_part <= 127):
      first_cut_node.append(i)
  return first_cut_node

#%%
def cut_second(lst, first_node):
  lst_len = len(lst)
  lst_rest = lst[first_node:lst_len]
  right_scope = min(4, len(lst_rest))
  second_cut_node = []
  for i in range(1, right_scope):
    before_part = int(lst_rest[0:i])
    after_part = int(lst_rest[i:len(lst_rest)])
    if(int(lst_rest[i]) != 0) and (before_part > 0) and (before_part <= 127) and (after_part > 0) and (after_part <= 127):
      second_cut_node.append(i+first_node)
  return second_cut_node
#%%
def all_password(lst):
  if len(lst) > 10 or len(lst) < 3 or lst[0] == 0:
    print('[]')
  else:
    res = "["
    first_nodes = cut_first(lst)
    for first_node in first_nodes:
      second_nodes = cut_second(lst, first_node)
      for second_node in second_nodes:
        password_one = lst[0:first_node]
        password_two = lst[first_node:second_node]
        password_three = lst[second_node:len(lst)]
        res += '{'
        res += password_one 
        res += '、'
        res += password_two 
        res += '、'
        res += password_three 
        res += '}, '
    res_new = res[:-2]
    res_new += ']'
    print(res_new)
     
#%%
words = input()
all_password(words)

# %%
