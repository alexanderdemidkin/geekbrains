import json
from os import close


firm_list = []
avg_dict = {}
with open('json7.json','w') as j:
    with open('text7.txt','r') as file:
        avg_prib = 0
        firm_dict = {}
        for lines in file:
            a= lines.split()
            prib = int(a[2]) - int(a[3])
            if prib > 0:
                avg_prib = avg_prib + prib
            firm_dict[a[0]] = prib
        firm_list.append(firm_dict)
        avg_dict['average_prifit'] = avg_prib
        firm_list.append(avg_dict)
    json.dump(firm_list,j,ensure_ascii=False,indent=4)
