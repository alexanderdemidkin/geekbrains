my_list = [7, 5, 3, 3, 2]
st = str(input('введите число:'))
if st.isdigit():
    el = int(st)
    my_list.append(el)
    my_list.sort()
    my_list.reverse()
    print(my_list)

else:
    print('Вы ввели не число')