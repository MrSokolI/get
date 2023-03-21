import RPi.GPIO as GP
import time

GP.setmode(GP.BCM)
GP.setup(25, GP.OUT)
p = GP.PWM(25,50)
p.start(50)
p.stop()
a = 10
try:
    while True:
        
        if a == 'q':
            break
        if int(a)- float(a) != 0:
            print('Не целое число!')
            5/0
        if int(a) < 0:
            print('Отрицательное число!')
            5/0
        if int(a) > 100:
            print('Большое число!')
            5/0    
        p = GP.PWM(25,int(a))
        p.start(int(a))
        a = input()
        p.stop()

             

except:
    print('ВВедено неверное значение!')   


finally:
    GP.output(25, 0)
    GP.cleanup()