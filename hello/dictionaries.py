'''
A={'Name':'Raza','Class':'10','Sec':'A'}
print(A)
A['year']=2016
print(A)

alien_0={}
alien_0['Ramu']=10
alien_0['shamu']=23
alien_0['gamu']=23
alien_0['mamu']=23
print(alien_0)
#changed value
alien_0['Ramu']=100

print(alien_0)


#if eleif else in dictonary
alien_0={'alienx_x':10,'alien_speed':'med','alienx__y':'20'}
if alien_0['alienx_x']==10:
    updtaed_alien_x=20
new_aline_x=alien_0['alienx_x']+updtaed_alien_x
print(new_aline_x)
'''
## del
#alien_0={'alienx_x':10,'alien_speed':'med','alienx__y':'20'}
#del alien_0['alienx_x']
#print (alien_0)
'''
classdic = {'Name':'Raza','Class':'10','Div':'A','Rollno':'32'} 
print(classdic['Name'])
del(classdic['Name'])
print(classdic)


schooldic={'School_name':'SAS','college_name':'mit','college_state':'Maha'}
'''
#Get is used to give a message or value that is not present in the dictonary so you will 
# not get an error instead you will get a message

# classdic = {'Name':'Raza','Class':'10','Div':'A','Rollno':'32'}
# point_value=classdic.get('C','No such value present')
# print(point_value)


#$$$$$ Looping through thr dictonary for loop and print each value and key 
# using items
'''
schooldic={'School_name':'SAS','college_name':'mit','college_state':'Maha'}


for key , value in schooldic.items():
        print({key})
        print({value})

'''
#schooldic={'School_name':'SAS','college_name':'mit','college_state':'Maha'}


#for name  in schooldic.keys():
    #    print(name)
       
#schooldic={'School_name':'SAS','college_name':'mit','college_state':'Maha'}


#for name  in schooldic.values():
 #       print(name)

lst=[]
for new in range(3):
    data={'this':'is'}
    lst.append(new)
print(lst)






