'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
'''

#==================================================================
#Idea: I am going to do this by creating a pyramid type as practice in creating types
#==================================================================

#the numbers in a long (suggestively formatted) string
numbers_str = "75 \
95 64 \
17 47 82 \
18 35 87 10 \
20 4 82 47 65 \
19 1 23 75 3 34 \
88 2 77 73 7 63 67 \
99 65 4 28 6 16 70 92 \
41 41 26 56 83 40 80 70 33 \
41 48 72 33 47 32 37 16 94 29 \
53 71 44 65 25 43 91 52 97 51 14 \
70 11 33 28 77 73 17 78 39 68 17 57 \
91 71 52 38 17 14 91 43 58 50 27 29 48 \
63 66 4 68 89 53 67 30 73 16 69 87 40 31 \
4 62 98 27 23 9 70 98 73 93 38 53 60 4 23"

#creating a list, with entries the numbers (as strings)
list_str = numbers_str.split(" ")

#converting the entries to ints.
list_nums =[]

for i in list_str:
    list_nums.append(int(i))


#Defining the class pyramid, on which we are going to implement. Input should be a list of integers filling the pyramid left to right and top to bottom.
class pyra(object): 
    def __init__(self,list):
        self.list = list
    
    #gives pryas a nice print
    def __str__(self):
        #initial output
        display = ""
        #initial max entry of row
        target = 0
        #initial position along row
        counter = 0
        for entry in self.list:
            if target != counter:
                display = display + str(entry) + " "
                counter += 1
            elif target == counter:
                display = display + str(entry) + "\n"
                counter = 0
                target += 1
        return display
    
    def entry(self,r,n):
        '''should take in a pyramid, a row number and an n, should output the nth term of the row'''
        assert n <= r, 'the row does not have that many entries'
        return self.list[n + r*(r+1)//2]

    def __len__(self):
        total = len(self.list)
        length = 0
        i=1
        while total >= i:
            total -= i
            i +=1
            length +=1
        return length

    def subpyra(self,r,n):
        '''creates the sub-pyramid with the nth entry of the rth row at the apex'''
        assert n <= r, 'the row does not have that many entries'
        #initialising sublist
        sublist = []
        #creater the sublist for the subpyramid
        for i in range(r,len(self)+1):
            for j in range(n, n+i-r):
                sublist.append(self.list[j + (i-1)*(i)//2])        
        return pyra(sublist)

#==================================================================
#Idea: Finally we can actually define the function that will solve the problem
#==================================================================

#create the pyramid in question
pyramid = pyra(list_nums)


def max_total(pyramid):
    if len(pyramid) == 1:
        return pyramid.entry(0,0)
    return pyramid.entry(0,0) + max(max_total(pyramid.subpyra(1,0)), max_total(pyramid.subpyra(1,1)))

print('the maximum path is', max_total(pyramid))


















#bug testing
#print(list_nums)
#print(pyramid)
#print(len(pyramid))
#print(pyramid.entry(3,3))
#print(pyramid.subpyra(3,3))