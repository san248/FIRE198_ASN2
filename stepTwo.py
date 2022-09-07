import numpy as np
from random import random

# ASN2 Step Two

# Question Two


def matrixSize(A, B):
    if ((len(A) == len(B)) and (len(A[0]) == len(B[0]))):
        return ((A.transpose())*B*(np.linalg.inv(A)))
    else:
        return "Matrices need to be of same size!"

# Question Three


def positiveOrNegativeOne():
    num = np.random.randint(1, 10)
    if(num <= 5):
        return -1
    else:
        return 1


# Question Five
inputList1 = np.random.randint(0, 10, (10, 1))
print("Input List One: ")
print(inputList1)
outputList1 = [0 if (x >= 5 and x <= 7) else x for x in inputList1]
print("Output List One: ")
print(outputList1)

# Question 6
inputList2 = np.random.randint(0, 10, (10, 1))
print("Input List Two: ")
print(inputList2)
outputList2 = ["Even" if x % 2 == 0 else "Odd" for x in inputList2]
print("Output List Two: ")
print(outputList2)

# Question Seven
I = np.random.randint(0, 255, [256, 256])
print("Array I: ")
print(I)
Is = np.dstack([[I]])
Is = np.repeat(Is, 3, axis=0)
print("Array Is: ")
print(Is)


def main():
    A = np.array([[1, -1, 3], [1, 3, -3], [5, 3, 3]])
    B = np.array([[3, 8, 1], [-4, 1, 1], [-4, 1, 1]])
    C = np.array([[5, 7, 8], [5, 3, 8]])
    print(matrixSize(A, B))
    print(matrixSize(B, C))
    print(positiveOrNegativeOne())
    print(positiveOrNegativeOne())
    print(positiveOrNegativeOne())


if __name__ == "__main__":
    main()
