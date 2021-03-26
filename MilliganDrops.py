#%%
import math
u = float(input("Input U: "))
t = float(input("Input t: "))
denominator_1 = t*(1+0.02*math.sqrt(t))
denominator_2 = u*math.pow(denominator_1,3/2)
result = 92800/denominator_2
print("q= ", result)   
print("q/e= ", result/1.60)
n = round(result/1.60)
print("n= ", n)
print("e'= ", result/n);
print("|e'-e|/e%= ", 100*abs(result/n-1.60)/1.60)
