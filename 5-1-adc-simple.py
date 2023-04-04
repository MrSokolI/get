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
        for i in range(256):
            time.sleep(0.007)
            v = GP.input(comp)
            em = adc(i)
            sig = dec2bin(i)
            GP.output(dac,sig)
            volt = i/255*3.3
            if v == 0:
                print(volt)
                break       
except:
    print('Error')   

finally:
    GP.output(dac, 0)
    GP.cleanup()
