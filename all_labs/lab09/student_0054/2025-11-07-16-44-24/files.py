# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED


"""
Write a function called print_stars_to_file. It should take an integer n as a parameter (you can
assume n>=1), and it should create a text file named stars_n.txt, where n is the actual value of the
parameter n. In this text file, it should contain n lines of text:


the first line is (n-1) leading space characters followed by 1 star character *
the second line is (n-2) spaces followed by 3 stars
the third line (n-3) spaces followed by 5 stars
the fourth line is (n-4) spaces followed by 7 stars
the n-th line (last line) has (2*n-1) stars with no leading space character

For example, calling print_stars_to_file(3) would create 
a file named stars_3.txt which has the following content:
*
***
*****

Specifically, your function should:
Open a file named stars_n.txt (where n is the value of the parameter) in 'w' (write-only) mode.
Write n lines of stars to the file as described on the previous page. The number of leading space
characters and stars must match the description exactly. There should be NO trailing space
characters at the end of each line.
It’s ok if your file contains a trailing empty line at the end, as long as that line has no character.
Do NOT ask the user for any input.
Do NOT include the function call to this function when you submit.

Tip: There are several ways to write strings to a file. You can use a file’s write function -- if you do, note
that this function does not automatically write a newline character, so you need to include an explicit
'\n' (i.e., newline) character at the end of each line. Alternatively, you can use the familiar print
function, with an extra argument that says file=f, where f is the file variable. For example,
print('Hello', file=f) will write the string 'Hello' to the file you opened as variable f. The print
function automatically adds a newline character each time you call it.
When you are done writing this function, call print_stars_to_file(3) in your program, and then
check if it successfully created a file named stars_3.txt in the current working directory -- this is
usually the directory you see at the Terminal window in VSCode. If you don’t know how to find this
directory, ask a staff member to help you. Open this file to see if it has the expected content. Feel free
to try a few other parameter values to verify that all resulting files are correct.
Tip: If you encounter any problem, we strongly encourage you to use the debugger to execute your code
one line at a time and figure out what may be wrong. This is the standard way we debug and fix issues
in a program. When you write a complex program, you can’t expect to simply eyeball the code to figure
out the problems -- the debugger is your best and most effective tool.
"""


def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n+1):
            spaces = n - i
            stars = 2*i - 1
            line = (' ' * spaces) + ('*' * stars)
            f.write(line + '\n')


"""Write a function called calc_avg_from_file. It takes no parameters, and its task is to calculate and
return the average grade from a text file named grades.txt, which stores the students’ grades, one
number per line. For example, grades.txt may have the following content:
82.5
93
77.5
65

Your function should read from this file, get all the numbers, calculate, and return the average of them,
which is 79.5 in this particular example. Specifically, your function should:
Open the file named grades.txt in 'r' (read-only) mode.
Read the entire content of the file into a string. If you opened the file as f, you can do
text=f.read() to read the whole content into a string called text. Using the above example, this
string will have the following characters: '82.5\n93\n77.5\n65'. Note there is a newline
character '\n' after each number (except the last one).
Split the text into individual grades. Because the numbers are separated by '\n'
, we can use text.split('\n') to return a list of strings, each representing an individual grade. Using the
above example, this will return a list that looks like: ['82.5','93','77.5','65']
Calculate and return the average grade using this list. Note that this is a list of strings, so to
perform arithmetic calculations, you need to cast each string to a float.
This function should only read from grades.txt and should NOT write anything to any file.
When you are done writing this function, create a grades.txt file yourself and use it to test your
function. Specifically, in VSCode, you can click File -> New Text File, and write some numbers there,
such as the above 4 numbers. Make sure the file has NO trailing empty line at the end (i.e., your last
number should NOT be followed by a newline) -- if you have a trailing empty line, the string’s split
function will create an empty string at the end of the list, which is not what we want.
Then click File -> Save As to save your numbers as grades.txt in the current working directory. Again,
it is generally the directory you see at the Terminal window in VSCode. Finally, in your program, call
print(calc_avg_from_file()) and see if it prints out the correct result. You can also change the
numbers in grades.txt, save it, and run your program again and verify the result is still correct. If you
encounter any problems, use the debugger to help you figure out the issue.
"""

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text = f.read()  
    grade_strings = text.split('\n')
    grades = [float(g) for g in grade_strings]
    average = sum(grades) / len(grades)
    return average
