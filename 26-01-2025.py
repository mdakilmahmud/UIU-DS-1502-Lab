import numpy as np
b=np.array([1,2,3,4,5])
a=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(b) # 1d array
print(a) # 2d array


n1=np.array([2,3,5,7,11])
n2=np.array([[2.1,3.1,5,7,11],[0.1,3.1,5.5,7,3.1]])
print("type(n1)",type(n1))
print("n1.dtype",n1.dtype)
print("n1.ndim",n1.ndim)
print("n1.shape",n1.shape) #(5,)
print("type(n2)",type(n2))
print("n2.dtype",n2.dtype)
print("n2.ndim",n2.ndim)
print("n2.shape",n2.shape) #(5,2)


a1=np.arange(5)
print(a1)
a2=np.arange(5,10)
print(a2)
a3=np.arange(10,1,-2)
print(a3)
a4=np.linspace(0.0,1.0,num=5)
print(a4)
a1=np.arange(1,21).reshape(4,5)
print(a1)
a1=np.arange(1,21).reshape(4,6) # valuerror
print(a1)

# space ber korar system
# (max value-min value)/koto gulo number chaichi-1
# (1-0)/5-1


grades=np.array([[1,2,3],[4,5,6],[7,8,9]])
print((grades.sum(axis=0))) # 0 er jonne row wise
print((grades.sum(axis=1))) # 1 er jonne collum wise
print(grades.mean()) 
print(grades.mean(axis=1)) # 1 er jonne collum wise
print(grades.max())
print(grades.max(axis=0)) # 0 er jonne row wise
print(grades.max(axis=1))
print(grades.min())


a1=np.arange(1,6)
a2=np.linspace(1.1,5.5,5)
print(a1)
print(a2)
print(a1+a2)
print(a1*a2)
print(a1/a2)