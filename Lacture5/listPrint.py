# nums = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(nums) :
#     print(nums[i])
#     i += 1

# students = ["Hashim","Fahim","Salman","Naseem"]
# j = 0
# while j < len(students) :
#     print(students[j])
#     j += 1
nums = [1,4,9,16,25,36,49,64,81,100]
x = 49
i = 0
while i < len(nums) :
    if(nums[i] == x):
      print("Element found at index : ",i)
    else:
      print("finding element again : ")
    i += 1