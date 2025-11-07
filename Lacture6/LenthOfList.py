cities = ["Katihar","Patna","Delhi","Ghaziabaad","Mumbai"]
heroes = ["Hashim","Azhar","Imran","Kameel","Jamil","Arsh"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

def print_list(list):
    for item in list :
        print(item,end=" ")

print_list(heroes)
print_list(cities)


def cal_fact(n):
    fact = 1
    for i in range (1,n+1):
        fact *= i
    print(fact)


cal_fact(5)
cal_fact(7)
cal_fact(8)
cal_fact(9)

def converter(usd_val):
    inr_val = usd_val*86
    print(usd_val ,"USD = ", inr_val ,"INR")

converter(1)
converter(10)
converter(15)
converter(51)
converter(100)