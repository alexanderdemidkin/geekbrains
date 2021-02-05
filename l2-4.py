
inputstring = input('Введите строку: ')
wordlist = inputstring.split(' ')
i = 1
for el in wordlist:
    if len(el) > 10:
        el = el[0:10]
    print(i,el)
    i = i + 1 

