
#@ Numbers in Python
integer_number = 10
print(type(integer_number))  #/ Output: <class 'int'>

floating_number = 10.5
print(type(floating_number))  #/ Output: <class 'float'>

complex_number = 3 + 4j
print(type(complex_number))  #/ Output: <class 'complex'>


## Basic Arithmetic Operations

#* Addition
print(5 + 3)  #/ Output: 8

#* Subtraction
print(10 - 2)  #/ Output: 8

#* Multiplication
print(4 * 2)  #/ Output: 8

#* Division
print(16 / 2)  #/ Output: 8.0

#* Floor Division (discards the fractional part)
print(17 // 2)  #/ Output: 8

#* Modulus (returns the remainder of the division)
print(18 % 10)  #/ Output: 8

#* Exponentiation (power)
print(2 ** 3)  #/ Output: 8

#* Integer
integer_number = 10
print(type(integer_number))  #/ Output: <class 'int'>

#* Floating-point
floating_number = 10.5
print(type(floating_number))  #/ Output: <class 'float'>

#* Complex numbers
complex_number = 3 + 4j
print(type(complex_number))  #/ Output: <class 'complex'>


## Math Library

import math

#* Square root
print(math.sqrt(64))  #/ Output: 8.0

#* Trigonometric functions
print(math.sin(math.pi / 2))  #/ Output: 1.0
print(math.cos(0))  #/ Output: 1.0

#* Logarithm
print(math.log(2, 10))  #/ Output: 0.3010299956639812 (logarithm of 2 to base 10)
print(math.log(math.e))  #/ Output: 1.0 (natural logarithm)

#* Constants
print(math.pi)  #/ Output: 3.141592653589793
print(math.e)  #/ Output: 2.718281828459045  



## Random Library
import random

#* Random float: 0.0 <= number < 1.0
print(random.random())

#* Random integer within a range
print(random.randint(1, 10))

#* Random choice from a list
choices = ['apple', 'banana', 'cherry']
print(random.choice(choices))

#* Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

## Boolean 

#* Boolean values

is_active = True
print(is_active)  #/ Output: True

is_closed = False
print(is_closed)  #/ Output: False

#* Boolean Operations

print(True and False)  #/ Output: False
print(True or False)  #/ Output: True
print(not True)       #/ Output: False


#* Comparison Operators
print(10 > 5)  #/ Output: True
print(10 == 5) #/ Output: False
print(10 != 5) #/ Output: True


#* Converting to Boolean
print(bool(0))    #/ Output: False
print(bool(42))   #/ Output: True
print(bool(''))   #/ Output: False
print(bool('Hi')) #/ Output: True
 


 
