# fucntion defenation
def calc_sum(a,b):  # parameters
    sum = a+b
    print(sum)
    return sum

def calc_sum1(a,b):
    return a+b

sum = calc_sum1(15,45)  # fucntion call arguments
print(sum)

calc_sum(12,11)    # fucntion call arguments
calc_sum(12,10)
calc_sum(12,5)
calc_sum(45,85)


def print_hello():
    print("Hello")

print_hello()
print_hello()
print_hello()
print_hello()
output = print_hello()
print(output)  #None