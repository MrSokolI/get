import RPi.GPIO as GP
import time
from matplotlib import pyplot as plt   
comp = 4
troyka = 17

def dec2bin(num):
    return [int(i) for i in bin(num)[2:].zfill(8)]
volt = []
dac = [26, 19, 13, 6,5,11,9,10]
GP.setmode(GP.BCM)
GP.setup(dac, GP.OUT)
GP.setup(17, GP.OUT,initial = GP.LOW)
GP.setup(comp, GP.IN)
def adc(vol):
    return int(vol/3.3*255)
o = 255
vrem = 0
tt = []
try:
    while o/255*3.3 < 3.2:
        o = 0
        lol = [0 for i in range(8)]
        for i in range(8):
            lol[i] = 1
            GP.output(dac,lol)
            time.sleep(0.02)
            vrem += 0.02
            if GP.input(comp) == 0:
                lol[i] = 0
                GP.output(dac,lol)
            else:
                o += 2**(i)
        tt.append(vrem)
        volt.append(o/255*3.3)  
        print(o/255*3.3)
    GP.output(17, GP.HIGH)
    while o/255*3.3 > 0.2 :
        o = 0
        lol = [0 for i in range(8)]
        for i in range(8):
            lol[i] = 1
            GP.output(dac,lol)
            time.sleep(0.02)
            vrem += 0.02
            if GP.input(comp) == 0:
                lol[i] = 0
                GP.output(dac,lol)
            else:
                o += 2**(i)
        tt.append(vrem)
        volt.append(o/255*3.3)  
        print(o/255*3.3)


except:
    print('Error')   

finally:
    print(volt)
    print()
    print(vrem)
    x = tt
    y = volt
    plt.plot(x, y, marker="o", c="g")
    plt.show()
    f = open('exp.txt', 'w')
    for i in range(len(tt)):
        f.write(str(volt[i])+'\n')

    GP.output(dac, 0)
    GP.cleanup()