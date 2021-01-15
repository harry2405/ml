import random
import csv
attributes=[['sunny','rainy'],['warm','cold'],['normal','high'],['strong','weak'],['warm','cool'],['same','change']]
print(attributes)
num_attributes=len(attributes)
print("\n the most general hypothesis:['?','?','?','?','?','?'] \n");
print("\n the most specific hypothesis:['0','0','0','0','0','0']\n");
a=[];
print("\n the given training data set\n");
with open('C:\\Users\\sredd\\Desktop\\lab\\ws-1.csv','r') as csvFile:
	reader=csv.reader(csvFile)
	for row in reader:
	   a.append(row)
	   print(row)
print("\n the initial value of hypothesis:\n")
hypothesis=['0']*num_attributes
print(hypothesis)
for j in range(0,num_attributes):
	hypothesis[j]=a[0][j];
print("\n the find s:finding a maximally specific hypothesis\n")
for i in range(0,len(a)):
	if a[i][num_attributes]=='Yes':
		for j in range(0,num_attributes):
			if a[i][j]!=hypothesis[j]:
				hypothesis[j]='?'
			else:
				hypothesis[j]=a[i][j]
	print("for training example no:{0} the hypothesis is".format(i),hypothesis)
print("\n the maximally specific hypothesis for a given example:\n")
print(hypothesis)