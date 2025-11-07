class car:
    color = "Red"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped. ")


class ToyotaCar(car):
    def __init__(self,name):
        self.name = name


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("TATA")

print(car1.start())
print(car1.stop())
print(car2.name)
print(car2.color)