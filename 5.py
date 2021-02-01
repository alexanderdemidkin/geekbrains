proceeds_str=input('Введите сумму выручки: ')
if proceeds_str.isdigit():
    costs_str=input('Введите сумму издержек: ')
    if costs_str.isdigit():
        proceeds = int(proceeds_str)
        costs = int(costs_str)
        if proceeds > costs :
            print('Прибыль: выручка больше издержек')
            profit = proceeds - costs
            rent = profit/proceeds
            print('Рентабельность равна:' + str(rent))
            staff_str = input('Введите количество сотрудников: ')
            if staff_str.isdigit():
                staff = int(staff_str)
                if staff != 0:
                    profit_on_men = profit/staff
                    print('Прибыль на человека равна: '+ str(profit_on_men))
                else:
                    print('Введено 0 коливчество сотрудников')    

        elif proceeds == costs :
            print('Выручка равна издержкам')
        else:
            print('Убыток: выручка меньше издержек')
    else:
        print('Сумма издержек не число')
else:
    print('Сумма выручки не число')