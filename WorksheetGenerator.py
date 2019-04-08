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
                2: singleIfWkst,
		3: IfElseWkst,
		4: IfElseIfElseWkst,
		6: simpleRecur}
    containsInput = True;
    counter = 1
    while counter == 1:
        problemType = 6
        diff = 1
        amount = 50
        #this should do the format
        #1.
        #Problem
        #
        #2.
        #Problem       
        for i in range(amount):
            returner += str(counter) + ".\n" + typeDict[problemType](6,difficulty=diff) + "\n"
            counter += 1
    print(returner)
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
	else:
		operators = "+-*/"
		base1 = random.randInt(2,16)
		base2 = random.randInt(2,16)
		base3 = random.randInt(2,16)
		return baseConverter(random.randInt(2, 1048576), base1) + "_" + base1 + " " + operators[random.randInt(0,3)] + " " + baseConverter(randomInt(2,1048576), base2) + "_" + base2 + operators[random.randInt(0,3)] + " " + baseConverter(randomInt(2,1048576), base3) + "_" + base3 + " = \"__________\"_10"

#problemType 2
#Output format:
#Optional Variables
#if( X1 (>,<,==,!=) Y1)
#	out.println("Hello");
#out.println("World");		
def singleIfWkst(self, difficulty):
	symbols = [">", "<", "==", "!="]
	if difficulty == 1:
		return "if( " + random.randInt(-15,15) + " " + symbols[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\t + out.println(\"Hello\");"
	if difficulty == 2:
		return "if( " + random.randInt(-15,15) + " " + symbols[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\t + out.println(\"Hello\");\nout.println(\"World\");"
	if difficulty == 3:
		return "int x = " + random.randInt(-15,15) + ";\nif( x " + symbols[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\tout.println(\"Hello\");\nout.println(\"World\");"
	if difficulty == 4:
		return "int x = " + random.randInt(-15,15) + ";\n int y = " + random.randInt(-15,15) + ";\nif( x " + symbols[random.randInt(0,3)] + " y )\n\tout.println(\"Hello\");\nout.println(\"World\");"
	if difficulty == 5:
		operators = "+-*/"
		return "int x = " + random.randInt(-15,15) + ";\n int y = " + random.randInt(-15,15) + ";\nif( x " + operators[random.randInt(0,3)] + " " + random.randInt(-15,15) + " " + symbols[random.randInt(0,3)] + " y " + operators[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\tout.println(\"Hello\");\nout.println(\"World\");"

#problemType 3
#Output format:
#Optional Variables
#if( X1 (>,<,==,!=) Y1)
#	out.println("Hello");
#else
#	out.println("World");	
def IfElseWkst(self, difficulty):
	symbols = [">", "<", "==", "!="]
	if difficulty == 1:
		return "if( " + random.randInt(-15,15) + " " + symbols[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\t + out.println(\"Hello\");\nelse\n\tout.println(\"World\");"
	if difficulty == 2:
		return "if( " + random.randInt(-15,15) + " " + symbols[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\t + out.println(\"Hello\");\nelse\n\tout.println(\"World\");"
	if difficulty == 3:
		return "int x = " + random.randInt(-15,15) + ";\nif( x " + symbols[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\tout.println(\"Hello\");\nelse\n\tout.println(\"World\");"
	if difficulty == 4:
		return "int x = " + random.randInt(-15,15) + ";\n int y = " + random.randInt(-15,15) + ";\nif( x " + symbols[random.randInt(0,3)] + " y )\n\tout.println(\"Hello\");\nelse\n\tout.println(\"World\");"
	if difficulty == 5:
		operators = "+-*/"
		return "int x = " + random.randInt(-15,15) + ";\n int y = " + random.randInt(-15,15) + ";\nif( x " + operators[random.randInt(0,3)] + " " + random.randInt(-15,15) + " " + symbols[random.randInt(0,3)] + " y " + operators[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\tout.println(\"Hello\");\nelse\n\tout.println(\"World\");"

#problemType 4
#Output format:
#Optional Variables
#if(X1 (>,<,==,!=) Y1)
#	out.println("Hello");
#else if(X1 (>,<,==,!=) Y1)
#	out.println("Kind");
#else
#	out.println("World");
def IfElseIfElseWkst(self,difficulty):
	symbols = [">", "<", "==", "!="]
	if difficulty == 1:
		return "if( " + random.randInt(-15,15) + " " + symbols[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\t + out.println(\"Hello\");\nelse if( " + random.randInt(-15,15) + " " + symbols[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\t + out.println(\"Kind\");\nelse\n\tout.println(\"World\");"
	if difficulty == 2:
		return "if( " + random.randInt(-15,15) + " " + symbols[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\t + out.println(\"Hello\");\nelse if( " + random.randInt(-15,15) + " " + symbols[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\t + out.println(\"Kind\");\nelse\n\tout.println(\"World\");"
	if difficulty == 3:
		return "int x = " + random.randInt(-15,15) + ";\nif( x " + symbols[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\tout.println(\"Hello\");\nelse if( x " + symbols[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\tout.println(\"Kind\");\nelse\n\tout.println(\"World\");"
	if difficulty == 4:
		return "int x = " + random.randInt(-15,15) + ";\n int y = " + random.randInt(-15,15) + ";\nif( x " + symbols[random.randInt(0,3)] + " y )\n\tout.println(\"Hello\");\nelse if( x " + symbols[random.randInt(0,3)] + " y )\n\tout.println(\"Hello\");\nelse\n\tout.println(\"World\");"
	if difficulty == 5:
		operators = "+-*/"
		return "int x = " + random.randInt(-15,15) + ";\n int y = " + random.randInt(-15,15) + ";\nif( x " + operators[random.randInt(0,3)] + " " + random.randInt(-15,15) + " " + symbols[random.randInt(0,3)] + " y " + operators[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\tout.println(\"Hello\");\nelse if( x " + operators[random.randInt(0,3)] + " " + random.randInt(-15,15) + " " + symbols[random.randInt(0,3)] + " y " + operators[random.randInt(0,3)] + " " + random.randInt(-15,15) + " )\n\tout.println(\"Kind\");\nelse\n\tout.println(\"World\");"

#problemType 5
#Output format:
#String word = "(A-Z)*";
#word = word.(substring(x,y), replace('a','b'), remove('a'), charAt(x), indexOf('a'), lastIndexOf('a'), toUpperCase(), toLowerCase());
#out.println(word);
#INCOMPLETE

"""
def StringMethodProblems(self, difficulty):
	commands = ["toUpperCase(", "toLowerCase(", "charAt(", "indexOf(", "lastIndexOf(", "remove(", "replace(", "substring("]
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	if difficulty == 1:
		word = alphabet[random.randInt(0,52)] for x in range(random.randInt(1,7))
		command = commands[random.randInt(0,1)]
		return "String word = \"" + word +"\";\nword = word." + command+");\nout.println(word);"
	if difficulty == 2:
		word = alphabet[random.randInt(0,52)] for x in range(random.randInt(1,12))
		command = commands[random.randInt(2,4)]
		return "String word = \"" + word+"\";\nword = word." + command + ");\nout.println(word);"
	if difficulty == 3:
		word = alphabet[random.randInt(0,52)] for x in range(random.randInt(1,18))
		command = commands[random.radInt(5,6)]
		return "String word = \"" + word +"\";\nword = word." + command +");\nout.println(word);"
	if difficulty == 4:
		word = alphabet[random.randInt(0,52)] for x in range(random.randInt(1,26))
		return "String word = \"" + word +"\";\nword = word.substring(" + 7 + ");\nout.println(word);"
	if difficulty == 5:
		word = alphabet[random.randInt(0,52)] for x in range(random.randInt(1,7))
		command = commands[random.randInt(0,7)]
		return "String word = \"" + word +"\";\nword = word." + command +");\nout.println(word);"

def classProblems(self,difficulty):
	raise NeedToImplementException

#problemType X
#Output format:
#int[] arr = new int[x];
#for(initializer; conditional; modifier)
#	arr[x] = arr[x (+-*/) y];
#for(initializer; conditional; modifier)
#	out.println(arr[x]);
def arrayIteration(self, difficulty):
	if difficulty == 1:
		operands = ["+","-", "/", "*"]
		return "int [] arr = new int[" + random.randInt(1,8) +"];\nfor(int x = 0; x < arr.length; x++)\n\tarr[x] = arr[x " + operands[random.randInt()] + " " + random.randInt(1,5)+"];\nfor(int x = 0; x < arr.length; x++)\n\tout.println(arr[x]);"
	if difficulty == 2:
		pass
	if difficulty == 3:
		pass
	if difficulty == 4:
		pass
	if difficulty == 5:
		pass
"""
#problemType X
#Output format:
#What is the output of the function call foo(1..15) with foo(num) defined as below.
#public void foo(int num)
#{
#	if(num > (1..10))
#		out.println(num);
#	foo(num - (1..3));	
#}

def simpleRecur(self, difficulty):
	if difficulty == 1:
		return "What is the output of the function call foo(" + str(random.randint(1,15)) + ") with foo(num) defined as below.\npublic void foo(int num)\n{\n\tif(num > " + str(random.randint(1,10)) + ")\n\t\tout.println(num);\n\tfoo(num - " + str(random.randint(1,3)) + ");\n}"

if __name__ == "__main__":
	main()	
#etc...    
              

#End of Generation Functions			  
