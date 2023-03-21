import RPi.GPIO as GP
import time


def dec2bin(num):
    return [int(i) for i in bin(num)[2:].zfill(8)]



dac = [26,19,13,6,5,11,9,10]
GP.setmode(GP.BCM)
GP.setup(dac, GP.OUT)

try:
    while True:
        a = input()
        
        if a == 'q':
            break
        if int(a)- float(a) != 0:
            print('Не целое число!')
            5/0
        if int(a) < 0:
            print('Отрицательное число!')
            5/0
        if int(a) > 255:
            print('Большое число!')
            5/0    
        GP.output(dac, dec2bin(int(a))) 
        print(int(a)/255*3.3)
             

except:
    print('ВВедено неверное значение!')   




finally:
    GP.output(dac, 0)
    GP.cleanup()