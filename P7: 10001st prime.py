#What is the 10,001st prime number?
#just generate them all

#which prime do you want?
N = 10001

#a list returning a list where we have True if the element divides n
def mod(list,n):
    output=[]
    for p in list:
        output.append(n % p != 0)
    return output 
#TEST
#list = [2,11,5,35,43]
#print(mod(list,8))   
# 
#We can now define the loop we wnted in the first place because I don't know enough syntax
primes = []
i=2
count = 0
while count < N:
    if all(mod(primes,i)):
        primes.append(i)
        count += 1
    i += 1

print("The " + str(N) +"th prime is " + str(primes[-1]))

#answer is 104,743

#WORKS but run time is ~2mins :( 