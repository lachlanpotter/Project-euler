#What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?: 
'''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
'''


#first issue is to remember how to store the grid as an array

import numpy as np

#out raw data is not an array :(
A_str = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'

#initialize A
A = np.zeros((20,20))


#overwrite the zero matrix with the correct entry
for i in range(20):
    for j in range(20):
        if int(A_str[3*i + 60*j]) == 0:
            A[i,j] = int(A_str[3*i + 60*j+1])
        else:
            A[i,j] = int(A_str[3*i + 60*j] + A_str[3*i + 60*j+1])

#test your matrix A is correct
#print(A)


#tests horizontal rows of a square matrix X at lease 4x4 for maximum product. Outputs the max product, its factors and their entries in the matrix.
def max_rows(X):
    max_prod = 0
    optimal_entries =  [A[0,0],A[1,0],A[2,0],A[3,0]]
    optimal_placements = [(0,0), (1,0), (2,0), (3,0)]
    for i in range(np.shape(X)[0] - 3):
        for j in range(np.shape(X)[1]):
            #update the maximum if it needs updating
            if max_prod < A[i,j]*A[i+1,j]*A[i+2,j]*A[i+3,j]:
                max_prod = A[i,j]*A[i+1,j]*A[i+2,j]*A[i+3,j]
                optimal_entries = [A[i,j],A[i+1,j],A[i+2,j],A[i+3,j]]
                optimal_placements = [(i,j), (i+1,j), (i+2,j), (i+3,j)]
    return [max_prod, optimal_entries, optimal_placements]

#outcome statement form rows
print("the maximum product of four in a row is", max_rows(A)[0], "as the product of", max_rows(A)[1], "in the places", max_rows(A)[2])




#same function for the columns
def max_cols(X):
    max_prod = 0
    optimal_entries =  [A[0,0],A[0,1],A[0,2],A[0,3]]
    optimal_placements = [(0,0), (1,0), (2,0), (3,0)]
    for i in range(np.shape(X)[0]):
        for j in range(np.shape(X)[1] - 3):
            #update the maximum if it needs updating
            if max_prod < A[i,j]*A[i,j+1]*A[i,j+2]*A[i,j+3]:
                max_prod = A[i,j]*A[i,j+1]*A[i,j+2]*A[i,j+3]
                optimal_entries = [A[i,j], A[i,j+1], A[i,j+2], A[i,j+3]]
                optimal_placements = [(i,j), (i,j+1), (i,j+2), (i,j+3)]
    return [max_prod, optimal_entries, optimal_placements]

#outcome statement from cols
print("the maximum product of four in a column is", max_cols(A)[0], "as the product of", max_cols(A)[1], "in the places", max_cols(A)[2])




#same function for the rdiagonal
def max_rdiag(X):
    max_prod = 0
    optimal_entries =  [A[0,0],A[1,1],A[2,2],A[3,3]]
    optimal_placements = [(0,0), (1,1), (2,2), (3,3)]
    for i in range(np.shape(X)[0] - 3):
        for j in range(np.shape(X)[1] - 3):
            #update the maximum if it needs updating
            if max_prod < A[i,j]*A[i+1,j+1]*A[i+2,j+2]*A[i+3,j+3]:
                max_prod = A[i,j]*A[i+1,j+1]*A[i+2,j+2]*A[i+3,j+3]
                optimal_entries = [A[i,j], A[i+1,j+1], A[i+2,j+2], A[i+3,j+3]]
                optimal_placements = [(i,j), (i+1,j+1), (i+2,j+2), (i+3,j+3)]
    return [max_prod, optimal_entries, optimal_placements]

#outcome statement from rdiagonal
print("the maximum product of four in a leading diagonal is", max_rdiag(A)[0], "as the product of", max_rdiag(A)[1], "in the places", max_rdiag(A)[2])




#same function for the rdiagonal
def max_ldiag(X):
    max_prod = 0
    optimal_entries =  [A[3,0],A[2,1],A[1,2],A[0,3]]
    optimal_placements = [(3,0), (2,1), (1,2), (0,3)]
    for i in range(np.shape(X)[0] - 3):
        for j in range(3, np.shape(X)[1]):
            #update the maximum if it needs updating
            if max_prod < A[i,j]*A[i+1,j-1]*A[i+2,j-2]*A[i+3,j-3]:
                max_prod = A[i,j]*A[i+1,j-1]*A[i+2,j-2]*A[i+3,j-3]
                optimal_entries = [A[i,j], A[i+1,j-1], A[i+2,j-2], A[i+3,j-3]]
                optimal_placements = [(i,j), (i+1,j-1), (i+2,j-2), (i+3,j-3)]
    return [max_prod, optimal_entries, optimal_placements]

#outcome statement from rdiagonal
print("the maximum product of four in a leading diagonal is", max_ldiag(A)[0], "as the product of", max_ldiag(A)[1], "in the places", max_ldiag(A)[2])