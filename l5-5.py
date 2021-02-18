a = []
i = 'y'
sum = 0
while i == 'y':
    el = input('Введите число: ')
    if el.isdigit():
        a.append(el)
    i = input('Если хотите ввести еще элемент введите "y" :')
with open('text5.txt','w') as file:
    for elem in a:
        file.write(elem)
        file.write(' ')
file.close()
with open('text5.txt','r') as file_read:
    text = file_read.read()
    b = text.split()
    for dig in b:
        sum = sum + int(dig)
print('Сумма всех чисел файла text5.txt равна {}'.format(sum))