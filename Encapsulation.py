class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self._color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self._color = value

    def get_color(self):
        return self._color
    

ford = Car(200, 'red')
honda = Car(250, 'blue')
audi = Car(300, 'black')

ford.set_speed(300)
print(ford.get_speed())
print(ford.get_color())
