# if the function didn't return anything that is called VOID
# Exercise 1
def addition1(a,b):
  result=a+b
  print(f'The sum of {a} and {b} is {result}')

def addition2(a,b):
  result=a+b
  return result

def addition3():
  a=int(input('Enter the first integer: '))
  b=int(input('Enter the second integer: '))
  result=a+b
  print(f'The sum of {a} and {b} is {result}')

x=int(input('Enter first integer: '))
y=int(input('Enter the second integer: '))
addition1(x,y)
print(f"The sum of {x} and {y} is {addition2(x,y)}")
total=addition2({x,y})
print(f'The sum is {total}')
addition3()

# Exercise 2
s=0
def faCtorial(x,y):
  fac=x
  for i in range(x,y+1):
    fac*=i
    addition(fac)

def addition(fac):
  global s
  s+=fac

for i in range(x,y+1):
  faCtorial(i)
x=int(input('Start: '))
y=int(input('End: '))
print(f'The Sum of {x} and {y} is {s}')

# Exercise 3
def infoStudent(name,cgpa=0.0):
  print(f'Name={name}, cgpa={cgpa}')

infoStudent('Tanim')
infoStudent('Tanim',3.5)
infoStudent('Ayesha')

# Exercise 4
def infoStudent(name,cgpa):
  print(f'Name = {name}, Cgpa = {cgpa}')
infoStudent(name='Foysal',cgpa=4.0)

# Exercise 5
x=5 #global variable
y=10
def fun1(): 
  # total-local variable
  total=x+5
  x=2
  print('Inside fun1():',total)
def fun2(y): # in the function what we will introduce it will turn into local variable
  global x
  x=y
fun1()
print('Outside fun1():',total)
fun2(y)
print("x=",x)

# Exercise 6
x=5 #global variable
def fun1(): 
  # total-local variable
  total=x+5
  fun2(total)

def fun2(y):
  global x
  x=y
fun1()

# Exercise 7
def sumList(l):
  result=0
  for i in l:
    result+=i
  return result

print(sumList([1,2,3,4,5])) #3,8,10,11,12

# Function Practice Problem 3
def muLtiply(n):
  item=1
  for i in n:
    item*=i
  return item
print(muLtiply([8, 2, 3, -1, 7]))

# Function Practice Problem 8
def uniqueNumber(n):
  new_list=[]
  for i in n:
    if i not in new_list:
      new_list.append(i)
  print(new_list)
print(uniqueNumber([1, 2, 3, 3, 3, 3, 4, 5]))