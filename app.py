counter = 100 # An integer assignment
miles = 1000.0 # A floating point
name = "John" # A string
print (counter)
print (miles)
print (name)

str = 'Hello World!'
print (str) # Prints complete string
print (str[0]) # Prints first character of the string
print (str[2:5]) # Prints characters starting from 3rd to 5th
print (str[2:]) # Prints string starting from 3rd character
print (str * 2) # Prints string two times
print (str + "TEST") # Prints concatenated string

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list) # Prints complete list
print (list[0]) # Prints first element of the list
print (list[1:3]) # Prints elements starting from 2nd till 3rd
print (list[2:]) # Prints elements starting from 3rd element
print (tinylist * 2) # Prints list two times
print (list + tinylist) # Prints concatenated lists

""" Python Tuples
A tuple is another sequence data type that is similar to the list. A tuple consists of a
number of values separated by commas. Unlike lists, however, tuples are enclosed within
parenthesis.
The main difference between lists and tuples is- Lists are enclosed in brackets ( [ ] ) and
their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) )
and cannot be updated. Tuples can be thought of as read-only lists.  """

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print (tuple) # Prints complete tuple
print (tuple[0]) # Prints first element of the tuple
print (tuple[1:3]) # Prints elements starting from 2nd till 3rd
print (tuple[2:]) # Prints elements starting from 3rd element
print (tinytuple * 2) # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple

""" 
Python Dictionary
Python's dictionaries are kind of hash-table type. They work like associative arrays or
hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any
Python type, but are usually numbers or strings. Values, on the other hand, can be any
arbitrary Python object. """

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one']) # Prints value for 'one' key
print (dict[2]) # Prints value for 2 key
print(dict)  # Prints the dictionary
print (tinydict) # Prints complete dictionary
print (tinydict.keys()) # Prints all the keys
print (tinydict.values()) # Prints all the values

""" Data Type Conversion
int(x [,base]) Converts x to an integer. The base specifies the base if x is a string.
float(x) Converts x to a floating-point number.
complex(real [,imag]) Creates a complex number.
str(x) Converts object x to a string representation.
repr(x) Converts object x to an expression string.
eval(str) Evaluates a string and returns an object.
tuple(s) Converts s to a tuple.
list(s) Converts s to a list.
set(s) Converts s to a set.
dict(d) Creates a dictionary. d must be a sequence of (key,value) tuples.
frozenset(s) Converts s to a frozen set.
chr(x) Converts an integer to a character.
unichr(x) Converts an integer to a Unicode character.
ord(x) Converts a single character to its integer value.
hex(x) Converts an integer to a hexadecimal string.
oct(x) Converts an integer to an octal string. """



a = 21
b = 10
c = 0
c = a + b
print ("Line 1 - Value of c is ", c)
c = a - b
print ("Line 2 - Value of c is ", c )
c = a * b
print ("Line 3 - Value of c is ", c)
c = a / b
print ("Line 4 - Value of c is ", c )
c = a % b
print ("Line 5 - Value of c is ", c)
a = 2
b = 3
c = a**b # exponent
print ("Line 6 - Value of c is ", c)
a = 10
b = 5
c = a//b #floor division (div)
print ("Line 7 - Value of c is ", c)


a = 20
b = 20
print ('Line 1','a=',a,':',id(a), 'b=',b,':',id(b))
if ( a is b ):
 print ("Line 2 - a and b have same identity")
else:
 print ("Line 2 - a and b do not have same identity")
if ( id(a) == id(b) ):
 print ("Line 3 - a and b have same identity")
else:
 print ("Line 3 - a and b do not have same identity")
b = 30
print ('Line 4','a=',a,':',id(a), 'b=',b,':',id(b))
if ( a is not b ):
 print ("Line 5 - a and b do not have same identity")
else:
 print ("Line 5 - a and b have same identity")


# precedence operators

""" ** Exponentiation (raise to the power)
~ + - Ccomplement, unary plus and minus (method names for
the last two are +@ and -@)
* / % // Multiply, divide, modulo and floor division
+ - Addition and subtraction
>> << Right and left bitwise shift
& Bitwise 'AND'
^ | Bitwise exclusive `OR' and regular `OR'
<= < > >= Comparison operators
<> == != Equality operators
= %= /= //= -= += *=
**=
Assignment operators
is is not Identity operators
in not in Membership operators
not or and Logical operators """

a = 20
b = 10
c = 15
d = 5
print ("a:%d b:%d c:%d d:%d" % (a,b,c,d ))
e = (a + b) * c / d #( 30 * 15 ) / 5
print ("Value of (a + b) * c / d is ", e)
e = ((a + b) * c) / d # (30 * 15 ) / 5
print ("Value of ((a + b) * c) / d is ", e)
e = (a + b) * (c / d) # (30) * (15/5)
print ("Value of (a + b) * (c / d) is ", e)
e = a + (b * c) / d # 20 + (150/5)
print ("Value of a + (b * c) / d is ", e)