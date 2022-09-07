# FIRE198_ASN2
FIRE198 - Autonomous Unmanned Systems stream 

Code corresponding to assignment two

Simple matrix manipulation

Step 1:

1. Your task it to implement the following using only Numpy and built-in Python data-structures.
Construct two random 3 x 3 matrices A and B. Now perform the following operations, (a) AB(matrix multiplication), (b) A⊙B (element-wise multiplication), (c)A^T * B * A^-1, (d) Reshape A and B to  vectors A_v, B_v and concatenate A_v, B_v to make a  9x2 vector called C_v. Now compute the I_2 norm of C_v which will be of size 9x1.

2. Create a random Image I of size 256x256 whose element values range from [0,255]. Create another random Mask M of size 256x256 whose element values are either 0 or 1. Now replace the values in Image I at indexes corresponding to ones in mask M to 0.


Step 2: 
1. (Not a coding question)
 
2. Create a function that takes two numpy array square matrices A and B of any size and does the following: (a) Raise an exception with the message "Matrices need to be of same size!", (b) If matrices are of same size, return the value . Test your function with random sample matrices A and B from the main function.

3. Create a function that returns a value of -1 or +1 with equal probability. Test your function from the main function.

4. (Not a coding question)

5. Create a random list of numbers of length 10 where each element varies from 0 to 10. Then use list comprehension to create a new list where any number between [5, 7] in the original is set to zero and other numbers remain the same. E.g., input list: [0,1,1,2,3,4,5,7,9,0], output list: [0,1,1,2,3,4,0,0,9,0].

6. Create a random list of numbers of length 10 where each element varies from 0 to 10. Then use list comprehension to create a new list that has "Even" and "Odd" for each number (Assume 0 to be even). E.g., input list: [0,1,1,2,3,4,5,7,9,0], output list: [Even, Odd, Odd, Even, Odd, Even, Odd, Odd, Odd, Even].

7. Create a random numpy array I of size 256x256 whose element values range from [0, 255]. Now create an array I_s which is of size (256 x 256 x 3) where each of the third channel (python index 2) is a copy of the image.




