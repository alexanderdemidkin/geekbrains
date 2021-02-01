first_day = input('Введите результат 1 дня: ')
result_str = input('Введите итоговый результат: ')
firstday = float(first_day)
result = float(result_str)
if result < firstday:
    print(Невозможно достичь - итоговый результат меньше результата первого дня)
else:
    day = 1
    while firstday <= result :
        firstday += firstday/10
        day+=1
    print('Спортсмен достигнет результата ' + result_str + ' за ' + str(day) + ' дней')

        