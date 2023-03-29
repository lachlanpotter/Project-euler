##########################
#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
##########################
#Here's the idea
#n+2 total = n total + (n^2 + n + 1) + (n^2 + 2n + 2) + (n^2 + 3n + 3) + (n^2 + 4n + 4)

N=1001

def total(n):
    if n == 1:
        return 1
    elif n > 1:
        return total(n-2) + 4*(n-2)**2 + 10*n - 10

print(total(N))

print(1003**1003 % 10000000000)