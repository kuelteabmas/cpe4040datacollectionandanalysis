import csv
import pandas as pd
import matplotlib.pyplot as plt

data = []
hrdata = []
spodata = []

with open('hrdata.csv', 'r') as hrdatafile:
    csvReader = csv.reader(hrdatafile)
    for row in csvReader:
        data.append(row)

    for index in range(len(data)):
        hrdata.append(results[index][0])
        spodata.append(results[index][1])

hrdata = [float(i) for i in hrdata]
print(hrdata)
print(spodata)


plt.subplot(121)
plt.plot(hrdata,'r',marker = '.', ms = 10)
plt.title('HRData')
plt.ylabel('Heart Beat')
plt.xlabel('Set')


plt.subplot(122)
roll = pd.Series(hrdata).rolling(window=4).mean().iloc[4-1:].values
plt.plot(roll,marker= '.', ms = 10)
plt.title('4-Point Moving Average')
plt.ylabel('HRData')
plt.xlabel('Set')

plt.show