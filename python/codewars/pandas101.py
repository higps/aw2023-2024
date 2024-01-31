import pandas as pd

def rename_columns(df, names):  
    print(df)
    
    pass


df_input = pd.DataFrame(data=[[1,2,3,5], [4,5,6,6],[1,7,8,9]], columns=list('ABCD'))
names = ('A', 'B', 'C')
rename_columns(df_input, names)
