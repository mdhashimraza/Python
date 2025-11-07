class car:
    color = "Red"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped. ")


class ToyotaCar(car):
    def __init__(self,brand):
        self.brand = brand

class fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type






car1 = fortuner("deisel")

car1.start()