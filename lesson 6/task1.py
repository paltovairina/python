import time


class TrafficLight:
    __color = ["Красный", "Жёлтый", "Зелёный"]

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(2)
            elif i == 2:
                time.sleep(7)
            i += 1


t = TrafficLight()
t.running()
