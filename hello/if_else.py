''''
cars=['Audi','Mercedes','bmw']
for car in cars:
    if car== 'bmw':
        print(car.upper()) #()are used for calling the upper method
    else:
        print(car.title())    

#inequality
order=['panner']
if order !='anchovies':
    print("Hold on")       

# ad operator
a=20
b=18

a >=21 and b>=21

# or operator
a=20
b=18

a >=21 or b>=21

#In operator to check if certain value is peresent in the list

a=['an','pan','man'] 
'pan' in a

# not in

banned=['anni','mary','halsey']
user=['justin']

if user not in banned:
    print("You can join")


#boolean true or false     


car='suabru'
print((car=='suabru'))

# simple if statement
age=70
if age >=18:
    print('You can vote')
else:
    print('you cant vote')    

#lets print your ticket using if else elif else block chain
print("Please enter your age☺️")
user=int(input())
if user <=10:
    print("Your are free for rides congo")
elif user == 20:
    print("your ticket is ₹ 500")
else:
    user >=21
    print("Your ticket is ₹ 1000")

##### if - elif chain
required=['mashroom','peproni','olive'] 
if 'mashroom' in required:
    print("Mashroom added")  
if 'pepromni' in required:
    print("Peproni added")  
if 'olive' in required:
    print("olive added")
print('terminate')    
'''

requestes=['c','b','s']
availables=['a','b','s']

for required in requestes:
    if required in availables:
        print("yes adding")
    else:
         print("not adding")
print("done")           