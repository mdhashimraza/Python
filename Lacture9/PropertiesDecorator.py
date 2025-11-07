class student:
    def __init__(self,phy,che,math):
        self.phy = phy
        self.che = che
        self.math = math
        #self.percentage = str((self.phy+self.che+self.math)/3)+"%"
    
    # def calcPercentage(self):
    #     self.percentage = str((self.phy+self.che+self.math)/3)+"%"


    @property
    def percentage(self):
       return str((self.phy+self.che+self.math)/3)+"%"


stu1 = student(98,99,97)
print(stu1.percentage)
stu1.phy = 86
print(stu1.phy)
print(stu1.percentage)

