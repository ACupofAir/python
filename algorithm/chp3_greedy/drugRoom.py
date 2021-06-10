#%%
class cow:
    def __init__(self, begin, end):
        self.start = begin
        self.end = end
#%%
# cow sort by end time
def countBadCow(cows, bullpenNum):
  badCount = 0
  sorted_cows = sorted(cows,key=(lambda x:x.end))
  bullpens = [0]*bullpenNum
  for cow in sorted_cows:
    bullpenEarlyest = min(bullpens)
    if cow.start < bullpenEarlyest:
      badCount += 1
    else:
      cows_replace_lst = []
      for cow_replace in bullpens:
        if cow_replace <= cow.start:
          cows_replace_lst.append(cow_replace)
      bullpens[bullpens.index(max(cows_replace_lst))] = cow.end
  return badCount
    
# %%
basic_line = input()
basic_line_int = list(map(int, basic_line.split()))
medic_num, room_num = basic_line_int[0], basic_line_int[1]
line = [[0]*3]*medic_num        
for i in range(medic_num):
  temp_line = input()
  line[i] = list(map(int, temp_line.split()))

# %%
lst_7 = []
lst_8 = []
lst_9 = []
lst_10 = []
lst_11 = []
lst_12 = []
for medic in line:
  if medic[2] == 7:
    lst_7.append(cow(medic[0], medic[1]))
  elif medic[2] == 8:
    lst_8.append(cow(medic[0], medic[1]))
  elif medic[2] == 9:
    lst_9.append(cow(medic[0], medic[1]))
  elif medic[2] == 10:
    lst_10.append(cow(medic[0], medic[1]))
  elif medic[2] == 11:
    lst_11.append(cow(medic[0], medic[1]))
  else:
    lst_12.append(cow(medic[0], medic[1]))

sum_bad_medic = countBadCow(lst_7, room_num) + countBadCow(lst_8, room_num)+ countBadCow(lst_9, room_num)+ countBadCow(lst_10, room_num)+ countBadCow(lst_11, room_num)+ countBadCow(lst_12, room_num)
print(medic_num - sum_bad_medic)
# %%
