from pynput.keyboard import Key, Controller
from inputs import *
from sys import stderr
from logging import *
import time


#For outputs
maxsteer_angle = int(30) #in degrees
maxbreak = int(75) #hardest breaking allowed
maxaccel = int(80) #most power

keyboard = Controller()
i = 0

#Checks for usable gamepads
#for device in devices:
#    print(device)
accel = int()
brake = int()
steer = int()
base = True


def log():
        l  = getLogger()
        sh = StreamHandler(stderr)
        sh.setLevel(DEBUG)
        f  = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        sh.setFormatter(f)
        l.addHandler(sh)
        l.setLevel(DEBUG)

#For gamepads
while 1:
        
        #logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        l  = getLogger()
        sh = StreamHandler(stderr)
        sh.setLevel(DEBUG)
        f  = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        sh.setFormatter(f)
        l.addHandler(sh)
        l.setLevel(DEBUG)
        data = steer,accel,brake
        #logging.warning("Logged")
        #starttime=time.time()
        #while True:
        #  print(steer)
        #  l.info('%s', data)
        #  time.sleep(0.5 - ((time.time() - starttime) % 0.5))
        events = get_gamepad()
        for event in events:
                1
                #print(event.code)
                #print(event.state)
                #print(event.ev_type)
        if event.code == 'BTN_TL':
              #i += 1
              #print('click', i)
            if event.state == 1:
                print("BLINK_L")
        if event.code == 'BTN_TR':
              #i += 1
              #print('click', i)
            if event.state == 1:
                print("BLINK_R")
        if event.code == 'BTN_START' :
              break
        if 'BTN_SELECT' == event.code:
            if event.state == 1:
                print("happy")
        if 'BTN_SELECT' == event.code:
            if event.state == 1:
                print("happy")

                
        if 'BTN_NORTH' == event.code:
            if event.state == 1:
                print("Y")
        if 'BTN_SOUTH' == event.code:
            if event.state == 1:
                print("A")
        if 'BTN_EAST' == event.code:
            if event.state == 1:
                print("B")
        if 'BTN_WEST' == event.code:
            if event.state == 1:
                print("X")
                
        if 'ABS_HAT0Y' == event.code:
            if event.state == 1:
                print("down")
        if 'ABS_HAT0Y' == event.code:
            if event.state == -1:
                print("up")
        if 'ABS_HAT0X' == event.code:
            if event.state == 1:
                print("right")
        if 'ABS_HAT0X' == event.code:
            if event.state == -1:
                print("left")
                
        if 'ABS_RZ' == event.code:
            accel = round((event.state/255)*100, 1)
            #l.info('%s', data)
            print(accel)

        if 'ABS_Z' == event.code:
            brake = round((event.state/255)*-100, 1)
            if brake == (-0.0):
                brake = 0.0
            if accel > 0:
                accel = abs(0)
            #l.info('%s', data)
            print(brake)
        if 'ABS_RX' == event.code:
            #print(event.state)
            steer = round((event.state/32768)*100, 1)
            #print(steer)
            if 0 < abs(event.state) < 3525:
                steer = round(0, 1)
                if base == True:
                    base = False
                    print(steer)
                    #l.info('%s', data)
            if abs(event.state) >= 3525:
                print(steer)
                #l.info('%s', data)
                base = True
        if 'ABS_RX' >= event.code:
            if abs(event.state) >= 32765:
                print("FULL")
        if 'ABS_RX' >= event.code:
            #steer = (event.state/)
            1
        #if steer == 0 or brake == 0 or accel == 0:
        #    l.info('%s', data)

    #    if 'ABS_RY' == event.code:
            #print(event.state)
     #       steer = round((event.state/32768)*100, 1)
            #print(steer)
    #        if 0 < abs(event.state) < 3500:
    #            steer = 0 
   #             print(steer)
  #              1
   #         if abs(event.state) >= 3500:
   #             print(steer)
  #              1
  #      if 'ABS_RY' >= event.code:
  #          if abs(event.state) >= 32765:
 #               print("FULL")
  #      if 'ABS_RY' >= event.code:
            #steer = (event.state/)
  #          1


#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')



