class Vehicle:
    licenseCode = ""
    SerialCode = ""
    def TurnOnAircon(self):
        print("Turn on : Airconditioner")

class Car(Vehicle):
    pass
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

car1 = Car
car1.TurnOnAircon(Vehicle)

pickup1 = PickUp
pickup1.TurnOnAircon(Vehicle)

van1 = Van
van1.TurnOnAircon(Vehicle)

estatecar1 = EstateCar
estatecar1.TurnOnAircon(Vehicle)
