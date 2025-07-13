# Exercise 1
my_list=["Hello","winter","Cold","Fever"]
for i in my_list:
  print(i, end=" ")

# Exercise 2
my_list=["Hello","winter","Cold","Fever"]
for i in my_list:
  if len(i)>4:
    print(i, end=" ")

# Exercise 3
my_list=["Hello","winter","Cold","Feve"]
for i in range(len(my_list)):
    if i%2==1:
        if len(my_list[i])>4:
            print(my_list[i])

# Exercise 4
my_list = [10,20,35,30,40]
sum=0
for i in my_list:
  if i%5==0 and i%10==0:
    sum=sum+i
print(sum)

# Exercise 5
my_list = ["Hello","Morning", "Lazy", "Hello"]
search_string = input("Enter a string you want to search: ")
replace_string = input("Enter a string you want to replace: ")
for i in range(len(my_list)):
  if my_list[i]==search_string:
    my_list[i]=replace_string
print(my_list)

# Exercise 6
num_list=[10,5,35,70,45]
for i in num_list:
  if i%2==0:
    print(i)
    break
print(i)

# Exercise 7
num_list=[10,5,35,70,45]
for i in num_list:
  if i%2==0:
    continue
    print(i)
  print(i)
print(i)

# Exercise 8
counter = 0
while counter <=10:
  print(counter)
  counter+=1

# Exercise 9
counter = 10
while counter>=1:
  print(counter)
  counter=counter-1

# Exercise 10
while True:
  num = int(input("Enter a digit: "))
  if num==5:
    break
  else:
    print('please enter 5 to exit the loop!')

# Exercise 11
num = ["Hello","Hi","World"]
index=0
while index<len(num):
  print(num[index])
  index+=1 

# Exercise 12
num = [1,2,3,4,5]
index = 0
even_sum=[]
odd_sum=[]
while index<len(num):
  if index%2==0:
    even_sum.append(index)
  else:
    odd_sum.append(index)
  index+=1
print(sum(even_sum))
print(sum(odd_sum))