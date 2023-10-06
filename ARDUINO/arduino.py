# import time
# from fhict_cb_01.custom_telemetrix import CustomTelemetrix
# board = CustomTelemetrix()



# def setup():
#     board.set_pin_mode_digital_output(5)
#     board.set_pin_mode_digital_output(6)
#     board.set_pin_mode_digital_output(7)
#     board.set_pin_mode_digital_output(8)



# def loop():
#     board.digital_write(8, 1)
#     time.sleep(0.5)
#     board.digital_write(8, 0)
#     time.sleep(0.5)
#     board.digital_write(5, 1)
#     time.sleep(0.5)
#     board.digital_write(5, 0)
#     time.sleep(0.5)
#     board.digital_write(6, 1)
#     time.sleep(0.5)
#     board.digital_write(6, 0)
#     time.sleep(0.5)
#     board.digital_write(7, 1)
#     time.sleep(0.5)
#     board.digital_write(7, 0)
#     time.sleep(0.5)

# setup()
# while True:
#     try:
#         loop()
#     except KeyboardInterrupt: 
#         print('shutdown')
#         board.shutdown()



# import time, sys

# from fhict_cb_01.custom_telemetrix import CustomTelemetrix
# #-----------
# # Constants
# #-----------
# BUTTON1 = 8

# #------------------------------
# # Initialized global variables
# #------------------------------
# level = 0
# prevLevel = 0

# #-----------
# # functions
# #-----------
# def ButtonChanged(data):
#     global level
#     level = data[2] # get the level
#     # Keep the callback function short and fast.
#     # Let loop() do the 'expensive' tasks.

# def setup():
#     global board
#     board = CustomTelemetrix()
#     board.set_pin_mode_digital_input_pullup(BUTTON1, callback = ButtonChanged)
#     # Note: Getting button level via callback ButtonChanged() is more 
#     #       accurate for Firmata. When button is pressed or release,
#     #       the ButtonChanged() function is called and this sets the 
#     #       level variable.

# def loop():
#     global prevLevel
#     # Only print button level when level changed.
#     if (prevLevel != level):
#         # Lets respond on button level change.
#         print(level)
#         prevLevel = level

# #--------------
# # main program
# #--------------
# setup()
# while True:
#     try:
#         loop()
#     except KeyboardInterrupt: # crtl+C
#         print ('shutdown')
#         board.shutdown()
#         sys.exit(0)  


# import time
# import sys
# from fhict_cb_01.custom_telemetrix import CustomTelemetrix


# # -----------
# # Constants
# # -----------
# BUTTON1PIN = 8
# REDLEDPIN = 4


# # -----------
# # functions
# # -----------
# def setup():
#     global board
#     board = CustomTelemetrix()
#     # set pin to input pullup
#     board.set_pin_mode_digital_input_pullup(BUTTON1PIN)
#     board.set_pin_mode_digital_output(REDLEDPIN)


# def loop():
#     time.sleep(0.01)  # Give Firmata some time to handle protocol.
#     data = board.digital_read(BUTTON1PIN)
#     if data:
#         level = data[0]
#         print(level)

#         if (level == 0):
#             board.digital_write(REDLEDPIN, 1)
#         else:
#             board.digital_write(REDLEDPIN, 0)


# # --------------
# # main program
# # --------------
# setup()
# while True:
#     try:
#         loop()
#     except KeyboardInterrupt:  # crtl+C
#         print('shutdown')
#         board.shutdown()
#         sys.exit(0)



# from fhict_cb_01.custom_telemetrix import CustomTelemetrix
# import time, sys

# #-----------
# # Constants
# #-----------
# POTPIN = 0 # analog pin A0

# #-----------
# # functions
# #-----------
# def setup():
#     global board
#     board = CustomTelemetrix()
#     board.set_pin_mode_analog_input(POTPIN)
#     time.sleep(0.1)

# def loop():
#     value = board.analog_read(POTPIN)
#     print(value)

