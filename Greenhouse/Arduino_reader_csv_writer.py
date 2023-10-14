import csv
import datetime
import random
import time
import requests
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix


board = CustomTelemetrix()
DHTPIN = 12
LDR_PIN = 2
humidity = 0
temperature = 0
brightness = 0

sample_list = []
listlen = 15


def setup():
   global board
   board.set_pin_mode_dht(DHTPIN, dht_type=11, callback=measurements)
   board.set_pin_mode_analog_input(LDR_PIN, callback=ldr_print, differential=10)

def date_printer():
   current_datetime = datetime.datetime.now()
   datetd = current_datetime.date()
   datenow = datetd.strftime("%m/%d/%Y")
   return datenow

def time_printer():
   current_datetime = datetime.datetime.now()
   time1 = current_datetime.time()
   ftime = time1.strftime("%H:%M:%S")
   return ftime

def ldr_print(data):
   global brightness
   brightness = data[2]

def measurements(data):
   global humidity, temperature
   humidity = data[4]
   temperature = data[5]


def loop():
    global sample_list
    while True:
        date1 = date_printer()
        ctime = time_printer()
        temp = temperature
        hum = humidity
        light = brightness
        sample_list.append((date1,ctime,temp,hum,light))
        sample_list = sample_list[-listlen:]
        for row in sample_list:
            response = requests.post('http://127.0.0.1:5000',json =row)
            if response.status_code != 200:
                print(response.text)
            else:
                print("OK")   
        time.sleep(1)
  
setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:
        print('shutdown')
        board.shutdown()