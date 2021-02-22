class Car:

    def __init__(self,name,color,speed,is_police = False):
        self.name = name 
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def start(self):
        print('Машина {} поехала'.format(self.name))

    def stop(self):
        print('Машина {} останолась'.format(self.name))
    
    def turn(self,direction):
        if direction == 0: s = 'Направо'
        elif direction == 1: s = 'Налево'
        else: s = 'Развернулась'
        print('Автомобиль {n} поехал {t}'.format(n = self.name,t = s))
    
    def show_speed(self):
        print('Скорость автомобиля {n} - {s} км\ч'.format(n = self.name, s = self.speed))

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print('Скорость автомобиля {n} составляет {s} - Превышение скорости!'\
                    .format(n = self.name, s = self.speed ))
        else:
            return print('Скорость автомобиля {n} составляет {s}'\
                    .format(n = self.name, s = self.speed ))

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print('Скорость автомобиля {n} составляет {s} - Превышение скорости!'\
                    .format(n = self.name, s = self.speed ))
        else:
            return print('Скорость автомобиля {n} составляет {s}'\
                    .format(n = self.name, s = self.speed ))

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police = True):
        Car.__init__(self,name, color, speed, is_police=is_police)

towncar = TownCar('taxi','yellow',70)
towncar.start()
towncar.show_speed()
towncar.turn(1)
towncar.stop()

policecar = PoliceCar('priora','blue',60)
policecar.turn(2)
policecar.stop()

workcar= WorkCar('kamaz','red',39)
workcar.start()
workcar.show_speed()

sportcar = SportCar('lotus','green',90)
sportcar.show_speed()
sportcar.turn(0)
