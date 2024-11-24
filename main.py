import time
from os import times

program = \
    [
        ". A set 1",
        ". B set 0",
        ". Fib set 0",
        "math. Fib sum A B",
        ". B set A",
        ". A set Fib",
        ". Fib show",
        ". goto 3"
    ]
for var in program:
    program[program.index(var)] = program[program.index(var)].split(" ")

var = {}

def param(variable):
    if variable in var:
        return var[variable]
    else:
        return variable

print("program est de type: " + str(type(program)))
print("var est de type: " + str(type(var)) + "\n\n")



line = -1
while line != len(program)-1:
    line +=1
    #print(line)
    time.sleep(0.1)

    #"." for basics function
    if program[line][0] == ".":
        if program[line][1] == "goto":
            line = int(param(program[line][2])) -1

        elif program[line][2] == "set":
            var[program[line][1]] = param(program[line][3])


        elif program[line][2] == "show":
            print(param(program[line][1]))


    #math operation function
    if program[line][0] == "math.":
        if program[line][2] == "sum":
            #print(param(program[line][3]) + "-num1")
            #print(param(program[line][4]) + "-num2")
            var[program[line][1]] = int(param(program[line][3])) + int(param(program[line][4]))

        elif program[line][2] == "diff":
            var[program[line][1]] = int(param(program[line][3])) - int(param(program[line][4]))

        elif program[line][2] == "pdct":
            var[program[line][1]] = int(param(program[line][3])) * int(param(program[line][4]))

        elif program[line][2] == "quot":
            var[program[line][1]] = int(param(program[line][3])) / int(param(program[line][4]))

        elif program[line][3] == "ecquot":
            var[program[line][1]] = int(param(program[line][4])) // int(program[line][5])
            var[program[line][2]] = int(param(program[line][4])) % int(program[line][5])

        elif program[line][2] == "ecquot":
            var[program[line][1]] = int(param(program[line][3])) // int(param(program[line][4]))

        elif program[line][2] == "rest":
            var[program[line][1]] = int(param(program[line][3])) % int(param(program[line][4]))





exit(line)
