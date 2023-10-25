# import csv
# import datetime
# import random 
# import time
# from flask import Flask, render_template, request, redirect,jsonify



# app = Flask(__name__)
# temperature_data = []
# average_temperature = []

# @app.route('/', methods=['GET','POST'])
# def index():
#     global temperature_data,average_temperature

#     if request.method == 'POST':
#         row = request.get_json()
#         temperature_data.append(row)
#         temperature_data = temperature_data[-15:]
#         average_temperature.append(row[2])


#     avrgtemp = round(sum(average_temperature)/len(average_temperature),2)

#     return render_template('brandnew..html', temperature_data=temperature_data, average = avrgtemp )

# if __name__ == '__main__':
#     app.run(debug=True)


# height = [1,1]
# left = 0
# right = len(height) - 1
# ma = 0

# while left < right:
#     h1 = height[left]
#     h2 = height[right]
#     width = right - left
#     ca = min(h1,h2)*width
#     ma = max(ma,ca)

#     if h1<h2:
#         left = left + 1
#     else:
#         right = right-1 

# print(ma)

# for idx, num in enumerate(list):
#     for idx2, num2 in enumerate(list[idx:], start = idx):
#         if num >= num2:
#             t = (idx2-idx)*num2
#             if t >= sum:
#                 sum = t
#         if num <= num2:
#             t = (idx2-idx)*num
#             if t >= sum:
#                 sum = t

# print(sum)



# # nums = [3,2,1,5,6,4]
# nums = [3,2,3,1,2,4,5,5,6]
# k = 4
# sortednums = sorted(nums, reverse = True)
# print(sortednums[k-1])

# nums1 = [0,1,7,11]
# nums2 = [9,2,4,6]
# k = 3

# list = []
# sum = nums1[0]+nums2[0]
# # for idx, num in enumerate(nums1):
# #     # sum = 0
# #     # sum = nums1[0]+nums2[0]
# #     for idx2, num2 in enumerate(nums2):
# #         if num + num2 <= sum:
# #             sum = num + num2
# #             list.append(num)
# #             list.append(num2)
# #     # print(num)
# #     # print(num2)
# #     print(sum)

# # for i in range(k):
# #     print(list[i])

# for i in range(len(nums1)):
#     for j in range(len(nums2)):
#         if nums1[i] + nums2[j] <= sum:
#             sum = nums1[i] + nums2[j]
#             list.append(nums1[i])
#             list.append(nums2[j])
#     print(sum)
# # print(list)


# from collections import Counter
# ransomNote = "fffbfg"
# magazine = "effjfggbffjdgbjjhhdegh"

# list1 = list(ransomNote)
# list2 = list(magazine)

# counter1 = Counter(list1)
# counter2 = Counter(list2)

# if counter1 <= counter2:
#     print("T")
# else:
#     print("F")

n = 13
list1 = []

for i in range(1,n+1):
    list1.append(str(i))
list1.sort()
print(list1)
l2=[int(i) for i in list1]
print(l2)

# for i in range (1,n+1):
#     list1.append(i)

# for num in list1:
#     numm = str(num)
#     for num2 in list1[1:]:
#         nummm = str(num2)
#         if numm in nummm and num < num2:
#             list1.insert(list1.index(num)+1,num2)


# print(list1)