count_str = 0
count_sim_it = 0
with open("count.txt", "r") as file:
    for line in file:
        count_sim = 0
        count_str += 1
        for sim in line:
            count_sim += 1
            count_sim_it += 1
        print('Строка{st} содержит {sm} символов'.format(st = count_str,sm = count_sim))
    print('Всего строк: {st} в них {sm} символлов'.format(st = count_str, sm =  count_sim_it))
file.close()