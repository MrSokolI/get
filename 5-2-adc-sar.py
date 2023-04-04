import RPi.GPIO as GP
import time


comp = 4
troyka = 17

def dec2bin(num):
    return [int(i) for i in bin(num)[2:].zfill(8)]

dac = [26, 19, 13, 6,5,11,9,10]
GP.setmode(GP.BCM)
GP.setup(dac, GP.OUT)
GP.setup(17, GP.OUT,initial = GP.HIGH)
GP.setup(comp, GP.IN)

def adc(vol):
    return int(vol/3.3*255)

try:
    while True:
        o = 0
        lol = [0 for i in range(8)]
        for i in range(8):
            lol[i] = 1
            GP.output(dac,lol)
            time.sleep(0.01)
            if GP.input(comp) == 0:
                lol[i] = 0
                GP.output(dac,lol)
                time.sleep(0.01)
            else:
                o += 2**(i)   
        print(o/255*3.3)
except:
    print('Error')   

finally:
    GP.output(dac, 0)
    GP.cleanup()
