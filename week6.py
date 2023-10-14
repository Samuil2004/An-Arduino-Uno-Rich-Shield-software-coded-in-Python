from flask import Flask
from flask import render_template
from flask import request, redirect
import random
import time
import datetime

app = Flask(__name__)


# sample_list = [
#      ("14:00", "75"),
#      ("15:00", "45"),
#      ("16:00", "50"),
#      ("17:00", "90"),
#      ("18:00", "38")
# ]



@app.route("/")
def index():
    global sample_list
    return render_template('week6.html', sample = sample_list)



if __name__ == '__main__':
    app.run(debug= True)
