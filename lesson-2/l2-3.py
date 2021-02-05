
seasons = {'Весна': [3,4,5],'Лето':[6,7,8],'Осень':[9,10,11],'Зима':[12,1,2]}
mes_str = str(input('Введите месяц в виде числа от 1 до 12: '))
if mes_str.isdigit() and int(mes_str) > 0 and int(mes_str) < 12:
    mes = int(mes_str)
    for k, v in seasons.items():
        if mes in v:
             print('{} месяц года - это {}'.format(mes,k))
else:
    ('Введенное значение не является числом от 1 до 12')