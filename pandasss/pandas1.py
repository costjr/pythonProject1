import pandas as pd
"""lst = ["Impact", 'Academics', 'and', 'Camps', 'Profesional', 'courses']
lst2 = [11, 22, 33, 44, 55, 66, 77]
df = pd.DataFrame(list(zip(lst, lst2)), columns=['Name', 'val'])
#df = pd.DataFrame(lst, index =['a', 'b', 'c', 'd', 'e', 'f'], columns=['Names'])
print(df)
"""
lst = [['Ion, 15'], ['Mihai, 16'], ['Vlad, 17'], ['Vasea, 18']]
df = pd.DataFrame(lst, columns=['Name','Age'])
print(df)