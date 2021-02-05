
col_str = str(input('Вdедите количество элементов: '))
if col_str.isdigit():
    col = int(col_str)
    if col> 0:
        user_list = []
        for i in range(0,col):
            el = str(input('Вdедите следующий элемент  '))
            user_list.append(el)
        print('начальный список - {}'.format(user_list))
        it = col % 2
        max_el = col 
        if it == 1:
            max_el = col - 1
        for j in range(0,max_el,2):
            varb = user_list[j]
            user_list[j] = user_list[j+1]
            user_list[j+1] = varb

        print('измененный список - {}'.format(user_list))
        
