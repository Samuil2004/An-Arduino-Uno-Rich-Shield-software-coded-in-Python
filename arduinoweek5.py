# import time
# from fhict_cb_01.custom_telemetrix import CustomTelemetrix
# board = CustomTelemetrix()

# board.displayShow(8173)
# time.sleep(1)

# board.displayShow(-0)
# time.sleep(1)

# board.displayShow("1E4A")
# time.sleep(1)

# board.displayShow(54)
# time.sleep(1)

# board.displayShow(0)
# time.sleep(1)

# board.displayShow(-137)
# time.sleep(1)

# board.displayShow('-3.141f')
# time.sleep(1)

# board.displayShow('3.141f')
# time.sleep(1)

# board.displayShow('0.643f')
# time.sleep(1)

# board.displayShow('-0.495f')
# time.sleep(1)

# board.displayShow('-0.00f')
# time.sleep(1)
# board.displayOff()
# board.shutdown()


# -------------------------------------------------------------------------------

import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix

board = CustomTelemetrix()


DHTPIN = 12 
BUTTON1PIN = 8
LDR_PIN = 2

def setup():
    global board
    board.displayOn()
    board.set_pin_mode_dht(DHTPIN, dht_type=11)
    board.set_pin_mode_digital_input_pullup(BUTTON1PIN)
    board.set_pin_mode_analog_input(LDR_PIN, callback=brightness, differential=10)

sensor_value = 0
def brightness(data):
    global sensor_value
    sensor_value = data[2]
    

counter = 0
def loop():
    
    global counter
    data = board.digital_read(BUTTON1PIN)
    if data:
            level = data[0]
            if level == 0:
                counter = counter + 1
                if counter > 3:
                     counter = 1

    if counter == 0:
         pass
    if counter == 1:
        humidity, temperature, timestamp = board.dht_read(DHTPIN)
        board.displayShow(temperature)
    elif counter == 2:
        humidity, temperature, timestamp = board.dht_read(DHTPIN)
        board.displayShow(humidity)
    elif counter == 3:
        board.displayShow(sensor_value)
    time.sleep(0.5)

setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:  # crtl+C
        print('shutdown')
        board.shutdown()


# ----------------------------------------------------------------------


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




# board = CustomTelemetrix()

# # The analog input pin that the Light Dependent Resitor (LDR)
# # is attached to
# LDR_PIN = 2

# # Here we define a callback function


# def callback_ldr(data):
#     # data list contains the following:
#     # [pin_type, pin_number, pin_value, raw_time_stamp]
#     sensor_value = data[2]
#     resistance_sensor = (1023-sensor_value)*10/sensor_value
#     print(
#         f"The resistance of the light sensor is: {resistance_sensor:.1f} KOhm")

#     klux = 325 * pow(resistance_sensor, -1.4) / 1000
#     board.displayShow(klux)
#     print(f"Illuminance is approximately {klux:.3f} Kilo lux")


# # We set the callback function so that any change of more than 50 units
# # in the sensor results in calling the supplied function "callback_ldr"
# board.set_pin_mode_analog_input(
#     LDR_PIN, callback=callback_ldr, differential=50)

# # infinite loop with a short (10 millisecond) pause to avoid overloading the CPU
# while True:
#     try:
#         time.sleep(0.01)
#     # if anyone presses <CTRL+C> break out of the loop
#     except KeyboardInterrupt:
#         break

# # clean up
# print("Shutting down...")
# board.shutdown()




# import time,sys
# from fhict_cb_01.custom_telemetrix import CustomTelemetrix

# DHTPIN = 12
# LDRPIN = 2
# BUTTON1PIN = 8

# humidity = 0
# temperature = 0
# brightness = 0
# display_mode = 0

# def LDRChanged(data):
#     global brightness
#     brightness = data[2]

# def Measure(data):
#     global humidity, temperature
#     humidity = data[4]
#     temperature = data[5]

# def setup():
#     global board
#     board = CustomTelemetrix()
#     board.displayOn()
#     board.set_pin_mode_dht(DHTPIN, dht_type=11, callback=Measure)
#     board.set_pin_mode_analog_input(LDRPIN, callback=LDRChanged, differential=10)
#     board.set_pin_mode_digital_input_pullup(BUTTON1PIN)

# def loop():
#     global display_mode
#     btn = board.digital_read(BUTTON1PIN)
#     if btn:
#         level = btn[0]
#         if level == 0:
#             display_mode += 1
#             if display_mode > 3:
#                 display_mode = 0

#     board.displayClear()

#     if display_mode == 0:
#         pass 
#     elif display_mode == 1:
#         board.displayShow(temperature)
#     elif display_mode == 2:
#         board.displayShow(humidity)
#     elif display_mode == 3:
#         board.displayShow(brightness)

#     time.sleep(1)

# setup()

# while True:
#     try:
#         loop()
#     except KeyboardInterrupt:
#         print('shutdown')
#         board.shutdown()
#         sys.exit(0)








# import time
# import sys
# from fhict_cb_01.custom_telemetrix import CustomTelemetrix

# board = CustomTelemetrix()

# # Constants
# DHTPIN = 12  # digital pin
# BUTTON1PIN = 8
# LDR_PIN = 2

# # Functions
# def setup():
#     board.displayOn()
#     board.set_pin_mode_dht(DHTPIN, dht_type=11)
#     board.set_pin_mode_digital_input_pullup(BUTTON1PIN)

# def brightness():
#     data = board.digital_read(LDR_PIN)
#     brightness2 = board.analog_read(LDR_PIN)
#     return brightness2

