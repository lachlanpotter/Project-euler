'''

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

'''

N = 1000

total = 0
for digi in str(2**N):
    total += int(digi)

print(total)

    