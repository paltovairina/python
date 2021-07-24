class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def go(self):
        return f"Автомобиль {self.name} поехал"

    def stop(self):
        return f"Автомобиль {self.name} остановился"

    def turn(self, direction):
        return f"Автомобиль {self.name} повернул {direction}"

    def show_speed(self,speed):
        return self.speed


class TownCar(Car):

    color = "White"
    name = "Volkswagen"
    is_police = False

    def show_speed(self,speed):
        self.speed = speed
        if speed > 60:
            return f"Вы превысили скорость! Ваша скорость - {self.speed} км/ч"


class SportCar(Car):
    speed = 200
    color = "Pink"
    name = "Bugatti"
    is_police = False


class WorkCar(Car):

    color = "Yellow"
    name = "Volvo"
    is_police = False

    def show_speed(self,speed):
        self.speed = speed
        if speed > 40:
            return f"Вы превысили скорость!Ваша скорость - {self.speed} км/ч"


class PoliceCar(Car):
    speed = 80
    color = "White&Blue"
    name = "Toyota"
    is_police = True


town_car = TownCar()
sport_car = SportCar()
work_car = WorkCar()
police_car = PoliceCar()
print(town_car.name)
print(town_car.show_speed(80))
print(work_car.turn("влево"))
print(police_car.go())

