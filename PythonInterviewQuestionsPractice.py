'''
1.	What is Python and what are its features?
    Python is an inturpreted, high-level, general-purpose programming language. Emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected.  

    Python an an Easy to learn interpreted language. Its platform independent and comes with a large standard library. its an OOL, Dynamicly Typed, and has Garbarge Collection

2.	Explain the difference between Python 2 and Python 3.
    There is 5 main differences:
    1. Syntax
    2. String Repersentation. In 2 they're a sequence of bytes but in 3 Strings are repped by unicode
    
    Notes:
    1. Libraries: Some Libs aren't updated to work with Python 3
    2. Compatibaility: Python 3 isn't backwards compatible 
    3. Development: python 2 is no longer devloped while 3 is the primary focus


3.	What are the built-in data types in Python?
    * Numbers
    * Floating point
    * String 
    * bool
    * none

    if we include  mapping and sequences then also:
    * list
    * tuple
    * Set
    * range
    * dict

4.	What is the difference between a tuple and a list in Python?
    Tuples are immutable,declared by ()  
    lists are mutable, declared by []

5.	How do you create a dictionary in Python?
    Using {} with a : in the middle to denote between key and valuse.
    ex: {'key1':1}

6.	What is a generator in Python?
    A function that yeilds an iterator instead of using like a function that returning them. It allows a sequence of valuse to be generatead without storing the entire sequence in memory at one time

7.	What are the different types of loops in Python and when would you use each one?
    * for   : when iterating through sequences or doing an action a defined amount of times
    * while : when an actionm needs to be ran until a particluar condtion is met


8.	What is a decorator in Python?

9.	How do you handle exceptions in Python?

10.	What is the difference between a module and a package in Python?

11.	What is PEP 8 and why is it important?

12.	How do you debug Python code? (dubugger included)

13.	How would you reverse a string in Python?

14.	What are the advantages of using NumPy over regular Python lists?

15.	What are the different types of inheritance in Python?

16.	How do you implement a linked list in Python?

17.	What is the difference between deep and shallow copying in Python?

18.	What are the benefits of using a virtual environment in Python?

19.	Explain the difference between *args and **kwargs in Python.
    While both are passed into functions, using Kwargs or Keyword Varibles, the order of passage doesn't matter where if you pass in args or arguments into a function now the order matters
    
20.	How do you check if a string is a palindrome in Python?
'''


#Programming questions:
#Write a Python function to calculate the factorial of a number.

print('\n')
print('\n')
print('\n')

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        print("Argument(s) is/are:", *args)
        result = func(*args, **kwargs)
        print("Function", func.__name__, "returned:", result)
        print('\n')
        return result
    return wrapper
    

@log_decorator
def factorial(num):
    answer = 1
    for i in range(1,num):
        answer = answer*i   
    return answer

test = 5
factorial(test)

#Write a Python function to check if a number is prime.

@log_decorator
def isAPrime(num):
    prime = True
    if (num%2==0):
        prime = False
    elif (num%3==0):
        prime = False
    elif (num%4==0):
        prime = False
    elif (num%5==0):
        prime = False
    elif (num%6==0):
        prime = False
    elif (num%7==0):
        prime = False
    elif (num%8==0):
        prime = False
    elif (num%9==0):
        prime = False
    return prime

test = 37
isAPrime(test)


#Write a Python function to check if a string is a palindrome.
@log_decorator
def isAPalindrome(input):
    palin = False
    input = input.lower().replace(" ", "")
    inputR = input[::-1]
    if input == inputR:
        palin = True
    return palin

test = 'Race Cart'
isAPalindrome(test)
#Write a Python program to check if two strings are anagrams.
@log_decorator
def anagram(one,two):
    x = []
    one = sorted(one.replace(" ","").lower())
    two = sorted(two.replace(" ","").lower())
    if(len(one)!=len(two)):
        return False
    for i in range(0,len(one)):
        if one[i] != two[i]:
            return False
    return True


test = 'Tom Marvolo Riddle'
test2 = 'I Am Lord Voldemort'
anagram(test,test2)

#Write a Python program to reverse a string.
@log_decorator
def stringReversal(input):
    return input[::-1]

test = 'I Am Lord Voldemort'
stringReversal(test)

#Write a Python program to sort a list of integers.
@log_decorator
def sortNumbers(nummies):
    return sorted(nummies)

test = [23,345,1234,45,21,76,231,456,123,69]
sortNumbers(test)

#Write a Python program to find the common elements between two lists.
@log_decorator
def FindingSimilarItems(one,two):
    answer = set(one).intersection(set(two))
    return answer

test1 = [23,345,1234,45,21,76,231,456,123,69]
test2 = [21, 23, 45, 76, 123, 231, 345, 456]
FindingSimilarItems(test1,test2)



#Write a Python function to find the maximum and minimum elements in a list.
@log_decorator
def findMinimumAndMaximumInList(input):
    minn = min(input)
    maxx = max(input)
    return (f'Max: {maxx} | Min: {minn}')

test = [23,345,1234,45,21,76,231,456,123,69]
findMinimumAndMaximumInList(test1)


#Write a Python program to remove duplicates from a list.
@log_decorator
def removeDuplicatesFromList(input):
    return set(input)


test = [37,37,37,37,37,37,23,23,23,23,76,87,99,99,99,99]
removeDuplicatesFromList(test)

#Write a Python program to find the second largest number in a list.
@log_decorator
def findSecondHighestInList(input):
    input.pop(input.index(max(input)))
    answer = max(input)
    return answer

test = [23,345,1234,45,21,76,231,456,123,69]
findSecondHighestInList(test1)

#Write a Python program to calculate the average of a list of numbers
@log_decorator
def findAverageInList(input):
    Answer = 0
    dividen = 0
    for i in range(0,len(input)):
        dividen += 1
        Answer += input[i]
    if dividen == 0:
        return -1
    return Answer/dividen

test = [23,345,1234,45,21,76,231,456,123,69]
findAverageInList(test)

#Write a Python function to check if a string is a valid IP address.
@log_decorator
def isAnIpAddress(ip):
    holder= ip.split(".")
    if len(holder) != 4:
        return False
    else:
        if 0>int(holder[0]) or int(holder[0])>255:
            return False
        if 0>int(holder[1]) or int(holder[1])>255:
            return False
        if 0>int(holder[2]) or int(holder[2])>255:
            return False
        if 0>int(holder[3]) or int(holder[3])>255:
            return False
        return True
    
test = '0001.0000.23.256'
isAnIpAddress(test)

#Write a Python program to generate all permutations of a list.
@log_decorator
def findAllPermutations(daList):
    answer=[]
    for i in range(0,len(daList)):
        for j in range(0,len(daList)):
            answer += [((daList[i],daList[j]))]

    return answer

test1 = [1,2,3,4,5,6,7,8,9]
findAllPermutations(test1)

#Write a Python function to check if a given year is a leap year.
@log_decorator
def isLeapYear(year):
    if (year%4 == 0):
        return True
    else:
        return False

testyear = 2000
isLeapYear(testyear)

#Write a Python program to find the most frequent element in a list.
@log_decorator
def findMode(daList):
    theDict = {}
    for x in daList:
        if(x not in theDict):
            theDict.update({x:1})
        elif(x in theDict):
            theDict[x] += 1
     
    getReturn = 0
    toReturn = ''
    for key in theDict:
        if theDict[key] > getReturn:
            getReturn = theDict[key]
            toReturn = key
    return toReturn

test = ['a','b','c','a','a','a','a','b','b','b','c','c','c','c','c','c']
findMode(test)





