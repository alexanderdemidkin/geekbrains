lines = []
pr = 'y'
while pr != '':
    pr = str(input('Введите строку (для завершения ввода введите ""): '))
    lines.append(pr)
print('Ввод строк закончен')
with open("test.txt", "w") as file:
    for line in lines:
        file.write(line + '\n')
file.close()
