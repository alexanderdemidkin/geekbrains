work ={}
zp_sum = 0
workers_count = 0
with open("workers.txt", "r") as file:
    for line in file:
        key,*value = line.split()
        work[key] = value
    for k,v in work.items():
        for el in v :
            if int(el) <= 20000:
                print(k,el)
            workers_count += 1
            zp_sum = zp_sum + int(el)
            itog = zp_sum/workers_count
    print('Средняя зарплата равна: {}'.format(itog))
        