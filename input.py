from pynput.keyboard import Key, Controller
from inputs import *


keyboard = Controller()
i = 0
clean = abs 

#Checks for usable gamepads
#for device in devices:
#    print(device)
accel = int()
brake = int()
steer = int()
base = True


#For gamepads
while 1:
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
            print(accel)

        if 'ABS_Z' == event.code:
            brake = round((event.state/255)*-100, 1)
            if brake == (-0.0):
                brake = 0.0
            if accel > 0:
                accel = abs(0)
            print(brake)
        if 'ABS_RX' == event.code:
            #print(event.state)
            steer = round((event.state/32768)*100, 1)
            #print(steer)
            if 0 < abs(event.state) < 3500:
                steer = 0 
                if base == True:
                    base = False
                    print(steer)
            if abs(event.state) >= 3500:
                print(steer)
                base = True
        if 'ABS_RX' >= event.code:
            if abs(event.state) >= 32765:
                print("FULL")
        if 'ABS_RX' >= event.code:
            #steer = (event.state/)
            1


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






