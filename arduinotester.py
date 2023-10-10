import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix
from flask import Flask
from flask import render_template
from flask import request, redirect


board = CustomTelemetrix()
app = Flask(__name__)

# -----------
# Constants
# -----------
DHTPIN = 12  # digital pin
# -----------
# functions
# -----------
sample_list2 = []
max_samples2 = 15

def setup():
    board.displayOn()
    board.set_pin_mode_dht(DHTPIN, dht_type=11)


def loop():
    global sample_list2
    humidity, temperature, timestamp = board.dht_read(DHTPIN)
    print(humidity, temperature)
    board.displayShow(temperature)
    sample_list2.append((temperature,humidity))
    sample_list2 = sample_list2[-max_samples2:]


    # return temperature,humidity
    time.sleep(0.01) 
    return temperature,humidity
 # Give Firmata some time to handle protocol.

# @app.route(\'/post\_data\, methods = \[\'Post'\]'\)
@app.route('/')
def index():
    # global sample_list2
    loop()
    # temperature,humidity = loop()
    # temperature, _ = loop()
    # _, humidity = loop()
    # sample_list2.append((temperature,humidity))
    return render_template('subpointA.html', sample2 = sample_list2)

if __name__ == '__main__':
    sample_list2 = []
    # setup()
    app.run(debug= True)
setup()


# --------------
# main program
# --------------


# setup()
# while True:
#     try:
#         loop()
#     except KeyboardInterrupt:  # crtl+C
#         print('shutdown')
#         board.shutdown()
#         sys.exit(0)


# if __name__ == '__main__':
#     app.run(debug= True)