# def loop():
#     counter = 0  # Reset the counter inside the loop
#     while True:
#         data = board.digital_read(BUTTON1PIN)
#         level = data[0] if data else 1  # Set level to 1 if no data is available
#         if level == 0:
#             counter = (counter + 1) % 5  # Increment the counter, looping from 4 back to 0

#         if counter == 1:
#             humidity, temperature, timestamp = board.dht_read(DHTPIN)
#             board.displayShow(temperature)
#         elif counter == 2:
#             humidity, temperature, timestamp = board.dht_read(DHTPIN)
#             board.displayShow(humidity)
#         elif counter == 3:
#             brightness1 = brightness()
#             board.displayShow(brightness1)
#         elif counter == 4:
#             board.displayClear()

#         time.sleep(0.01)

# if __name__ == '__main__':
#     setup()
#     while True:
#         try:
#             loop()
#         except KeyboardInterrupt:
#             print('shutdown')
#             board.shutdown()



# import time,sys
# from fhict_cb_01.custom_telemetrix import CustomTelemetrix

# DHTPIN = 12
# LDRPIN = 2
# BUTTON1PIN = 8

# humidity = 0
# temperature = 0
# brightness = 0
# display_mode = 0

# def LDRChanged(data):
#     global brightness
#     brightness = data[2]

# def Measure(data):
#     global humidity, temperature
#     humidity = data[4]
#     temperature = data[5]

# def setup():
#     global board
#     board = CustomTelemetrix()
#     board.displayOn()
#     board.set_pin_mode_dht(DHTPIN, dht_type=11, callback=Measure)
#     board.set_pin_mode_analog_input(LDRPIN, callback=LDRChanged, differential=10)
#     board.set_pin_mode_digital_input_pullup(BUTTON1PIN)

# def loop():
#     global display_mode
#     btn = board.digital_read(BUTTON1PIN)
#     if btn:
#         level = btn[0]
#         if level == 0:
#             display_mode += 1
#             if display_mode > 3:
#                 display_mode = 0

#     board.displayClear()

#     if display_mode == 0:
#         pass 
#     elif display_mode == 1:
#         board.displayShow(temperature)
#     elif display_mode == 2:
#         board.displayShow(humidity)
#     elif display_mode == 3:
#         board.displayShow(brightness)

#     time.sleep(1)

# setup()

# while True:
#     try:
#         loop()
#     except KeyboardInterrupt:
#         print('shutdown')
#         board.shutdown()
#         sys.exit(0)




# import time
# import sys
# from fhict_cb_01.custom_telemetrix import CustomTelemetrix

# board = CustomTelemetrix()

# BUTTON1PIN = 8
# DHTPIN = 12
# LDR_PIN = 2

# OFF = 0
# temp = 1
# hum = 2
# br = 3

# current_state = OFF

# def setup():
#     board.displayOn()
#     board.set_pin_mode_digital_input_pullup(BUTTON1PIN)
#     board.set_pin_mode_dht(DHTPIN, dht_type=11)

# def temperature():
#     _, temperature, _ = board.dht_read(DHTPIN)
#     board.displayShow(temperature)

# def humidity():
#     _, humidity, _ = board.dht_read(DHTPIN)
#     board.displayShow(humidity)

# def brightness():
#     data = board.analog_read(LDR_PIN)
#     brightness2 = data
#     board.displayShow(brightness2)

# def cycle_display():
#     global current_state
#     if current_state == OFF:
#         current_state = temp
#     elif current_state == temp:
#         current_state = hum
#     elif current_state == hum:
#         current_state = br
#     elif current_state == br:
#         current_state = temp

# setup()
# while True:
#     try:
#         data = board.digital_read(BUTTON1PIN)
#         if data:
#             level = data[0]
#             if level == 0:
#                 cycle_display()
#                 if current_state == temp:
#                     temperature()
#                 elif current_state == hum:
#                     humidity()
#                 elif current_state == br:
#                     brightness()
#         time.sleep(0.1)
#     except KeyboardInterrupt:
#         print('shutdown')
#         board.shutdown()




# import time
# from fhict_cb_01.custom_telemetrix import CustomTelemetrix
# import sys


# BUTTON1PIN = 8
# DHTPIN = 12
# LDRPIN = 2
# board = CustomTelemetrix()

# humidity = 0
# temperature = 0
# brightness = 0
# display_mode = 0


# def setup():
#     global board
#     board.displayOn()
#     board.set_pin_mode_dht(DHTPIN, dht_type=11, callback=measurements)
#     board.set_pin_mode_analog_input(LDRPIN, callback=ldr_print, differential=10)
#     board.set_pin_mode_digital_input_pullup(BUTTON1PIN)

# def ldr_print(data):
#     global brightness
#     brightness = data[2]

# def measurements(data):
#     global humidity, temperature
#     humidity = data[4]
#     temperature = data[5]

# def loop():
#     global display_mode
#     data1 = board.digital_read(BUTTON1PIN)
#     if data1:
#         level = data1[0]
#         if level == 0:
#             display_mode = display_mode + 1
#             if display_mode > 3:
#                 display_mode = 1

#     board.displayClear()

#     if display_mode == 0:
#         pass 
#     elif display_mode == 1:
#         board.displayShow(temperature)
#     elif display_mode == 2:
#         board.displayShow(humidity)
#     elif display_mode == 3:
#         board.displayShow(brightness)

#     time.sleep(0.5)

# setup()

# while True:
#     try:
#         loop()
#     except KeyboardInterrupt:
#         print('shutdown')
#         board.shutdown()
#         sys.exit(0)