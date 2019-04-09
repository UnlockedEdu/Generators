import os.path, subprocess
from subprocess import STDOUT, PIPE


def main():
    inputCode = (
        "int x = 8;\n"
        + "int y = -1;\n"
        + "if( x / -6 != y + 5 )\n"
        + '\tout.println("Hello");\n'
        + 'out.println("World");'
    )
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
    answer = execute_java("tester.java")
    f = open("answers.txt", "a")
    f.write(answer)
    f.close()


def compile_java(java_file):
    subprocess.check_call(["javac", java_file])


def execute_java(java_file):
    java_class, ext = os.path.splitext(java_file)
    cmd = ["java", java_class]
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = proc.communicate()
    return str(stdout)


if __name__ == "__main__":
    main()
