import pandas as pd
data= {
    'Name' : ["Darshana","Ridam","Dipika","A","B","C"],
    'Age' : [21,56,89,22,54,90],
    'City' : ['New York','Canada', 'Iran','aa','bb','cc']
    }
d=pd.DataFrame(data)
print(d)
'''print(d['Age']>50)
e=d[d['Age']>50]
print(e)'''
print(d.loc[3,('Name','Age')])
print(d.iloc[2,[0,1]])
