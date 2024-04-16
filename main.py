# PYTHON ESSENTIAL-1 PROGRAMS.
# PROGRAM-1
print("Hello world")
print("My name is", "Python.")
print("Monty Python.")
print("Hey Swetha")
print("Hey Swetha,How are you..!")
# PROGRAM-2
# this is key arguments mechanism in python.
print("My name is", "Python.", end=" ")
print("Monty Python.")
print("my name is python", "my sis name is python.1", end=" ")
print("my bro name is python.2")
# PROGRAM-3
# we use this \n then we will observe the difference.
print("My name is", "Python.", end="\n")
print("Monty Python.")
# another example.
print("My name is ", end="")
print("Monty Python.")
# another key argument "Sep=which will be used for seperate the string.
print("My", "name", "is", "Monty", "Python.", sep="-")
#  we will make the difference and run the code.
print("My", " ", " ", " ", "Python.", sep="-")
# instead of useing"-"  this we will use sep="$".
print("My", "name", "is", "Monty", "Python.", sep="$")
# Using two key arguments.
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python", sep="...", end="")
# PROGRAM-4
# printing arrow
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
print("    @")
print("   @ @")
print("  @   @")
print(" @     @")
print("@@@   @@@")
print("  @   @")
print("  @   @")
print("  @   @")
print("  @@@@@")
# PROGRAM-5
# octal and hexadecimal numbers
print(0o123)
print(0x123)
# Esacpe charectors
print("I like \"Monty Python\"")
print('I like "Monty Python"')
# using two=',""- Coding Strings
print('I\'m Monty Python.')
print("I'm Monty Python.")
#  two Boolean values have strict denotations in Python:(true, false)
print(True > False)
print(True < False)
# PROGRAM-6
# LAB-code
print("\"I'm\"\n\"\"learning\"\"\n\"\"\"python\"\"\"\n")
# Operators-Data manipulation tools
# +, -, *, /, //, %, **
# exponentiation
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
# ex
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
# Division
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
# Integer division
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
print(6 // 4)
print(6. // 4)
print(-6 // 4)
print(6. // -4)
# Operators: remainder (modulo)
print(14 % 4)
print(14 // 4)
print(3 * 4)
print(12 % 4.5)
# Operators: addition
print(-4 + 4)
print(-4. + 8)
# The subtraction operator, unary and binary operators
print(-4 - 4)
print(4. - 8)
print(-1.1)
print(-5. - 5)
# Operators and their bindings
print(9 % 6 % 2)
# binding ex
print(2 ** 2 ** 3)
# List of priorities-1.**,2.+,-(unary),3.*, /, //, %,4.+,-(binary)
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
# EX-1:
print((2 ** 4), (2 * 4.), (2 * 4))
# Exercise 2
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
# Exercise 3:
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
var = 1
print(var)
# ex:
var = "3.8.5"
print("Python version: " + var)
# Assigning a new value to an already existing variable
var = 1
print(var)
var = var + 1
print(var)
# PROGRAM-7
# mathematical problem
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c=", c)
# PROGRAM-8
# LAB code:
john = 3
marry = 5
adam = 6
total_apples = john + marry + adam
print("total_apples=", total_apples)
swetha = 20
sowmya = 10
hari = 50
total_apples = swetha * hari + sowmya
print("Total number of apples:", total_apples)
# PROGRAM-9
# LAB-CODE
kilometers = 12.25
miles = 7.38
miles_to_kilometers = 11.88
kilometers_to_miles = 7.61
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
# comments ON COMMENTS
x = 1
y = 2
# y = y + x
print(x + y)
# The input() function
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")
# Type casting
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
# EX:
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a ** 2 + leg_b ** 2) ** .5
print("Hypotenuse length is", hypo)
# PROGRAM-10
# String operators:
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")  # Concatenation
# Replication:
# string * number,
# number * string.
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
# Type conversion: str()
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a ** 2 + leg_b ** 2) ** .5))
# PROGRAM-11
# LIST
my_list = []  # Creating an empty list.
for i in range(5):
    my_list.append(i + 1)
print(my_list)
# Lists in action
my_list = [10, 1, 8, 3, 5]
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)
# PROGRAM-12
# Sorting a  LIST
my_list = [8, 10, 6, 2, 4]  # list to sort
for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.
# ex;
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
# the inner life of lists
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)
# The in and not in operators
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
# PROGRAM-13
# Lists - some simple programs
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)
# PROGRAM-14
# Lists - some simple programs
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")
# PROGRAM-15
# Lists in lists: two-dimensional arrays - continued
EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
print(board)


# PROGRAM-16
# Positional parameter passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")


# PROGRAM-17
# Effects and results: lists and functions - continued
def strange_list_fun(n):
    strange_list = []
    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list


print(strange_list_fun(5))


# PROGRAM-18
# Swaplist first element and last element
def swapList(newone):
    size = len(newone)
    temp = newone[0]
    # 1 2 3 4 6 (5-1=4)
    newone[0] = newone[size - 1]
    newone[size - 1] = temp
    print("Here is the ouput after swapping")
    print("please check below")
    return newone


newone = [1, 2, 3, 4, 6]
print(swapList(newone))
# PROGRAM-19
# largest among three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
largest_number = max(number1, number2, number3)
print("The largest number is:", largest_number)
# PROGRAM-20
# Jasmine plant sampletest
name = input("enter flower name:")
if name == "Jasmine":
    print("Yes - Jasmine is the best plant ever!")
elif name == "Jasmine":
    print("No, I want a big Jasmine!")
else:
    print("Jasmine! Not", name + "!")
# PROGRAM-21
# Swapping three elements in a List
def swapPositions(lst, pos1, pos2, pos3):
    lst[pos1], lst[pos2], lst[pos3] = lst[pos3], lst[pos1], lst[pos2]
    return lst
List = [23, 45, 64, 72, 95, 257]
pos0, pos3, pos4 = 0, 3, 4
print(swapPositions(List, pos0, pos3, pos4))
###Thank You

