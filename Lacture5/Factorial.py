
n = int(input("Enter any number : "))
sum = 1
# for i in range(n,0,-1):
#     sum = sum*i
# print(sum)
 
for i in range(1,n+1):
   sum *= i
print("Factorial = ",sum)