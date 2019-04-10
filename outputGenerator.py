import os.path, subprocess
from subprocess import STDOUT, PIPE


def runner(inputCode, number):
    
    if number <= 1:
    	inputCode = parser(inputCode)
    return inputCode


def compile_java(java_file):
    subprocess.check_call(["javac", java_file])


def execute_java(java_file):
    java_class, ext = os.path.splitext(java_file)
    cmd = ["java", java_class]
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = proc.communicate()
    return str(stdout)


def baseSolver(num, base):
    vals = "0123456789ABCDEF"
    value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    curr = 1
    total = 0
    for a in range(len(num)):
        total += value[vals.find(num[len(num) - 1 - a])] * curr
        curr = curr * base
    return total


def parser(inputCode):
    parsed = inputCode.split()
    start = 0
    myList = []
    while (
        start == 0
        or parsed[start - 1] == "+"
        or parsed[start - 1] == "*"
        or parsed[start - 1] == "-"
        or parsed[start - 1] == "/"
    ):
        number = parsed[start].split("_")
        total = baseSolver(number[0], eval(number[1]))
        if start != 0:
        	myList.append(parsed[start - 1])
        myList.append(total)
        start += 2
    code = "out.println("
    for a in myList:
    	code += str(a) + " "
    code += ");\n"
    return code
