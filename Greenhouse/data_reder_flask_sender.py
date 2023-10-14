# import csv
# import datetime
# import random
# import time
# import requests

# csv_file = "data.csv"

# while True:
#     data_list = []

#     with open(csv_file, mode='r') as csvfile:
#         csv_reader = csv.reader(csvfile, delimiter='\t')
#         headers = next(csv_reader, None)
#         for row in csv_reader:
#             data_list.append(row)
#             response = requests.post('http://127.0.0.1:5000',json =row)
#             if response.status_code != 200:
#                 print(response.text)
#             else:
#                 print("OK")


#     for row in data_list:
#         print(row)

#     time.sleep(1)
