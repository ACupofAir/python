import pandas as pd
import numpy as np

data = [
    ['Abs', 'Fin', 'Helsi'],
    ['Dad', 'Mot', 'Vie'],
    ['Kirt', 'Bm', 'Cun'],
]
df = pd.DataFrame(data, columns=['Names', 'Country', 'City'])
print(df)
