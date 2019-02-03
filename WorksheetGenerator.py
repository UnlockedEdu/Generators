import random

#ToDo
#Find out all question types from Mason
#Implement all question types
#Figure out Databases
#Implement Databases
#Work on output formatting
#Work on difficulty Scaling
#Work on reasonable probability between procedural and database problems
#Fix bugs
#Fix bugs
#Learn Python
#Learn how I will be retrieving data(not a priority)

def main():
    returner = ""
    typeDict = {0: toBaseTen,
                1: baseConversion,
                2: stringWkst}
    containsInput = True;
    counter = 1
    while containsInput:
        problemType = 'input'
        difficulty = 'input'
        amount = 'input'
        #this should do the format
        #1.
        #Problem
        #
        #2.
        #Problem       
        for i in range(amount):
            returner += counter++ + ".\n" + typeDict[problemType](difficulty) + "\n"
    return returner
#Begining of Helper Functions
#a function that allows me to convert a number from base 10 to base x(2-16) because apparently python doesn't have this already?
def baseConverter(self, num, x):
	ans = ""
	key = "0123456789ABCDEF"
	while num < x:
		ans = key[num % x] + ans
		num = num//x
	return num + ans

#End of Helper Functions

#Begining of Generation Functions


#problemType 0
#Output format:
#X_Y = "_____"_10
def toBaseTen(self, difficulty):
	if difficulty == 1:
		bases = [2, 8, 16]
		base = bases[random.randInt(0,2)]
		return baseConverter(random.randInt(2, 32), base) + "_" + base + " = \"__________\"_10"
	elif difficulty == 2:
		bases = [2, 8, 16]
		base = bases[random.randInt(0,2)]
		return baseConverter(random.randInt(2, 256), base) + "_" + base + " = \"__________\"_10"
	elif difficulty == 3:
		bases = [2, 4, 8, 16]
		base = bases[random.randInt(0,3)]
		return baseConverter(random.randInt(2, 1024), base) + "_" + base + " = \"__________\"_10"
	elif difficulty == 4:
		bases = [2, 4, 8, 12, 16]
		base = bases[random.randInt(0,4)]
		return baseConverter(random.randInt(2, 32768), base) + "_" + base + " = \"__________\"_10"
	elif difficulty == 5:
		base = bases[random.randInt(2,16)]
		return baseConverter(random.randInt(2, 1048576), base) + "_" + base + " = \"__________\"_10"

#problemType 1	
#Output format:
#X1_Y1 (+-*/) X2_Y2 = "______"_10
def baseConversion(self, difficulty):
	if difficulty == 1:
		operators = "+-"
		bases = [2, 8, 10]
		base1 = bases[random.randInt(0, 2)]
		base2 = bases[random.randInt(0,2)]
		return baseConverter(random.randInt(2, 32), base1) + "_" + base1 + " " + operators[random.randInt(0,1)] + " " + baseConverter(randomInt(2,32), base2) + "_" + base2 + " = \"__________\"_10"
	elif difficulty == 2:
		operators = "+-"
		bases = [2, 8, 10, 16]
		base1 = bases[random.randInt(0, 3)]
		base2 = bases[random.randInt(0,3)]
		return baseConverter(random.randInt(2, 256), base1) + "_" + base1 + " " + operators[random.randInt(0,1)] + " " + baseConverter(randomInt(2,256), base2) + "_" + base2 + " = \"__________\"_10"
	elif difficulty == 3:
		operators = "+-*/"
		bases = [2, 8, 10, 16]
		base1 = bases[random.randInt(0, 3)]
		base2 = bases[random.randInt(0,3)]
		return baseConverter(random.randInt(2, 1024), base1) + "_" + base1 + " " + operators[random.randInt(0,3)] + " " + baseConverter(randomInt(2,32), base2) + "_" + base2 + " = \"__________\"_10"
	elif difficulty == 4:
		operators = "+-*/"
		bases = [2, 8, 10, 16]
		base1 = bases[random.randInt(0, 3)]
		base2 = bases[random.randInt(0,3)]
		base3 = bases[random.randInt(0,3)]
		return baseConverter(random.randInt(2, 32768), base1) + "_" + base1 + " " + operators[random.randInt(0,3)] + " " + baseConverter(randomInt(2,32768), base2) + "_" + base2 + operators[random.randInt(0,3)] + " " + baseConverter(randomInt(2,32768), base3) + "_" + base3 + " = \"__________\"_10"
	else
		operators = "+-*/"
		base1 = random.randInt(2,16)
		base2 = random.randInt(2,16)
		base3 = random.randInt(2,16)
		return baseConverter(random.randInt(2, 1048576), base1) + "_" + base1 + " " + operators[random.randInt(0,3)] + " " + baseConverter(randomInt(2,1048576), base2) + "_" + base2 + operators[random.randInt(0,3)] + " " + baseConverter(randomInt(2,1048576), base3) + "_" + base3 + " = \"__________\"_10"

#problemType 2
#Output format: 		
def singleIfWkst(self, difficulty):
	if difficulty == 1:
		pass
	if difficulty == 2:
		pass
	if difficulty == 3:
		pass
	if difficulty == 4:
		pass
	if difficulty == 5:
		pass

#etc...    
              

#End of Generation Functions			  
