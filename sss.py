# word = "abbcc "
# list1 = list(word)
# count = {}
# counter = 0
# for letter in list1:
#     if letter in count:
#         counter = counter + count[letter]
#         count[letter] = count[letter] + 1
#     else:
#         count[letter] = 1

# counter = 1
# counter2 = 0
# list2 = list(count.values())
# list2.sort()
# list2.reverse()
# i = list2[0]
# if i != 1:
#     i2 = i-1
# else:
#     i2 = i
# for j in range(1, len(list2)):
#         if i2 == list2[j]:
#             counter = counter + 1
#             # print(i2)
#             # print(list2[j])
#             # print("true")
#         #     break
#         # else:
#             # print("false")
#         elif i2 - list2[j] == -1 or i2 - list2[j] == 1:
#             counter2 = counter2+1
#         if counter2 > 1:
#             print("False")

# print(counter)
# if counter == len(list2):
#     print("TRUE")

# else:
#     print("FALSE")

# class Counter():
#     word = "aaasssvvv"

#     def eee(self,word):
#         # word = "aaasssvvv"

#         counting = Counter(word)
#         if len(word) > 5:
#             print("DA")
#         else:
#             print("NE")
#         for i in word:
#             print(i)
#         # print(counting)

#     # print(eee())


# print(count)
# print(count.values())


# class Solution(object):
#     def equalFrequency(self, word):
#         counting=Counter(word)
#         for i in word:
#             counting[i]-=1
#             newlist=[]
#             for j in counting.values():
#                 if j:
#                     newlist.append(j)
#             if len(set(newlist))==1:
#                 return True
#             counting[i]+=1
#         return False
        
# arr = [0,2,3,4,5,2,1]
# highest = arr.index(max(arr))
# # print(highest)
# # counter = 0
# # print(arr[-1])
# r = True
# if len(arr) >= 3 and arr[0] != arr[highest] != arr[-1]:
#     for i in range(0,highest):
#         if arr[i] >= arr[i+1]:
#             r = False
#             exit()
#     for j in range(highest+1,len(arr)):
#         if arr[j-1] <= arr[j]:
#             r = False
#             exit()

#     print (r)
#     # if r == True:
#     #     print("T")
#     # else:
#     #     print("F")
# else:
#     print("F")


#     # beats 54.74%
#     # beats 28.78%

#     # beats 73.61%
#     # beats 62.54%

#     # beats 91.76%
#     # beats 62.54%

#     # beats 94.67%
#     # beats 28.78%





# s = "fly me to the eeeeee"
# # j = s.split()
# print(len(s.split()[-1]))
# # print(s.index(" "),-1)


l1 = [0]
l2 = [0]

l1.reverse()
l11 = [str(x) for x in l1]
l12 = "".join(l11)
l13 = int(l12)
print(l13)

l2.reverse()
l22 = [str(x) for x in l2]
l23 = "".join(l22)
l24 = int(l23)
print(l24)

l3 = l24 + l13
l333 = [int(x) for x in str(l3)]
# l31 = [str(x) for x in l3]
l32 = list(l333)
l32.reverse()
l31 = [str(x) for x in l32]
l33 = "".join(l31)
print(l33)