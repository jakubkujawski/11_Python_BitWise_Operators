Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#BitWise Operators

# ~, And(&), Or(|), XOR(^), Left Shift (<<), Right Shift(>>)

# Complement Operator (~) - tilde

~12
-13

# ~ it's a reverse ~1 = 0 , ~0 = 1

bin(12)
'0b1100'
# negative numbers are not stored in the system, only positive numbers are stored
# twos compliment
# to find twos compliment first we need to find ones compliment + 1

~-13
12
bin(-13)
'-0b1101'
bin(13)
'0b1101'

# 13 = 00001101 , ones compliment = 11110010 , twos compliment (+1) = 11110011
11110011
11110011

binary_string = "11110011"  # Binary 
decimal_number = int(binary_string, 2)
print(decimal_number)
SyntaxError: multiple statements found while compiling a single statement

binary_string = "11110011"  # Binary 
decimal_number = int(binary_string, 2)
print(decimal_number)
SyntaxError: multiple statements found while compiling a single statement

bin(-13)
'-0b1101'

binary_string = "-0b1101"  # Binary 
decimal_number = int(binary_string, 2)
print(decimal_number)
SyntaxError: multiple statements found while compiling a single statement



~45
-46

~2
-3

~1
-2


12&13
12
#--------------------------------------------------------------------------

# And (&) Operator

12&13
12
# in And both must to be 1 to be 1, If we compare both binary numbers of 12 and 13 : 12 = 00001100 and 13 = 00001101

#00001100
#00001101
#--------
#00001100
#this is 12


# OR (|) Operator

12|13
13

# in OR operator just one needs to be 1 to be 1

#12 = 00001100 and 13 = 00001101 so

#00001100
#00001101
#--------
#00001101
# this is 13

#---------------------------------------------------------------------------

>>> #XOR Operator
>>> 
>>> # 0 0 -> 0 , 0 1 -> 1 , 1 0 -> 1 , 1 1 -> 0
>>> 
>>> # XOR (^)
>>> 
>>> 12 ^ 13
1
>>> 
>>> #12 = 00001100 and 13 = 00001101 so
... 
>>> #00001100
... #00001101
... #--------
>>> #00000001
>>> # this is 1
>>> 
>>> 
>>> 25 ^ 30
7
>>> #-----------------------------------------------------------------------------
>>> 
>>> #Left Shift (<<) Operator
>>> 
>>> 10 << 2
40
>>>  # 10 = 1010, 5 = 5.0 = 5.000  when left shifting it means adding zeros on the left side of the dot, in above example 10 is 1010 so shifting left by 2 is adding two 0s so 101000 -> 40 (and this is 40)
...  
>>> 
>>> # Right Shift (>>) Operator
>>> 
>>> 10 >> 2
2
>>> 
>>> # Right Shift is cutting two last numbers so 10 = 1010 so cutting two last numbers gives 10 which is 2 in decimal
>>> 
