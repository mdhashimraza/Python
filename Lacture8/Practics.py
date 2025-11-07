class student:
    def __init__(self,name,marks):
      self.name = name
      self.marks = marks

    def get_avg(self):
       sum = 0
       for val in self.marks:
          sum += val
       print("Hi", self.name ,"your avg score is :", sum / len(self.marks))

s1 = student("Hafsha Quraisi", [99,98,97])
s1.get_avg()
s1.name = "Hasmat"
s1.get_avg()
