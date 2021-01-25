import csv 
a=[] 
with open('mydata.csv')as traindata: 
 for row in csv.reader(traindata): 
 a.append(row) 
 print(row) 
import pandas as pd 
df = pd.read_csv('mydata.csv',header=none) 
a = df.values.tolist() 
print(df) 
n=len(a[0])-1 
print("\n the initial value of hypothesis: ") 
s = ['0'] * n 
g = ['?'] * n 
print ("\n the most specific hypothesis s0 :",s) 
print (" \n the most general hypothesis g0 :",g) 
s=a[0][:-1]
temp=[] 
print("\n candidate elimination algorithm\n") 
for i in range(len(a)): 
 if a[i][n]=="yes": 
   for j in range(n): 
     if a[i][j]!=s[j]: 
       s[j]='?' 
   for j in range(n): 
     for k in range(len(temp)): 
       if temp[k][j]!='?' and temp[k][j]!=s[j]: 
         del temp[k] 
 
 if a[i][n]=="no": 
   for j in range(n): 
     if s[j]!=a[i][j] and s[j]!='?': 
       g[j]=s[j] 
       if g not in temp: 
         temp.append(g) 
     g= ['?']*n 
 print("\n s{0}: ".format(i+1),s) 
 if (len(temp)==0): 
   print(" g{0}: ".format(i+1),g) 
 else: 
   print(" g{0}".format(i+1),temp)
