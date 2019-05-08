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
        8: wkst.simpleRecur,
    }
    methods = ""
    methodCallers = ""
    temp = ""
    ans = ""
    f = open("answers.txt", "w")
    compiler = open("tester.java", "w")
    for a in range(amount):
        temp = "\n" + typeDict[outputType](difficulty) + "\n"
        returner += str(a) + " " + temp
        temp = out.runner(temp, outputType)
        methods += "public static void method" + str(a) + "()\n{\n\t" + temp + "}"
        methodCallers += "method" + str(a) + "();\n"

    testSkeleton = (
        "import static java.lang.System.*;\n"
        + "import java.util.*;\n"
        + "import java.io.*;\n\n"
        + "public class tester \n"
        + "{\n"
        + "\tpublic static void main(String[]args)\n"
        + "\t{\n"
        + "\t\t "
        + methodCallers
        + "\n"
        + "\t}\n"
        + methods
        + "}"
    )
    compiler.write(testSkeleton)
    compiler.close()
    out.compile_java("tester.java")
    f.write(out.execute_java("tester.java"))
    f.close()
    f = open("questions.txt", "w")
    f.write(returner)
    f.close()


if __name__ == "__main__":
    main()
