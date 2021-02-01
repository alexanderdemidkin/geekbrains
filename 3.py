strnum = input('Введите число: ')
if strnum.isdigit():
    num1 = int(strnum)
    num2 = int(strnum * 2)
    num3 = int(strnum * 3)
    it = num1 + num2 + num3 
    print('Сумма '+str(num1)+'+'+str(num2)+'+'+str(num3)+' равна '+str(it) )

else:
    print('Введено не число')