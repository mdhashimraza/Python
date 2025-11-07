# recursive fucntion
def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)
    print("End")

show(5)


# recursion for factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
print(fact(7))