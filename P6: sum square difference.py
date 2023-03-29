#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

#N=10 to test
N = 100

def sum_of_squares(n):
    i=1
    ans = 0
    while i <= n:
        ans += i**2
        i += 1
    return ans
#TEST        
#print(sum_of_squares(3))

def square_of_sum(n):
    i=1
    sum=0
    while i <= n:
        sum += i
        i += 1
    return sum**2
#TEST
#print(square_of_sum(3))

print(square_of_sum(N) - sum_of_squares(N))