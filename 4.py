strnum = input('Введите целое число: ')
if strnum.isdigit():
    ln=len(strnum)
    i = 0
    mx = 0 
    while i < ln :
        a = int(strnum[i])
        if a > mx :
            mx = a
        i+=1
    print("Максимальная цифра числа "+str(strnum)+" равна: "+ str(mx))
         