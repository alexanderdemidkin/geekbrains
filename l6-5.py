class Stationery:
    def __init__(self,title):
        self.title = title
    
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручки {}'.format(self.title))


class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандаша {}'.format(self.title))


class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркера {}'.format(self.title))
stat = Stationery('st')
stat.draw() 
pen = Pen('bic')
pen.draw()
pencil = Pencil('constuctor')
pencil.draw()
handle = Handle('beifa')
handle.draw()
