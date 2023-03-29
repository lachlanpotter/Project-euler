#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#we will just define a (hopefully efficient) lcm function.

def lcm(n,m):
    i=max(n,m)
    while i <= n*m:
        if i % n == 0 and i % m == 0:
            return i
        i += max(n,m)

#to test let N=10
N = 20
i = 1
ans = 1

while i <= N:
    ans = lcm(i,ans)
    i += 1

print("the smallest positive number divisible by all numbers from 1 to " + str(N) + " is " + str(ans))