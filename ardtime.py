import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix
from flask import Flask
from flask import render_template
from flask import request, redirect
import random
import datetime


board = CustomTelemetrix()
app = Flask(__name__)


DHTPIN = 12  

sample_list2 = []
max_samples2 = 15
sample_list = []
max_samples = 20

def setup():
    board.displayOn()
    board.set_pin_mode_dht(DHTPIN, dht_type=11)


def loop():
    global sample_list
    humidity, temperature, timestamp = board.dht_read(DHTPIN)
    print(humidity, temperature)
    board.displayShow(temperature)
    sample_list.append((temperature,humidity))
    sample_list = sample_list[-max_samples:]
    time.sleep(0.01) 
    return temperature,humidity


def current_time():
    current_time = datetime.datetime.now()
    ftime = current_time.strftime("%m/%d/%Y, %H:%M:%S")
    return ftime

def light_level_measurement():
    return round(random.uniform(0,1000),2)


@app.route('/')
def index():
    global sample_list
    time_now = current_time()
    light_level = light_level_measurement()
    sample_list.append((time_now,light_level))
    sample_list = sample_list[-max_samples:]
    loop()


    return render_template('subpointA.html', sample = sample_list)

if __name__ == '__main__':
    sample_list2 = []
    # setup()
    app.run(debug= True)
setup()


