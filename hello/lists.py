#List
biycycle=['RE','Honda','Suzuki']
print(biycycle)

#Acsessing Elements in a List
biycycle=['RE','Honda','Suzuki']
print(biycycle[0].title())

#Modifiying Elements in a list
biycycle[0]='bus'
print(biycycle)

#Append - Add Element to the last
biycycle=['RE','Honda','Suzuki']
biycycle.append('CAR')
biycycle.append('Helicopter')
biycycle.append('Train')
print(biycycle)
#insert- Add element according to the convinence
biycycle.insert(5,'Train')

#Del Elements from element the only command where the function came before the variable without using point
del biycycle[0]
print(biycycle)

# Get elements when they are also not present POP
biycycle=['RE','Honda','Suzuki']
biycycle.pop()
print("pop",biycycle)

biycycle=['RE','Honda','Suzuki']
biycycle.pop(0)
print("pop0",biycycle)

biycycle=['RE','Honda','Suzuki']
biycycle.remove('RE')
print(biycycle)

#List sorting
biycycle=['RE','Honda','Suzuki']
biycycle.sort()
print("sort",biycycle)

#List sorting revese = TRUE
biycycle=['RE','Honda','Suzuki']
biycycle.sort(reverse=True)
print("sort",biycycle)

#List sorting revese = TRUE Here syntax is diffrent
biycycle=['RE','Honda','Suzuki']
print(sorted(biycycle))

# Print In revese 
biycycle=['RE','Honda','Suzuki']
biycycle.reverse()
print(biycycle)

# Length of the list  Here syntax is diffrent
biycycle=['RE','Honda','Suzuki']
len(biycycle)
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)


