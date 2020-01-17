
import max30102
import hrcalc

m = max30102.MAX30102()

dataHR=[]

for i in range(20):
    red, ir = m.read_sequential()
    dataHR[i*100:(i+1)*100] = red
    hr, hr_valid, spo2, spo2_valid = hrcalc.calc_hr_and_spo2(ir[:100], red[:100])
    
    print(hr, hr_valid, spo2, spo2_valid)

