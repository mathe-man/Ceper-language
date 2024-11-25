import time

fibonaciProgram = \
    [
        ". A set 1",
        ". B set 0",
        ". Fib set 0",
        "math. Fib sum A B",
        ". B set A",
        ". A set Fib",
        "Fib show",
        "program. sleep 0.6",
        "program. goto 3"
    ]

aProgram = \
    [
        ". Moy set 0",
        ". MoyDiv set 0",
        ". note input",
        ". note show",
        "math. Moy sum Moy note",
        ". MoyDiv quot Moy 10",
        ". MoyDiv show",
        "caca",
        "program. goto 2"

    ]


program = fibonaciProgram
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

    #"." for basics function
    if program[line][0] == ".":

        if program[line][2] == "set":
            var[program[line][1]] = param(program[line][3])


        elif program[line][2] == "show":
            print(param(program[line][1]))

        elif program[line][2] == "input":
            var[program[line][1]] = input()


    #math operation function
    elif program[line][0] == "math.":
        if program[line][2] == "sum":
            #print(param(program[line][3]) + "-num1")
            #print(param(program[line][4]) + "-num2")
            var[program[line][1]] = float(param(program[line][3])) + float(param(program[line][4]))

        elif program[line][2] == "diff":
            var[program[line][1]] = float(param(program[line][3])) - float(param(program[line][4]))

        elif program[line][2] == "pdct":
            var[program[line][1]] = float(param(program[line][3])) * float(param(program[line][4]))

        elif program[line][2] == "quot":
            var[program[line][1]] = float(param(program[line][3])) / float(param(program[line][4]))

        elif program[line][3] == "ecquot":
            var[program[line][1]] = float(param(program[line][4])) // float(program[line][5])
            var[program[line][2]] = float(param(program[line][4])) % float(program[line][5])

        elif program[line][2] == "ecquot":
            var[program[line][1]] = float(param(program[line][3])) // float(param(program[line][4]))

        elif program[line][2] == "rest":
            var[program[line][1]] = float(param(program[line][3])) % float(param(program[line][4]))


    #Information and function about the currently running program
    elif program[line][0] == "program.":

        if program[line][1] == "end":
            print("program ending...")
            break

        elif program[line][1] == "goto":
            line = int(param(program[line][2])) -1

        #elif program[line][1] == ""

        elif program[line][2] == "line":
            var[program[line][1]] = line

        elif program[line][1] == "sleep":
            time.sleep(float(param(program[line][2])))


    else:
        print(f"\033[31mError! Line {line + 1}: {program[line]}\033[0m")
        break

exit(line)
