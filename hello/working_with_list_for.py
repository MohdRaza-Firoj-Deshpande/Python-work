"""""
animals=['cat','dog','elephant']
for animal in animals:
    print(animal)

# Range
for i in range(1,5):
    print(i)    

#Making List out o range
li=list(range(1,4))
print(li)  

li=[]
for value in range(1,5):
    squares=value**2
    li.append(squares)
    print(li)

"""
li=[value**2 for value in range(2,30)]
print(li)   

#slicing a list
Name=['raza','rani','seema','chanda','bushra','abba','ammi']
print(Name[0:3])

Name=['raza','rani','seema','chanda','bushra','abba','ammi']
print(Name[:4])

Name=['raza','rani','seema','chanda','bushra','abba','ammi']
print(Name[0:])