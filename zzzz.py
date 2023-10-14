# import csv
# import datetime
# import random
# from flask import Flask, render_template

# app = Flask(__name__)

# # Define the CSV file and column headers
# csv_file = "subpointB.csv"
# columns = ["Date", "Time", "Temperature (°C)"]

# def get_current_time():
#     current_datetime = datetime.datetime.now()
#     date = current_datetime.strftime("%m/%d/%Y")
#     time = current_datetime.strftime("%H:%M:%S")
#     return date, time

# def generate_random_temperature():
#     return round(random.uniform(5, 45), 2)

# @app.route('/')
# def index():
#     # Generate random temperature and get the current date and time
#     date, time = get_current_time()
#     temperature = generate_random_temperature()

#     # Append the data to the CSV file
#     with open(csv_file, mode='a', newline='') as csvfile:
#         csv_writer = csv.writer(csvfile)
#         csv_writer.writerow([date, time, temperature])

#     # Read the CSV data
#     temperature_data = []
#     with open(csv_file, mode='r') as csvfile:
#         csv_reader = csv.reader(csvfile)
#         next(csv_reader)  # Skip the header row
#         for row in csv_reader:
#             temperature_data.append(row)

#     return render_template('brandnew..html', temperature_data=temperature_data)

# if __name__ == '__main__':
#     app.run(debug=True)



import csv
import datetime
import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Define the CSV file and column headers
csv_file = "subpointB.csv"
columns = ["Date", "Time", "Temperature (°C)"]

def get_current_time():
    current_datetime = datetime.datetime.now()
    date = current_datetime.strftime("%m/%d/%Y")
    time = current_datetime.strftime("%H:%M:%S")
    return date, time

def generate_random_temperature():
    return round(random.uniform(5, 45), 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Generate random temperature and get the current date and time
        date, time = get_current_time()
        temperature = generate_random_temperature()

        # Append the data to the CSV file
        with open(csv_file, mode='a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([date, time, temperature])

    # Read the CSV data
    temperature_data = []
    with open(csv_file, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            temperature_data.append(row)

    return render_template('brandnew..html', temperature_data=temperature_data)

if __name__ == '__main__':
    app.run(debug=True)
