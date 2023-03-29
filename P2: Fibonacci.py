#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#we start with the first two terms and generate the rest
fib = [1,1,2]
N = 4000000 

n=2
while fib[n] < N:
    fib.append(fib[n] + fib[n-1])
    n+=1
#test
#print(fib)

#take the even ones
even_fib = []
i=0
while i < len(fib):
    if fib[i] % 2 == 0:
        even_fib.append(fib[i])
    i+=1

#test
print(even_fib)

answer = sum(even_fib) 

print("the sum of even fibbonaci numbers less than " + str(N) + " is " + str(answer))