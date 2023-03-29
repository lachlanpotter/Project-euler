##########################################################
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
##########################################################

#I will just try to list all primes less than N

N = 2000000
'''
primes = []
total = 0
for i in range(2,N):
    #we want to do different things depending on if i is prime
    prime = True
    for j in primes:
        if i%j == 0:
            prime = False
            break
    if prime:
        primes.append(i)
        total += i
'''
#The above works but is too longggg, let's try a sieve

#This will detect primality (modulo 1 and 0)
zero_if_prime = [0]*(N+1)

#this will be a running tally of the sum of primes
sum_of_primes = 0

for i in range(2,N+1):
    #check if i is prime
    if zero_if_prime[i] == 0:
        #add i to our tally
        sum_of_primes = sum_of_primes + i
#uncomment below to check for bugs
#        print(sum_of_primes)
        for j in range(2*i,N+1,i):
            #remove multiples of i from our primes
            zero_if_prime[j] = 1

print('The sum of primes below ' + str(N) + ' is ' + str(sum_of_primes))