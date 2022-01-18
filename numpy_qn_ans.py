import numpy as np
a=np.random.randint(10,size=(5,5))
b=np.random.randint(10,size=(5,5))

print("a-> \n",a)
print("b-> \n",b)
print("a+b=> \n",a+b)

#Given a numpy array (matrix), how to get a numpy array output which is equal to the original matrix multiplied by a scalar?
print("2*a =>\n",2*a)

#Create an identity matrix of dimension 4-by-4
i = np.eye(4,dtype=np.int16)
print("identity matrix=> \n",i)

#Convert a 1-D array to a 3-D array

c = np.array([x for x in range(27)])
o = c.reshape(3,3,3)
print("initial \n",c)
print('after reshape \n',o)

#Convert all the elements of a numpy array from float to integer datatype
d=np.array([[2.5,3.8,1.2],[5.6,4.2,9.3]])
print('float ->\n',d)
e = d.astype('int')
print('int conversion \n',e)

#Convert a binary numpy array (containing only 0s and 1s) to a boolean numpy array
a = np.array([[1,0,0],
              [1,1,1],
              [0,1,0]])
print('before -> \n',a)
o = a.astype('bool')
print('after boolean conversion -> \n',o)

#Stack 2 numpy arrays horizontally i.e., 2 arrays having the same 1st dimension (number of rows in 2D arrays)
a1 = np.array([[1,2,3],[4,5,6]])
a2 = np.array([[7,8,9],[10,11,12]])
print("a1 \n",a1)
print("a2 \n",a2)
o = np.hstack((a1,a2))
print('after horizontal stack -> \n',o)

#Stack 2 numpy arrays vertically i.e., 2 arrays having the same last dimension (number of columns in 2D arrays)
o = np.vstack((a1,a2,a1))
print("after vertical stack -> a1-a2-a1 \n",o)

#Generate a sequence of numbers in the form of a numpy array from 0 to 100 with gaps of 2 numbers, for example: 0, 2, 4 ....
o = np.array([x for x in range(0,101,2)])
print(o)

#From 2 numpy arrays, extract the indexes in which the elements in the 2 arrays match
a = np.array([1,2,3,4,5])
b = np.array([1,3,2,4,5])
print("a \n",a)
print("b \n",b)
print("indexes at which values of both arrays are same \n",np.where(a==b))

#Output a sequence of equally gapped 5 numbers in the range 0 to 100 (both inclusive)
o  = np.linspace(0,100,5)
print(o)

#Output a matrix (numpy array) of dimension 2-by-3 with each and every value equal to 5
o = np.full((2,3),5)
print(o)

#Output an array by repeating a smaller array of 2 dimensions, 10 times
a = np.array([[1,2,3],[4,5,6]])
print('original array->\n',a)
o = np.tile(a,10)
print("after doing tile operation \n",o)

#Output a 5-by-5 array of random integers between 0 (inclusive) and 10 (exclusive)
o = np.random.randint(0,10,size=(5,5))
print("random Generated 5*5 matrix \n",o)

#Output a 3-by-3 array of random numbers following normal distribution
o = np.random.normal(size=(3,3))
print("random generated normal numbers \n",o)

#Given 2 numpy arrays as matrices, output the result of multiplying the 2 matrices (as a numpy array)
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print("a=> \n",a)
b = np.array([[2,3,4],
              [5,6,7],
              [8,9,10]])
print("b=> \n",b)
o = a@b
print("multiplication of two matrices a@b is => \n",o)
#alternate solution of above calculation is
o = np.matmul(a, b)
print("multiplication of two matrices is np.matmul(a, b) => \n",o)

#Output the transpose of a matrix (as numpy array)
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print("matrix a is => \n",a)
a_transpose = a.T
print("transpose of the given matrix is => \n",a_transpose)

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

a_transpose = a.T

#Calculate the sine of an array of angles (in radians) using NumPy
angles = np.array([3.14, 3.14/2, 6.28])
sine_of_angles = np.sin(angles)
print('angles is =>',angles)
print('Sine of the given array of angles = ', sine_of_angles)

#Calculate the cosine similarity of 2 vectors (as numpy arrays)
angles = np.array([3.14, 3.14/2, 6.28])
cosine_of_angles = np.cos(angles)
print('angles=>',angles)
print('Cosine of the given array of angles = ', cosine_of_angles)

#Output the array element indexes such that the array elements appear in the ascending order
array = np.array([10,1,5,2])
indexes = np.argsort(array)
print('array \n',array)
print('indexes through which array is being sorted \n',indexes)
