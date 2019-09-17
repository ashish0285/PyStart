""" count = 0
while count < 5:
 print (count, " is less than 5")
 count = count + 1
else:
 print (count, " is not less than 5")

for var in list(range(5)):
    print (var) """

""" for letter in 'Python': # traversal of a string sequence
 print ('Current Letter :', letter)
print()
fruits = ['banana', 'apple', 'mango']
for fruit in fruits: # traversal of List sequence
 print ('Current fruit :', fruit)
print ("Good bye!") """

""" fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
 print ('Current fruit :', fruits[index])
print ("Good bye!") """
""" 
numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if num%2==0:
        print ('the list contains an even number')
        break
else:
    print ('the list doesnot contain even number') """


""" import sys
list=[1,2,3,4]
it = iter(list) # this builds an iterator object
print (next(it)) #prints next available element in iterator
# Iterator object can be traversed using regular for statement

for x in it:
    print (x, end=" ")
# or using next() function
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit() #you have to import sys module for this
 """
""" A generator is a function that produces or yields a sequence of values using yield method.
When a generator function is called, it returns a generator object without even beginning
execution of the function. When the next() method is called for the first time, the function
starts executing, until it reaches the yield statement, which returns the yielded value. The
yield keeps track i.e. remembers the last execution and the second next() call continues
from previous value.
The following example defines a generator, which generates an iterator for all the Fibonacci
numbers.  """

import sys
def fibonacci(n): #generator function
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(5) #f is iterator object
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()