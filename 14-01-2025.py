#
colors={1:'Red',2:'Blue',3:'Yellow'}
print(colors)
print(len(colors))
print(colors[1])
print(colors.get(5,'none existen key'))
if 3 in colors:
    print(colors[3])
else:
    print('none existen key')
#
person_info={}
person_info["Name"]='Ali'
person_info["Age"]=21
person_info["E-mail"]='ali@gmail.com'
person_info["Address"]='Dhaka'
print(person_info)
person_info.update({'Name':'Ali',"Age":21,"E-mail":'ali@gmail.com',"Address":'Dhaka'})
print(person_info)
del person_info["E-mail"]
print(person_info)
#
person_info={}
person_info["Name"]='Ali'
person_info["Age"]=21
person_info["E-mail"]='ali@gmail.com'
person_info["Address"]='Dhaka'

for k,v in person_info.items():
    print(k,end=':')
    print(v)

for k in person_info.keys():
    print(k)
for k in person_info.values():
    print(k)
for k in person_info:
    print(k)