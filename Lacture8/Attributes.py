class student:
    college_name = "AKTU College"
    name = "my name is Hashim"   # class Attr

    def __init__(self,name,marks):
      self.name = name        # Obj   Attr > class Attr
      self.marks = marks
    
    def welcom(self):
       print("welcom student, ",self.name)

    def get_marks(self):
       return self.marks
   

s1 = student("Fahim",97)
s1.welcom()
print(s1.get_marks())