# #--------------
# # main program
# #--------------
# setup()
# while True:
#     try:
#         loop()
#     except KeyboardInterrupt: # crtl+C
#         print ('shutdown')
#         board.shutdown()
#         sys.exit(0)  


# import time
# import sys
# from fhict_cb_01.custom_telemetrix import CustomTelemetrix

# # -----------
# # Constants
# # -----------
# BUTTON1PIN = 8
# BUTTON2PIN = 9

# REDLEDPIN = 4
# GREENLEDPIN = 5
# # -----------
# # functions
# # -----------


# def setup():
#     global board
#     board = CustomTelemetrix()
#     board.set_pin_mode_digital_input_pullup(
#         BUTTON1PIN)  # set pin to input pullup
#     board.set_pin_mode_digital_input_pullup(
#         BUTTON2PIN)  # set pin to input pullup
#     # wait for board to be ready
#     time.sleep(0.1)


# def loop():

#     time.sleep(0.01)  
#     data = board.digital_read(BUTTON1PIN)
#     data = board.digital_read(BUTTON1PIN)

#     if data:
#         level = data[0]
#         print(level)
#         if (level == 0):
#             board.digital_write(REDLEDPIN, 1)
#         elif(level == 0):
#             board.digital_write(GREENLEDPIN,1)
#         else:
#          board.digital_write(REDLEDPIN, 0)



#     level1, time_stamp1 = board.digital_read(BUTTON1PIN)
#     level2, time_stamp2 = board.digital_read(BUTTON2PIN)
#     print(level1, level2)

#     time.sleep(0.01)  # Give Firmata some time to handle protocol.

#     value = board.digital_read(8)
#     print(value) # returns a list of level and
#     # option 1:
#     level = board.digital_read(8)[0]
#     # option 2:
#     level, time_stamp = board.digital_read(8)


# # --------------
# # main program
# # --------------
# setup()
# while True:
#     try:
#         loop()
#     except KeyboardInterrupt:  # crtl+C
#         print('shutdown')
#         board.shutdown()
#         sys.exit(0)



# import time
# import sys
# from fhict_cb_01.custom_telemetrix import CustomTelemetrix


# BUTTON1PIN = 8
# BUTTON2PIN = 9

# REDLEDPIN = 4
# GREENLEDPIN = 5


# def setup():
#    global board
#    board = CustomTelemetrix()
#    board.set_pin_mode_digital_input_pullup(BUTTON1PIN)
#    board.set_pin_mode_digital_output(REDLEDPIN)
# def loop():
#    time.sleep(0.01)  
#    data = board.digital_read(BUTTON1PIN)
#    if data:
#        level = data[0]
#        print(level)
#        if (level == 0):
#            board.digital_write(REDLEDPIN, 1)
#        else:
#            board.digital_write(REDLEDPIN, 0)


# setup()
# while True:
#    try:
#        loop()
#    except KeyboardInterrupt: 
#        print('shutdown')
#        board.shutdown()
#        sys.exit(0)




















# import time
# import sys
# from fhict_cb_01.custom_telemetrix import CustomTelemetrix

# # -----------
# # Constants
# # -----------
# BUTTON1PIN = 8
# BUTTON2PIN = 9

# REDLEDPIN = 4
# GREENLEDPIN = 5

# # -----------
# # functions
# # -----------


# def setup():
#     global board
#     board = CustomTelemetrix()
#     board.set_pin_mode_digital_input_pullup(
#         BUTTON1PIN)  # set pin to input pullup
#     board.set_pin_mode_digital_input_pullup(
#         BUTTON2PIN)  # set pin to input pullup
#     # wait for board to be ready
#     time.sleep(0.1)
#     board = CustomTelemetrix()
#     board.set_pin_mode_digital_output(GREENLEDPIN)
#     board.set_pin_mode_digital_output(REDLEDPIN)

# def loop():
#     board = CustomTelemetrix()

#     level1, time_stamp1 = board.digital_read(BUTTON1PIN)
#     level2, time_stamp2 = board.digital_read(BUTTON2PIN)
#     print(level1, level2)

#     time.sleep(0.01)  # Give Firmata some time to handle protocol.

