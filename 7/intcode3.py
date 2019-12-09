import itertools

program = [3,8,1001,8,10,8,105,1,0,0,21,34,59,76,101,114,195,276,357,438,99999,3,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,102,4,9,9,101,2,9,9,102,4,9,9,1001,9,3,9,102,2,9,9,4,9,99,3,9,101,4,9,9,102,5,9,9,101,5,9,9,4,9,99,3,9,102,2,9,9,1001,9,4,9,102,4,9,9,1001,9,4,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99]

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
    global phase_setting_used
    global input_sig_used
    if not phase_setting_used:
        phase_setting_used = True
        i = phase_setting
    elif not input_sig_used:
        input_sig_used = True
        i = input_sig
    else:
        i = input('input a value: ')
    program[parameter] = int(i)

    index += 2 # len(parameter + 1)

    return index, program

def op_output(index, program, modes, parameter):
    val = program[parameter] if modes[0] == '0' else parameter
    print(val)

    global output
    output = val

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

def run_intcode(program, ps, isg):
    opcode = 0
    index = 0

    global phase_setting_used 
    phase_setting_used = False
    global input_sig_used 
    input_sig_used = False

    global phase_setting
    global input_sig

    global output
    output = None

    phase_setting = ps
    input_sig = isg

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

    return output

settings = list(itertools.permutations([0,1,2,3,4]))

thruster_sigs = []

for setting_list in settings:
    thrust = run_intcode(program, setting_list[4], 
            run_intcode(program, setting_list[3], 
            run_intcode(program, setting_list[2],
            run_intcode(program, setting_list[1],
            run_intcode(program, setting_list[0], 0)))))
    thruster_sigs.append(thrust)

print(thruster_sigs)
print(max(thruster_sigs))
