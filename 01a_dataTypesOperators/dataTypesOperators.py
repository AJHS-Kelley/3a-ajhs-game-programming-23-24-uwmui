# Data Types and Operators, Ryan Kelley, v0.0

myInt = 5
myFloat = -3.0 

# Arithmetic Operators -- PEMDAS
print(myInt + 25) # Addition 
print(myFloat - 99) # Subtraction 
print(myFloat * 15) # Multiplication 
print(myInt / 10) # Division 
print(myInt ** 2) # Exponents 

# Modulus  -- divides, then returns remainder. 
print(18 % 9) 
# COMMONLY USED TO DETERMINE EVEN/ODDD NUMBERS

# Assignment Operator
myString = "Blah blah blah." 
x = 0
# = means "Assign the variable on the left the value on the right."
# = throws out any previously assigned value! 

# Addition Assignment Operator 
myString += "  I need to buy some eggs."
x += 2 
# += means "Keep the current value and add the new value from the right."

print(myString)
print(x)

# Comparison Operators -- Return True or False
print(3 > 7) # Greater Than 
print(2 >= 1) # Greater Than or Equal To
print(0 < -1) # Less Than 
print(-1 <= 5) # Less Than or Equal To 
print(3 == 7) # Is Equal To 
print(5 != -99) # Not Equal To 

# Logical Operators 
# and requires ALL conditions to be True for overall True. 
print(7 > 2 and 4 < 10) #(True and True) == True 
print(7 > 2 and 4 < 3) #(True and False) == False
print(7 > 2 and 4 > 3 and 1 != 2 and 5 == 5)

# or requires AT LEAST ONE condition to be True for overall True.
print(3 > 6 or 5 < 10) # (False or True) == True 
print(-10 > -5 or 15 < 10) # (False or False) == False 


# not -- 'opposite' value 
favColor = "Green"
print(favColor == (favColor is "Blue"))

print(4 > 3 and 1 != 2 and 5 < 3)
# True and True and False 

# print(keyUp == True and keyLeft == True or keyDown == False)


