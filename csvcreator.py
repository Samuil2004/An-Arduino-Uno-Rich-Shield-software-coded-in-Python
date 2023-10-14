import csv
import datetime
import random
import time
import requests

columns = ["Date" '\t''\t' "Time" '\t''\t'  "Temperature in °C"]
sample_list = []
listlen = 15


csv_file = "test.csv"


def time_printer():
   current_datetime = datetime.datetime.now()
   time1 = current_datetime.time()
   ftime = time1.strftime("%H:%M:%S")
   return ftime


def date_printer():
   current_datetime = datetime.datetime.now()
   datetd = current_datetime.date()
   datenow = datetd.strftime("%m/%d/%Y")
   return datenow


def temperature_printer():
   temperature = random.randint(5,45)
   return temperature

while True:
   ctime = time_printer()
   temp = temperature_printer()
   date1 = date_printer()
   sample_list.append((date1,ctime,temp))
   sample_list = sample_list[-listlen:]
   with open(csv_file, mode ='w', newline = '') as csvfile:
       csv_writer = csv.writer(csvfile, delimiter='\t')
       csv_writer.writerow(columns)
    #    response = requests.post('http://127.0.0.1:5000/',json =)

       for row in sample_list:
           csv_writer.writerow(row)
           response = requests.post('http://127.0.0.1:5000',json =row)
      


   time.sleep(1)

