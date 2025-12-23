lst=[1,2,3,4]
print(type(lst))

tple=tuple(lst)
print(tple)


#nesting tuples in list 
lst1=[(1,2,3,4),(5,6,7,8)]
print(lst1)

lst1.append(("swagat","school"))
print(lst1)

#nesting list in tuple
tpl=([1,2,3,4],[12,34,56])
print(tpl)

tpl[0].append('z')
print(tpl)
tpl[0].remove('z')
print(tpl)