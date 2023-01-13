a=list(range(5))
print(a)
print(type(a))
print(a[0])
[print(type(i)) for i in a]
import array
a=array.array('i',list(range(5)))
print(a)
import array as ar
a=ar.array('i',[1,2,3,4,5])
print(a)
a=ar.array('f',[1,2,3,4,5,6])
print(a)
import numpy as np
a=np.array([range(1,5) for i in [1,2,3,4]])
print('a=np.array([range(1,5) for i in [1,2,3,4]])')
print(a)

a=np.zeros(5,dtype=int)
print('a=np.zeros(5,dtype=int)')
print(a)

a=np.zeros((5,5), dtype=int)
print('a=np.zeros((5,5), dtype=int)')
print(a)

a1=np.random.randint(10,size=10)
print('a1=np.random.randint(10,size=5)')
print(a1)
print(a1.itemsize)
print(a1.nbytes)

a2=np.random.randint(10,size=(4,5))
print('a2=np.random.randint(10,size=(4,5))')
print(a2)

a3=np.random.randint(10,size=(3,2,5))
print('a3=np.random.randint(10,size=(3,2,5))')
print(a3)
print('a3.ndim:',a3.ndim) #số chiều
print('a3.shape:',a3.shape) #kích thước chi tiết
print('a3.size:',a3.size) #tổng số phần tử
print('a3.dtype:',a3.dtype) #kiểu dữ liệu chung

print('a3.itemsize:',a3.itemsize) #4 bytes, kích thước mỗi mảng con
print('a3.nbytes:',a3.nbytes) #bytes, kích thước mảng

print('a1[0]:',a1[0])
a1[0]=3
print('a1[0]:',a1[0])
a1[0]=3.2
print('a1[0]:',a1[0])
#array slicing
print(a1[0:5:2])
print(a2[0][3:])
print(a3[0][0][:3])

a=np.arange(10)
print('a=np.arange(10)')
print(a)

print(a2[0])
print('row a2[0,:]:',a2[0,:])
print('column a2[:,0]:',a2[:,0])

a4=np.arange(10)
print(a4)
a5=a4[:5]
print(a5)
a5[0]=5
print(a4) #binding

