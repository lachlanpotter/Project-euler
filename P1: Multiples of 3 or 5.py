#Q1: Find the sum of all the multiplies of 3 or 5 below 1000

#this will be the list of multiples
multiples = []

#gotta generate the list
i=1
while i < 1000:
    if(i % 3 == 0 or i % 5 == 0):
        multiples.append(i)
    i += 1
#can remove the comment below to bug check
print(multiples)

#summing the list
total = sum(multiples)

#printing the answer, have to stringify the result
print("the sum of multiples of 3 or 5 below 1000 is" + str(total))