#%%
def queen_ans_num(n):
    queen = [-1]*n
    count = 0 
    
    def available(row,col):
        for k in range(row):
            if queen[k]==col or queen[k]-col == k - row or queen[k]-col == row - k:
                return False
        return True
    
    def find(row):
        nonlocal count,n,queen
        if row == n:
            count += 1
        else:
            for col in range(n):
                if available(row,col):
                    queen[row]=col
                    find(row+1)
    
    find(0)
    return count
# %%
queen_n = []
while True:
    num = int(input())
    if num == 0:
        break
    else:
        queen_n.append(num)

for queen in queen_n:
    print(queen_ans_num(queen))
	

# %%
