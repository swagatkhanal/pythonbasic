#creating empty dictionary 
d={}
print(d)
#adding element 
d[0]="hello"
print(d)
d[1]=("hi","swagat")
print(d)
d["name"]="swagat"
print(d)
d["name"]={"first":"swagat","last":"khanal"}
print(d)
#accesing elements
print(d["name"])
print(d[0])
print(d.get(1))
print(d["name"]["first"])

#deleting elements
d.pop(0)
print(d)

d.popitem()   #delets last item
print(d)




