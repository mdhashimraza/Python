
age = int(input("Enter the age: "))
if(age >= 18):
    print("Can vote and apply for licence")
    print("Can drive and marraige")
elif(14 <= age < 18 ):
    print("Can not vote and apply for licence")
    print("Can not drive and marraige")
else: 
    print("Never vote and apply for licence")
    print("Never drive and marraige")
    print("Becaus he is very child")

print("See next sentance and follow the instraction:") 

light = input("Enter the traffic colour :")
if(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("Ready for go:")
elif(light == "green"):
    print("Let's go:")
else:
    print("It's invalid coloure. That is not traffic coloure.")

print("This exicution has been complated:")