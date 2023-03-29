#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#input number here
N0 = 600851475143

#================================
#APPROACH 1
#================================
"""
#generate all factors
factors =[]
n=1
while n < N+1:
    if N % n == 0:
        factors.append(n)
    n+=1

#test
print(factors)

#filter for primes

#take the largest
"""
#================================
#APPROACH 1 IS WAY TOO SLOW
#================================

#================================
#APPROACH 2
#================================
#find factors and take them out as you go. These will end up all being prime
N=N0
primefactors = []
i=2
while i<N0+1:
    if N0 % i != 0:
        i+=1
    if N0 % i == 0:
        N0 = N0/i
        primefactors.append(i)
#test
print(primefactors)
    
largest_prime_factor = max(primefactors)

#test 
#print(largest_prime_factor)
        
answer = "the largest prime factor of " + str(N) + " is " + str(largest_prime_factor)

print(answer)