nums = (1,4,9,16,25,36,49,64,81,100)
i = 0
while i < len(nums):
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1