#     # value = board.digital_read(8)
#     # print(value) # returns a list of level and
#     # option 1:
#     # level = board.digital_read(8)[0]
#     # option 2:
#     # level, time_stamp = board.digital_read(8)

# # def setup():
# #    global board
# #    board = CustomTelemetrix()
# #    board.set_pin_mode_digital_input_pullup(BUTTON1PIN)
# #    board.set_pin_mode_digital_output(REDLEDPIN)
# # def loop():
# #    time.sleep(0.01)  
#     data = board.digital_read(level1,level2)
#     if data:
#         level1 = data[0]
#         print(level1)
#         if (level1 == 0):
#             board.digital_write(REDLEDPIN, 1)
#         else:
#             board.digital_write(REDLEDPIN, 0)
    
#     if data:
#         level2 = data[0]
#         print(level2)
#         if (level2 == 0):
#             board.digital_write(GREENLEDPIN, 1)
#         else:
#             board.digital_write(REDLEDPIN, 0)



# # --------------
# # main program
# # --------------
# setup()
# while True:
#     try:
#         loop()
#     except KeyboardInterrupt:  # crtl+C
#         print('shutdown')
#         board.shutdown()
#         sys.exit(0)














# import time
# import sys
# from fhict_cb_01.custom_telemetrix import CustomTelemetrix

# # Constants
# BUTTON1PIN = 8
# BUTTON2PIN = 9

# REDLEDPIN = 4
# GREENLEDPIN = 5

# # Initialize variables for button levels
# level1 = 0
# level2 = 0

# def setup():
#     global board
#     board = CustomTelemetrix()
#     board.set_pin_mode_digital_input_pullup(BUTTON1PIN)
#     board.set_pin_mode_digital_input_pullup(BUTTON2PIN)
#     board.set_pin_mode_digital_output(GREENLEDPIN)
#     board.set_pin_mode_digital_output(REDLEDPIN)

# def loop():
#     global board, level1, level2  # Declare these variables as global

#     # Read the button levels
#     level1 = board.digital_read(BUTTON1PIN)
#     level2 = board.digital_read(BUTTON2PIN)

#     # Print the button levels
#     print(f"Button 1: {level1}, Button 2: {level2}")

#     # Check button levels and control LEDs
#     if level1 == 0:
#         board.digital_write(REDLEDPIN, 1)
#     else:
#         board.digital_write(REDLEDPIN, 0)

#     if level2 == 0:
#         board.digital_write(GREENLEDPIN, 1)
#     else:
#         board.digital_write(GREENLEDPIN, 0)

# # Main program
# setup()
# while True:
#     try:
#         loop()
#     except KeyboardInterrupt:  # Ctrl+C
#         print('Shutdown')
#         board.shutdown()
#         sys.exit(0)











# import time
# import sys
# from fhict_cb_01.custom_telemetrix import CustomTelemetrix


# BUTTON1PIN = 9  
# BUTTON2PIN = 8  

# REDLEDPIN = 4
# BLUELEDPIN = 6

# level1 = 0
# level2 = 0



# def setup():
#     global board
#     board = CustomTelemetrix()
#     board.set_pin_mode_digital_input_pullup(BUTTON1PIN)
#     board.set_pin_mode_digital_input_pullup(BUTTON2PIN)
#     board.set_pin_mode_digital_output(BLUELEDPIN)
#     board.set_pin_mode_digital_output(REDLEDPIN)

# def loop():
#     time.sleep(0.01)
#     global board, level1, level2 

#     level1  = board.digital_read(BUTTON1PIN)
#     level2 = board.digital_read(BUTTON2PIN)


#     if level1:
#         j = level1[0]  
#         print(j)
#         if j == 0:
#             board.digital_write(BLUELEDPIN, 1) 
#         else:
#             board.digital_write(BLUELEDPIN, 0)  
#     if level2:
#         i = level2[0]
#         print(i)
#         if i == 0:
#             board.digital_write(REDLEDPIN, 1)
#         else:
#             board.digital_write(REDLEDPIN, 0)


