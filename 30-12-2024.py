# Nested Loop
# Exercise 1
for row in range(1,4):
  for col in range(1,4):
    print(col,end=' ')
  print()

# Exercise 2
for i in range(1,6):
  for j in range(1,i+1):
    print(j,end=' ')
  print()

# Exercise 3
x=int(input('Enter a number: '))
for i in range(x,0,-1):
  for j in range(x,i-1,-1):
    print(j,end=" ")
  print()

# Exercise 4
x=int(input('Enter a number: '))
num=1
for i in range(1,x+1):
  for j in range(1,i+1):
      print(num,end=' ')
      num+=1
  print()

# Exercise 5
for row in range(1,3):
  for col in range(row,6,2):
    if row==col:
      break
    else:
      print(col)
  print()

# Exercise 6
for row in range(1,3):
  for col in range(1,6,2):
    if row==col:
      break
    else:
      print(col)
  print()

# Exercise 7
for row in range(1,3):
  for col in range(1,6,2):
    if row==col:
      continue
    else:
      print(col,end=' ')
  print()

# Exercise 8
n=int(input('Enter a number:'))
fac=1
for i in range(1,n+1):
  fac*=i
print(f'Factorial of {n} is {fac}')

# Exercise 9
n1=int(input('Enter the start value: '))
n2=int(input('Enter the end value: '))
fac=n1
for i in range(n1,n2+1):
  fac=1
  for j in range(1,i+1):
    fac*=j
  print(f'Factorial of your input {i} is {fac}')

# Exercise 10
list = ['Saturday', 'Sunday', 'Monday', 'Tuesday']
v = 'AEIOUaeiou'
for i in list:
  count = 0
  for j in i:
    if j in v:
      count += 1
  print(f'Number of vowels in {i} = {count}')
# for i in list:
#   if i in v:
#     count+=1
#   print(count)
for i in list:
  vowel_count = 0
  for j in i:
    if j in v: 
      if j in vowel_count:
        if count>1:
          vowel_count[j] += 1 
      else:
          vowel_count[j] = 0
  print(f'Duplicate vowels in {i} = {vowel_count}')