import RPi.GPIO as GP
import time


def dec2bin(num):
    return [int(i) for i in bin(num)[2:].zfill(8)]



dac = [26,19,13,6,5,11,9,10]
GP.setmode(GP.BCM)
GP.setup(dac, GP.OUT)

try:
    while True:   
        b = float(input())/512
        a = 1
        if a == 'q':
            break
        if int(a) - float(a) != 0:
            print('Не целое число!')
            5/0
        if int(a) < 0:
            print('Отрицательное число!')
            5/0
        if int(a) > 255:
            print('Большое число!')
            5/0    
        for i in range(255):
            time.sleep(b)
            GP.output(dac, dec2bin(i)) 
        for q in range(255,0,-1):
            time.sleep(b)
            GP.output(dac, dec2bin(q))    
        break
    
except:
    print('ВВедено неверное значение!')   




finally:
    GP.output(dac, 0)
    GP.cleanup()