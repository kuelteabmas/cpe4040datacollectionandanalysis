import max30102
import hrcalc

import csv

m = max30102.MAX30102()

dataHR=[]

#create and open a new csv file
with open("hrdata.csv", "w") as csvFile:
    # create the csv writer object
    csvwriter = csv.writer(csvFile)
    
    for i in range(20):
        red, ir = m.read_sequential()
        dataHR[i*100:(i+1)*100] = red
        hr, hr_valid, spo2, spo2_valid = hrcalc.calc_hr_and_spo2(ir[:100], red[:100])
        
        print(hr, hr_valid, spo2, spo2_valid)
        
        # write the data on each row 
        csvwriter.writerow([hr, spo2])