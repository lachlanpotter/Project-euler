##########################
#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
##########################

N=1000

def last10(n):
    if n==3:
        return 1 + 2**2 + 3**3
    elif n>1:
        return (last10(n-1) + n**n) % 10000000000

print(last10(N))

#Weird n=3 base case was use to avoid a recursion depth error