d={"Eno":123,"Ename":"abc"}
print(d)
print(d["Eno"])
print(d.get("Ename"))
d["age"]=22
print(d)
d.pop("Eno")
print(d)
d.popitem()
print(d)
for key in d:
    print(d)
for value in d.values():
    print(value)
for key,value in d.items():
    print(key,":",value)
d.clear()
print(d)



    
