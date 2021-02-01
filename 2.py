sc = input('Введите количество секунд: ')
if sc.isdigit():
   mn = int(sc) // 60 
   sc = int(sc) - (60 * mn)
   hr = mn // 60
   mn = mn - (60 * hr) 
   print(sc)
   print(mn)
   print(hr)
   print(str(hr)+':'+str(mn)+':'+str(sc))  
else:
    print('Введено не количество секунд')
