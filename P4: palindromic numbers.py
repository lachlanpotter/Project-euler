#Find the largest palindrome made from the product of two 3-digit numbers.

#===================================================
#Necessary subfunctions VVVVVVVV
#===================================================
#projection onto third co-ordinate
def p3(a,b,c):
    return c

#TEST
#print(p3(1,2,3))

#define a function that reverses a string 
def reverse(string):
    result = ""
    while string != "": 
        result = string[0] + result
        string = string[1:] 
    return result

#===================================================
#Necessary subfunctions ^^^^^^^^^^
#===================================================

#generate the set of 3-digits x 3-digits along with their product
candidates = [(a,b,a*b) for a in range(100,1000) for b in range(100,1000) if a <= b]


#define a function to check if a given number is a palindrome
palindromes = []
i=0
while i < len(candidates) :
    if str(candidates[i][-1]) == reverse(str(candidates[i][-1])):
        palindromes.append(candidates[i])
    i+=1

#test
#print(palindromes)

#create list of only the product
only_palindromes = []
i=0
while i < len(palindromes) :    
    only_palindromes.append(palindromes[i][-1])
    i+=1

#test
#print(only_palindromes)

#take the largest
largest_palindrome = []
i=0
while i < len(palindromes) :
    if palindromes[i][-1] == max(only_palindromes):
        largest_palindrome.append(palindromes[i])
    i+=1

print(largest_palindrome)





