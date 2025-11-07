class Persion:
    name = "anonymous"

    # def changeName(self,name):
    #     self.__class__.name = name

    @classmethod
    def changeName(cls,name):
        cls.name = name


p1 = Persion()
p1.changeName("Md Hashim Raza")
print(p1.name)
print(Persion.name)