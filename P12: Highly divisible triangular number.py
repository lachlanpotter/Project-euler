#What is the value of the first triangular number to have over five hundred divisors?

N = 50

#we need a dictionary to make the no_factors function faster

dict = {}
for i in range(2,10000):
    dict[i] = True

#this function will find the number of factors of a given int
def no_factors(n):
    factors = 1
    for i in range(2,n):
        if dict[i]:
            counter = 1
            while n % i == 0 and n >= i:
                counter += 1
                n = n/i
            factors = factors*counter
            for j in dict:
                if j != i and j%i == 0 and dict[j]:
                    dict[j] = False
    return factors


#this loop will enumerate over the triangular numbers and count divisors
def trig_min_fact(n):
    for i in range(2**n):
        if no_factors((i*(i+1))//2) > n:
            return (i*(i+1))//2
#        print(dict)
        
print("The first triangular number with over", N, "factors is", trig_min_fact(N))
#print(no_factors(28))
#print(dict)
#works but runs for too long


''' Even slower firs divisor counter
    # divisors = 0
    # for i in range(1,n+1):
    #     if n % i == 0:
    #         divisors += 1
    # return divisors
    # '''