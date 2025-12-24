course='swagat kumar khanal'  
print(course.upper())          #for uppercase 
print(course.lower())          # lower case 
print(course.find('kumar'))    #find 
print(course.find('g'))
print(course.replace('w','z'))    # replace the character that you want 
print(len(course ))
print(course.index('k'))

x=course.split(" ")    #creates a list 
print(x)
print(course.rpartition(" kumar "))

hello=" good morning"

conc=course  +  hello     #concatenation
print(conc)
