import WorksheetGenerator as wkst
import outputGenerator as out

def main():
	outputType = eval(input("Which problem would you like?"))
	difficulty = eval(input("How difficult would you like them?"))
	amount = eval(input("How many would you like?"))

	returner = ""
	typeDict = {
		0: wkst.toBaseTen,
		1: wkst.baseConversion,
		2: wkst.singleIfWkst,
		3: wkst.IfElseWkst,
		4: wkst.IfElseIfElseWkst,
		5: wkst.StringMethodProblems,
		6: wkst.classProblems,
		7: wkst.arrayIteration,
		8: wkst.simpleRecur
	}
	temp = ""
	f = open("answers.txt", "w")
	for a in range(amount):
		temp = (
			"\n" + typeDict[outputType](difficulty) + "\n"
		)
		returner += str(a) + " " + temp
		f.write(out.runner(temp))
	f.close()
	f=open("questions.txt","w")
	f.write(returner)
	f.close()
if __name__ == "__main__":
	main()