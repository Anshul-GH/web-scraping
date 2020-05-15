# '''
# Code	Names	Country
# 1	a	France
# 2	b	France
# 3	c	USA
# 4	d	Canada
# 5	e	TOTO
# 6	f	TITI
# 7	g	Corona
# '''
# import pandas as pd
# df = pd.read_clipboard(sep='\s\s+')
# # print(df)

# df2 = df.loc[~df['Names'].isin(['f','b','c'])].copy()

# print(df2)

import numpy as np
import pandas as pd

# x = np.array([[1,2,3,1,2,3], 
#               [4,5,np.nan,3,5,np.nan], 
#               [7,8,9,4,5,6],])

# df = pd.DataFrame([x[0][1], x[0][2], x[0][3]])
# df = pd.DataFrame(x)
# print(df)
# print(df.dropna(axis=1))


import pandas as pd

# # for read_clipboard()
# '''
# Shooting	Rebounds	FieldGoal
# Team1	Team1Stat	Team1Stat	Team1Stat
# Team2	Team2Stat	Team2Stat	Team2Stat
# '''

# df = pd.read_clipboard(sep='\t+')

# df_new = df.T.reset_index()
# df_new = df_new[['Team1', 'index', 'Team2']]
# df_new.columns = ['Team1', '', 'Team2']

# print(df_new)


# '''
# COL1                         COL2           COL3     COL4       COL4bis     COL5  COL6 COL7  COL8     COL9  COL10 COL11  COL12           COL13
# APE.1:8-9(+):Canis_lups      SEQ1            0.171    1041       243        0     436  1476  1485     194   487   1091   3.305000e-05    52
# APE.1:8-9(+):Canis_lups      YP_SEQ1         0.171    1041       243        0     436  1476  1485     194   487   1091   3.305000e-05    52
# APE.1:8-9(+):Canis_lups      SEQ2            0.20     1081       248        1     436  1476  1485     194   497   1091   0.305000e-08    51
# APZ.1:1-1(-):Felis_catus     SEQ1            0.184     732       184        0      61   792  1071     233   458   1308   2.275000e-03    45
# OKI:3946-7231(-):Ratus       SEQ3            0.185     852       203        0     388  1239  3285     194   443  1091   5.438000e-05    53
# OKI:3946-7231(-):Ratus       XP_SEQ3         0.185     852       203        0     388  1239  3285     194   443  1091   5.438000e-05    53
# '''

# df = pd.read_clipboard()

# # print(df)

# df1 = df[['COL1','COL2']]
# print(df1)
# df2 = df.loc[:, df.columns != 'COL2']
# print(df2)




import pandas as pd
import random

low_Percent = float(60)
high_Percent = float(120)

val_List=[]
val_List1 =[]
# for j in range(3):


for j in range(3):

    for i in range(2):
                num1 = (random.randint(low_Percent, high_Percent))
                # print(num1)
                num1 = num1/100
                # print(num1)
                val_List.append(num1)
                df= pd.DataFrame({'rand_num': val_List})
    print(df)
    print(df.loc[2:2])
    val_List1.append(df.loc[2:2])
    # print(val_List1)
# val_List1