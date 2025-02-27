import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import sys

repo_url = "https://github.com/KranFer/boxfile.git"
repo_name = "boxfile"
repo_path = "/content/" + repo_name

if not os.path.exists(repo_path):
  !git clone {repo_url}

file_path = os.path.join(repo_path, "data.txt")

with open(file_path, "r") as f:
    fdata = f.read()

data = []

data_all = fdata.split("\n")
#print(data_all)

for data_part in data_all:
    data.append(data_part.split(","))

#print(data)



data1 = []
data2 = []
data3 = []
data4 = []
data5 = []

#print(123)

for dot in data[3:]:
    data1.append(int(float(dot[3])))
    data2.append(int(float(dot[5])))
    data3.append(int(float(dot[6])))
    data4.append(int(float(dot[7])))
    data5.append(int(float(dot[8])))

print(f'Номер пациента\t ===>>\t  Анализ1 \t Анализ2 \t Gender \t Age \t Smoking \n')

for a in range(len(data1)-1):
    print(f'{a}\t\t ===>>\t  {data1[a]} \t\t {data2[a]} \t\t {data3[a]} \t\t {data4[a]} \t {data5[a]} ')

plt.figure(1)
param1, = plt.plot(data1[:39],data2[:39],'ro',label='Corp')
param2, = plt.plot(data1[42:80],data2[42:80],'g^',label='HC')
param3, = plt.plot(data1[81:89],data2[81:89],'bs',label='Astma')
param3, = plt.plot(data1[89:],data2[89:],'o',label='Infected')
plt.figure(2)
param1, = plt.plot(data1[:39],data3[:39],'ro',label='Corp')
param2, = plt.plot(data1[42:80],data3[42:80],'g^',label='HC')
param3, = plt.plot(data1[81:89],data3[81:89],'bs',label='Astma')
param3, = plt.plot(data1[89:],data3[89:],'o',label='Infected')
plt.figure(3)
param1, = plt.plot(data1[:39],data4[:39],'ro',label='Corp')
param2, = plt.plot(data1[42:80],data4[42:80],'g^',label='HC')
param3, = plt.plot(data1[81:89],data4[81:89],'bs',label='Astma')
param3, = plt.plot(data1[89:],data4[89:],'o',label='Infected')
plt.figure(4)
param1, = plt.plot(data2[:39],data3[:39],'ro',label='Corp')
param2, = plt.plot(data2[42:80],data3[42:80],'g^',label='HC')
param3, = plt.plot(data2[81:89],data3[81:89],'bs',label='Astma')
param3, = plt.plot(data2[89:],data3[89:],'o',label='Infected')
plt.figure(5)
param1, = plt.plot(data2[:39],data4[:39],'ro',label='Corp')
param2, = plt.plot(data2[42:80],data4[42:80],'g^',label='HC')
param3, = plt.plot(data2[81:89],data4[81:89],'bs',label='Astma')
param3, = plt.plot(data2[89:],data4[89:],'o',label='Infected')
plt.figure(6)
param1, = plt.plot(data3[:39],data4[:39],'ro',label='Corp')
param2, = plt.plot(data3[42:80],data4[42:80],'g^',label='HC')
param3, = plt.plot(data3[81:89],data4[81:89],'bs',label='Astma')
param3, = plt.plot(data3[89:],data4[89:],'o',label='Infected')

plt.show()
