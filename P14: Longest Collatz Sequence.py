'''
<p>The following iterative sequence is defined for the set of positive integers:</p>
<p class="margin_left"><var>n</var> → <var>n</var>/2 (<var>n</var> is even)<br /><var>n</var> → 3<var>n</var> + 1 (<var>n</var> is odd)</p>
<p>Using the rule above and starting with 13, we generate the following sequence:</p>
<div class="center">13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1</div>
<p>It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.</p>
<p>Which starting number, under one million, produces the longest chain?</p>
<p class="note"><b>NOTE:</b> Once the chain starts the terms are allowed to go above one million.</p>

'''

#We will solve this using a dictionary that assigns each integer to the length of its Collatz sequence.

#Which starting number under N gives the longest sequence?
N=1000000

dict = {1:1}

#The definition of Collatz is recursive and keeps a dictionary or prior calculated sequences, improving efficiency.
def collatz(i):
    '''takes in a positive int and '''
    if i not in dict:
        if i % 2 == 0:
            dict[i] = collatz(i/2) + 1
        else:
            dict[i] = collatz(3*i+1) + 1
    if i in dict:
        return dict[i]

for i in range(1,N):
    collatz(i)

#a general function to pick out the largest value in a dictionary along with its key(s)
def maxval(dic):
    keys = []
    values = dic.values()
    maxvalue = max(values)
    for key in dic:
        if dic[key] == maxvalue:
            keys.append(key)
    return (keys, maxvalue)

#print(dict)

print(maxval(dict))