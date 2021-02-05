goods = []
tpl = tuple()
dic_param = dict()
name_list = []
cost_list= []
kl_list = []
ed_list = []
col = str(input('Введите количество товаров: '))
if col.isdigit(): 
   
    if  int(col) > 0:
        
        for i in range (0,int(col)):
            name = input('Введите название товара: ')
            cost = input('Введите цену товара: ')
            kl = input('Введите количесво товара: ')
            ed = input('Введите ед. изменения товара: ')
            dic_param = {'Название':name, 'цена':cost, 'кол-во':kl, 'ед.изм':ed}
            name_list.append(dic_param['Название'])
            cost_list.append(dic_param['цена'])
            kl_list.append(dic_param['кол-во'])
            name_list.append(dic_param['ед.изм'])
            tpl1 = (i+1,dic_param)
            goods.append(tpl1)
        goods_dic = {'Название':name_list,'цена':cost_list,'кол-во':kl_list,'ед.изм':ed_list}
        for a in goods:
            print(a)
        for keys,values in goods_dic.items():
            print(keys)
            print(values) 
           
                
        
    else:
        print('Введеное число меньше 1')
else:
    print('Введено неверное количество товара')