import numpy as np

# ASN2 Step One
# Question One
A = np.array([[1, 2, -1], [2, 4, -3], [1, -2, 0]])
print("matrix one: ")
print(A)
B = np.arange(1, 10, 1).reshape(3, 3)
print("matrix two: ")
print(B)

# Part A
multiply = A * B
print("matrix multiplication: ")
print(multiply)

# Part B
element = A ** B
print("element-wise matrix multiplication: ")
print(element)

# Part C
At = A.transpose()
print("transpose of A: ")
print(At)

inverseA = np.linalg.inv(A)
print("inverse of A: ")
print(inverseA)

print("A^T BA^-1: ")
partC = At*B*inverseA
print(partC)

# Part D
Av = np.reshape(A, (9, 1))
print("vector Av")
print(Av)
Bv = np.reshape(B, (9, 1))
print("vector Bv")
print(Bv)
Cv = np.concatenate([Av, Bv], axis=1)
print("vector Cv")
print(Cv)
l2 = np.linalg.norm(Cv, axis=1)
print("l2 norm of Cv: ")
print(l2)

# Question 2
I = np.random.randint(0, 256, [256, 256])
print("Image I: ")
print(I)
M = np.random.randint(0, 2, [256, 256])
print("Mask M: ")
print(M)

I = np.where(M == 1, 0, I)
print("replacing values of I with zero where M is one: ")
print(I)
