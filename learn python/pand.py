import pandas as pd
import numpy as np
'''
pandas have 1. Series 1D, 2. dataframe2D, 3. panel 3D

'''
#Series
s=pd.Series()
print(s)
data=np.array(['a','b','c','d'])
s=pd.Series(data,index=[100,101,103,104])
print(s)

data={'a':0,'b':1,"c":2}
s=pd.Series(data)
print(s)
print(s[:3])
print(s['a'])
print([['a','c','d']])


#DataFrame
#pd.DataFrame(data,index, columns, dtype, copy)
#-columns is np.arrange(n) default
#copy is False default
'pandas supports: List Dict Series Nparray DF'
df =pd.DataFrame()
print(df) #empty

#from lists:
data=[1,2,3,4,5]
df=pd.DataFrame(data)
print(df)

data=[['A',10],['B',20],['C',30]]
df=pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)

#from dict:
data={'Name':['a','b','c'],'Age':[20,30,40]}

df=pd.DataFrame(data,index=['rank1','rank2','rank3'])
print(df)
data=[{'a':1},{'b':2}]

print(df)
df1=df.copy()
df1['new']=[40,50]
df1=df1['new']+df['a']
print(df1)

del df1['new']
print(df1)
df1.pop('a')
print(df1)

print(df.loc['a'])

print(df.iloc[:,:])
#add row using append(df2)
df.drop(0,axis=0)

#panel
#pd.Panel(data, items, major_axis, minor_axis, dtype, copy)
#items=0
#major=1
#minor=2
data=np.random.rand(2,4,5)
p=pd.Panel(data)
print(p)

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print (p['Item1'])

#transpose
df.T

#
df.sum('columname')
df.mean()
'std, describe (summary)'

#timedelta

td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])


#merge
#pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,left_index=False, right_index=False, sort=True)



















