
import random

# def functionName(): # Function Signature
# 	print("What is your name?\n")
# 	name = input("Please type it and press enter.\n")
# 	print(f"Hello, {name}.\n")

# # Call The Function
# functionName()

# def happyBirthday(numTimes, age):
# 	count = 0
# 	while count < numTimes:
# 		print("Happy Birthday!\n")
# 		count += 1
# 	print(f"Wow, you're {age} years old!\n")
	
# happyBirthday(10,55)
# happyBirthday(15,35)
# happyBirthday(17,35)
# happyBirthday(25,25)

# def functionWithReturn(num1, num2):
# 	sum = num1 + num2
# 	quotient = sum / 5
# 	return quotient
	
# example = functionWithReturn(5, 10)
# print(example)

def rollDice(numRoll, sizeRoll):
	count = 0
	sum = 0
	while count < numRoll: 
		roll = random.randint(1, sizeRoll)
		#print(f"Roll #{count}: {roll}\n")
		sum += roll
		count += 1
	#print(sum)
	return sum 

# print("D4 Rolls")
# d4Sum = rollDice(10, 4)
# print("D20 Rolls")
# d20Sum = rollDice(2, 20)

rollDice(10, 4)
rollDice(2, 20)

def genStat(): # Roll 4d6, drop the lowest.
	rolls = []

	count = 0
	while count < 4:
		rolls.append(rollDice(1, 6))
		count += 1
	
	# Sort, Drop Lowest
	rolls.sort()
	rolls.pop(0)
	return(sum(rolls))

count = 0
while count < 1000000:
	test = genStat()
	if test > 18:
		print ("You have exceeded the maximum roll.\n")
	if test < 3:
		print("You have not met the minimum roll.\n")
	count += 1
print ("If no error messages, all stats are within range.\n")

	
strength = genStat()
print(f"Your strength: {strength}\n")