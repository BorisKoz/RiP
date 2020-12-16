# поведенческий паттерн проектирования
# наблюдатель
# предметная область: оповещение об изменнении температуры на метеостанции.

import numpy


class subscriber():
    def __init__(self, name):
        self.name = name


class meteostation():
    def __init__(self, name):
        self.name = name
        self.temperature = [0]
        self.subscribers = list()

    def subscribe(self, sub):
        self.subscribers.append(sub)
        return f"{sub.name} подписался"

    def notify(self):
        for sub in self.subscribers:
            print(
                f"Оповещаю {sub.name} об изменении температуры на {self.name} с {self.temperature[-2]} до {self.temperature[-1]}")
            return "оповещены подписчики"

    def measure(self):
        self.temperature.append(numpy.random.randint(-2, 2))
        if self.temperature[-2] != self.temperature[-1]:
            self.notify()
            return "оповещение запущено"
        return "оповещение не нужно"


def client_code():
    station1 = meteostation("станция 1")
    station2 = meteostation("станция 2")
    subscriber1 = subscriber("Ann")
    subscriber2 = subscriber("John")
    station1.subscribe(subscriber1)
    station2.subscribe(subscriber1)
    station2.subscribe(subscriber2)
    station1.measure()
    station1.measure()
    station2.measure()


if __name__ == "__main__":
    client_code()