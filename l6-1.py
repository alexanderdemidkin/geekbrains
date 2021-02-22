import time
class traficlight:
    __color = 'red'

    def runing(self,color):
       
        while True:
            if color == 'red':
                print('Горит красный')
                time.sleep(7)
                color = 'yellow'
            elif color == 'yellow':
                print('Горит желтый')
                time.sleep(2)
                color = 'green'
            elif color == 'green':
                print('Горит зеленый')
                time.sleep(6)
                color = 'red'
            else:
                print('Некоректный цвет')

a = traficlight()
a.__color = 'red'
a.runing(a.__color)