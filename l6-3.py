class Worker:
    def __init__(self,name,surname,position,wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return print('Полное имя: {n} {s} '.format(n = self.name,s = self.surname))

    def get_full_profit(self):
        return print('Доход: {} '.format(sum(self._income.values())))

a = Position('Alex','Dupin','developer',1000,300)
a.get_full_name()
print(a.position)
a.get_full_profit()




    