
# listOflist = [[123, "A", "B", "C"], [456, "D", "E", "F"], [123, "G", "H", "I"]]

# test = {}

# temp=[{'key1':'value1','key2':'value2'},{'key1':'value3','key2':'value4'}]
# test['k1']['k2']['k3']=temp

# print(test)


# 61755415

# inp_date = '200605015'

# year = inp_date[:4]
# print(year)

# month = inp_date[4:6]
# print(month)

# from datetime import datetime

# datetime.strptime(inp_date[:6], '')

import pandas as pd

df = pd.DataFrame([{'Items': 'Product A + Product B + Product C'}, {'Items': 'Product A + Product B + Product B1 + Product C1'}])

My_Items = ['Product B1', 'Product C']

df['Item_list'] = df.Items.str.findall('|'.join(My_Items))
df['Item_list'] = [','.join(val) for val in df['Item_list']]

print(df)
