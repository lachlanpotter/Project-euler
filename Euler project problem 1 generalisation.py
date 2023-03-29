#choose the multiples that you want to count:
multiples_of = [3,5,7]
no_of_multiples = len(multiples_of)

#choose the upper bound
N = 1000

#===================================
#NOT WORKING YET
#===================================

j=0
while j<2:
    multiples = [x for x in range(N) if x % multiples_of[j] == 0]
    j+=1

#generate list of multiples
#multiples=list(range(0,N))
#i=1
#j=0
#while i < N:
#    while j < 3:
#        if i % multiples_of[j] != 0:
#            multiples.remove(i)
#        j+=1
#    i+=1

print(multiples)

#bug checks 
#print(str(no_of_multiples))