#types of list and some of their operation 

num =[1,2,3,4]
print(num)
print()         
letter=['a','b','c','d']
print(letter)
print(letter[::2])
print()

stg=["get","certified","hand"]
print(stg)
print(stg[::-1])    #reverse
print()

mix=[1,6,"mix"]
print(mix)
print(mix[2])
print(mix[1:2])
print()

mat=[[1,2],['a','b']]
print(mat)
print()
z=[0]*100
print(z)

conc=letter + stg     #adding strings 
print(conc)
print()


var=list("hey there")
print(var)
print()
one,*other=num  # * signifies that every element that has not been put into previous varible is put into the another varibale named other 

print(one)
print(other)
print()
num.append(6)  # add 6 
print(num)

 #extending list num with list stg 
num.extend(stg)
print(num)


#inserting into list 
num.insert(5,"swagat")
print(num)

#removing 
num.remove("swagat")
print(num)

#sorting 
var1=['b','c','f','a','g','h']
var1.sort()
print(var1)
