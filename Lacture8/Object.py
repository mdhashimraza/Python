class student:
      # default condtructors
    def __init__(self):
        pass

# parameterized constructors
    def __init__(self,name,marks):
      self.name = name
      self.marks = marks
      print("adding new student in database... ")
   

s1 = student("Fahim",97)
print(s1)
print(s1.name,s1.marks)
s2 = student("Hasmat",88)

print(s2.name,s2.marks)


# class Car:
#     color = "Blue"
#     brand = "mercedes"

# Car1 = Car()
# print(Car1.color)
# print(Car1.brand)