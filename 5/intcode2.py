program = [3,225,1,225,6,6,1100,1,238,225,104,0,1002,114,19,224,1001,224,-646,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1101,40,62,225,1101,60,38,225,1101,30,29,225,2,195,148,224,1001,224,-40,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1001,143,40,224,101,-125,224,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,101,29,139,224,1001,224,-99,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,14,34,225,102,57,39,224,101,-3420,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1101,70,40,225,1102,85,69,225,1102,94,5,225,1,36,43,224,101,-92,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1102,94,24,224,1001,224,-2256,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1102,8,13,225,1101,36,65,224,1001,224,-101,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,677,226,224,1002,223,2,223,1006,224,329,1001,223,1,223,1108,226,226,224,1002,223,2,223,1005,224,344,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,359,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,374,101,1,223,223,1107,226,226,224,1002,223,2,223,1005,224,389,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,404,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,108,677,226,224,1002,223,2,223,1006,224,434,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,449,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,479,101,1,223,223,7,677,677,224,102,2,223,223,1005,224,494,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,509,101,1,223,223,107,677,226,224,1002,223,2,223,1005,224,524,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,554,1001,223,1,223,8,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,584,1001,223,1,223,1008,677,677,224,102,2,223,223,1005,224,599,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,614,101,1,223,223,1107,677,226,224,1002,223,2,223,1006,224,629,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,659,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226]

# Tests, commented out

# program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]

# program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

# program = [1,1,1,4,99,5,6,0,99]

# program= [1,0,0,0,99]

# program = [1002,4,3,4,33]

# program = [1101,100,-1,4,0]

# program = [3,9,8,9,10,9,4,9,99,-1,8]

# program = [3,9,7,9,10,9,4,9,99,-1,8]

# program = [3,3,1108,-1,8,3,4,3,99]

# program = [3,3,1107,-1,8,3,4,3,99]

# program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]

# program =[3,3,1105,-1,9,1101,0,0,12,4,12,99,1]


def op_add(index, program, modes, *parameters):
    values = []
    values.append(program[parameters[0]] if modes[0] == '0' else parameters[0])
    values.append(program[parameters[1]] if modes[1] == '0' else parameters[1])

    program[parameters[2]] = sum([val for val in values])

    index += len(parameters) + 1

    return index, program

def op_mult(index, program, modes, *parameters):
    values = []
    values.append(program[parameters[0]] if modes[0] == '0' else parameters[0])
    values.append(program[parameters[1]] if modes[1] == '0' else parameters[1])

    program[parameters[2]] = values[0] * values[1]

    index += len(parameters) + 1

    return index, program

def op_input(index, program, modes, parameter):
    i = input('input a value: ')
    program[parameter] = int(i)

    index += 2 # len(parameter + 1)

    return index, program

def op_output(index, program, modes, parameter):
    val = program[parameter] if modes[0] == '0' else parameter
    print('the value at', parameter, 'is', val)

    index += 2 #len(parameter + 1)

    return index, program

def op_jit(index, program, modes, *parameters):
    check_value = program[parameters[0]] if modes[0] == '0' else parameters[0]
    if check_value != 0:
        index = program[parameters[1]] if modes[1] == '0' else parameters[1]
    else:
        index += len(parameters) + 1
    
    return index, program

def op_jif(index, program, modes, *parameters):
    check_value = program[parameters[0]] if modes[0] == '0' else parameters[0]
    if check_value == 0:
        index = program[parameters[1]] if modes[1] == '0' else parameters[1]
    else:
        index += len(parameters) + 1

    return index, program

def op_lt(index, program, modes, *parameters):
    values = []
    values.append(program[parameters[0]] if modes[0] == '0' else parameters[0])
    values.append(program[parameters[1]] if modes[1] == '0' else parameters[1])

    program[parameters[2]] = 1 if values[0] < values[1] else 0

    index += len(parameters) + 1

    return index, program

def op_equal(index, program, modes, *parameters):
    values = []
    values.append(program[parameters[0]] if modes[0] == '0' else parameters[0])
    values.append(program[parameters[1]] if modes[1] == '0' else parameters[1])

    program[parameters[2]] = 1 if values[0] == values [1] else 0

    index += len(parameters) + 1

    return index, program


opcode = 0
index = 0

opcode = program[index]

while int(opcode) != 99:

    opcode = str(opcode)

    jump = True

    if opcode.endswith('1'):
        param_count = 3
        op = op_add

    elif opcode.endswith('2'):
        param_count = 3
        op = op_mult

    elif opcode.endswith('3'):
        param_count = 1
        op = op_input

    elif opcode.endswith('4'):
        param_count = 1
        op = op_output

    elif opcode.endswith('5'):
        param_count = 2
        op = op_jit

    elif opcode.endswith('6'):
        param_count = 2
        op = op_jif

    elif opcode.endswith('7'):
        param_count = 3
        op = op_lt

    elif opcode.endswith('8'):
        param_count = 3
        op = op_equal

    else:
        print('some kind of error')
        break

    opcode = opcode.rjust(param_count + 2, '0')

    modes = opcode[-3::-1]
 
    params = [program[index + c] for c in range(1, param_count + 1)]

#    print('running', op, 'with opcode', opcode, 'and parameters', *params, 'in modes', modes)
#    print(program)
#    input()

    index, program = op(index, program, modes, *params)
#    print(program)

    opcode = program[index]

# print(program)
