#############################
#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#############################

#############################
#Idea: Instead of enumerating a million lexicographical orderings we establish the digits from left to right.
#############################
import math as m 
N  = 1000000
number = N - 1

#here is a script to find the ith digit of the nth permutation and the remaining permutations left
def next(n,i):
    digit = -1
    while n >= 0:
        n = n - m.factorial(10 - i)
        digit += 1
    return (digit, n + m.factorial(10 - i))

print(next(number,1))
print(next(next(number,1)[1], 2))

#here we fold this function to sucessively print the digits of the nth permutation
def permutation(n):
    for i in range(10):
        print(next(n,i+1))
        n = next(n,i+1)[1]

permutation(number)

#It doesn't give the exact answer because it doesnt keep track of the family of digits that have been "used up", but can be deciphered.
#ANSWER: 2783915406
