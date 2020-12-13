#%%
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace

plt.plot([100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
         [1.80618, 1.8961, 2.00687, 2.09743, 2.16436, 2.17286, 2.11593, 2.07159, 2.11381, 2.0824, 2.28385, 2.40824])
                                                                                
plt.xlabel('NumOfElements')                                                     
plt.ylabel('Height/log2(NumOfElements')                                         
plt.ylim(0, 3)                                                                  
                                                                                
                                                                                
# %%                                                                            
x = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]            
y = [0, 298, 591, 888, 1188, 1490, 1814, 2351, 2403, 3101, 3471]                
plt.plot(x, y)                                                                  
plt.xlabel("k")                                                                 
plt.ylabel("time/us")                                                           
                                                                                
#%%                                                                             
y = [i for i in range(0, 1000, 100)]                                            
x = [i for i in range(1, 11)]                                                   
plt.plot(x, y)                                                                  
# %%                                                                            
                                                                                