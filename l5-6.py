a = {}
sym = ['(л)','(пр)','(лаб)','\n',' ']
with open('text6.txt','r') as file:
    for lines in file:
        subj_sum = 0
        it = []
        subj,val = lines.split(':')
        b = val.split('-')
        for el in b:
            for s in sym:
                el = el.replace(s,'')
            it.append(el)   
        for e in it:
            if e.isdigit():
                subj_sum = subj_sum + int(e)
        a[subj] = subj_sum
    print(a)
file.close()
