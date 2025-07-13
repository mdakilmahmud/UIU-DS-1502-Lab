# Exercise 1
f=open('number.txt','r')
file_content=f.readlines()
f.close()
even=[]
odd=[]
for i in file_content:
  i=i.strip()
  i=int(i)
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)
print("Even List:",even)
print("Odd List:",odd)

# Exercise 2
f=open('number.txt','r')
file_content=f.readlines()
f.close()
number_list=[]
for i in  file_content:
  number_list.append(int(i.strip()))
print("Max_value",max(number_list))
print("Min_value",min(number_list))
print("Avg value",sum(number_list)/len(number_list))

# Exercise 3
f=open("Person_info.txt",'r')
file_lines=f.readlines()
f.close()
data_dict={}
for line in file_lines:
  name,age=line.split()
  data_dict[name]=age
print(data_dict)
strin=str(data_dict)
f1=open("output.txt",'w')
f1.write(strin)
f1.close()

# Exercise 4
f1=open('input.txt','r')
file_lines=f1.readlines()
f1.close()
student_dict={}
for line in file_lines:
  name,num1,num2,num3=line.split()
  student_dict[name]=[num1,num2,num3]
print(student_dict)