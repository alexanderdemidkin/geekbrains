a = {"One":"Один","Two":"Два","Three":"Три","Four":"Четыре"}
with open("input4.txt", "r") as file:
    text = file.read()
    for key,value in a.items(): 
        text = text.replace(key,value)
with open("output4.txt","w") as file_out:
    file_out.write(text)