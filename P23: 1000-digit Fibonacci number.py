'''

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

'''

#first define a fib function that uses a dictionary

fib_dict = {0:0, 1:1}

def fib(n):
    if n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = fib_dict[n-1] + fib_dict[n-2]
        return fib_dict[n]

n=1
index = 1
while fib(n-1) < 10**999:
    print(fib(n), "has index", index)
    n+=1
    index += 1