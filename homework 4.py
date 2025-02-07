class Engine:
    power = "Powerful Engine"
    _power = "Protected Engine"
    __power = "Private Engine"

    def __init__(self):
        self.status = "Stopped"
        self._status = "Idle"
        self.__status = "Hidden Status"

    def engine_info(self):
        print(self.power)
        print(self._power)
        print(self.__power)
        print(self.status)
        print(self._status)
        print(self.__status)

class Car(Engine):
    def car_info(self):
        print(self.power)
        print(self.status)
        print(self._power)
        print(self._status)
        print(self._Engine__power)
        print(self._Engine__status)

engine = Engine()
engine.engine_info()

car = Car()
car.car_info()