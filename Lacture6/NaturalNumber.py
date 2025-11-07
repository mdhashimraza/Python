

def cal_sun(n):
    if(n==0):
        return 0
    return cal_sun(n-1) +n

sum = cal_sun(100)
print(sum)