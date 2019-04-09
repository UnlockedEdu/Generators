import os.path, subprocess
from subprocess import STDOUT, PIPE


def runner(inputCode):
    inputCode = inputCode.replace("\n", "\n\t\t")
    f = open("tester.java", "w")
    testSkeleton = (
        "import static java.lang.System.*;\n"
        + "import java.util.*;\n"
        + "import java.io.*;\n\n"
        + "public class tester \n"
        + "{\n"
        + "\tpublic static void main(String[]args)\n"
        + "\t{\n"
        + "\t\t "
        + inputCode
        + "\n"
        + "\t}\n"
        + "}"
    )
    f.write(testSkeleton)
    f.close()
    compile_java("tester.java")
    return execute_java("tester.java")


def compile_java(java_file):
    subprocess.check_call(["javac", java_file])


def execute_java(java_file):
    java_class, ext = os.path.splitext(java_file)
    cmd = ["java", java_class]
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = proc.communicate()
    return str(stdout)
