import matplotlib.pyplot as plt
import csv
time=[]
p1=[]
p2=[]
with open('exportedVariables.csv',newline='') as data_file:
    reader=csv.reader(data_file, delimiter=',')
    for row in reader:
        time.append(row[0])
        p1.append(row[1])
        p2.append(row[2])
plt.plot(time,p1)