# setup()
# while True:
#     try:
#         loop()
#     except KeyboardInterrupt:  
#         print('Shutdown')
#         board.shutdown()
#         sys.exit(0)


# from fhict_cb_01.custom_telemetrix import CustomTelemetrix
# import time, sys

# #-----------
# # Constants
# #-----------
# POTPIN = 0 # analog pin A0

# #-----------
# # functions
# #-----------
# def setup():
#     global board
#     board = CustomTelemetrix()
#     board.set_pin_mode_analog_input(POTPIN)
#     time.sleep(0.1)

# def loop():
#     value, timestamp = board.analog_read(POTPIN)
#     print(value)

# #--------------
# # main program
# #--------------
# setup()
# while True:
#     try:
#         loop()
#     except KeyboardInterrupt: # crtl+C
#         print ('shutdown')
#         board.shutdown()
#         sys.exit(0)  




# from fhict_cb_01.custom_telemetrix import CustomTelemetrix
# import time, sys

# #-----------
# # Constants
# #-----------
# POTPIN = 0 # analog pin A0
# GREENLEDPIN = 5 # adjust this to your red LED's pin

# #-----------
# # functions
# #-----------
# def setup():
#     global board, green_led_brightness
#     board = CustomTelemetrix()
#     board.set_pin_mode_analog_input(POTPIN)
#     board.set_pin_mode_analog_output(GREENLEDPIN)

#     green_led_brightness = 0  # Initialize the brightness to 
#     board.analog_write(GREENLEDPIN, green_led_brightness)  # Set initial brightness

# def loop():
#     global green_led_brightness

#     # Read the potentiometer value
#     value_list = board.analog_read(POTPIN)
#     # Map the potentiometer value to LED brightness (0 to 255)
#     if value_list is not None and len(value_list)> 0:
#         value = value_list[0]
#         green_led_brightness = int(value / 1023.0 * 255)

#     # Update the red LED brightness
#         board.analog_write(GREENLEDPIN, green_led_brightness)

#         print("Potentiometer Value:", value)
#         print("Green LED Brightness:", green_led_brightness)
    
#     time.sleep(0.1)

# #--------------
# # main program
# #--------------
# setup()
# while True:
#     try:
#         loop()
#     except KeyboardInterrupt: # crtl+C
#         print('shutdown')
#         board.shutdown()
#         sys.exit(0)



import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix

# -----------
# Constants
# -----------
LED_PINS = [4, 5, 6, 7]

# -----------
# functions
# -----------


def setup():
    global board
    board = CustomTelemetrix()
    for pin in LED_PINS:
        board.set_pin_mode_digital_output(pin)


def loop():
    for pin in LED_PINS:
        board.digital_write(pin, 1)
        time.sleep(0.5)
        board.digital_write(pin, 0)
        time.sleep(0.5)


# --------------
# main program
# --------------
setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:  # crtl+C
        print('shutdown')
        board.shutdown()
        sys.exit(0)


























# import time
# import sys
# from fhict_cb_01.custom_telemetrix import CustomTelemetrix


# # -----------
# # Constants
# # -----------
# BUTTON1PIN = 8
# REDLEDPIN = 4


# # -----------
# # functions
# # -----------
# def setup():
#     global board
#     board = CustomTelemetrix()
#     # set pin to input pullup
#     board.set_pin_mode_digital_input_pullup(BUTTON1PIN)
#     board.set_pin_mode_digital_output(REDLEDPIN)


# def loop():
#     time.sleep(0.01)  # Give Firmata some time to handle protocol.
#     data = board.digital_read(BUTTON1PIN)
#     if data:
#         level = data[0]
#         print(level)

#         if (level == 0):
#             board.digital_write(REDLEDPIN, 1)
#         else:
#             board.digital_write(REDLEDPIN, 0)


# # --------------
# # main program
# # --------------
# setup()
# while True:
#     try:
#         loop()
#     except KeyboardInterrupt:  # crtl+C
#         print('shutdown')
#         board.shutdown()
#         sys.exit(0)
