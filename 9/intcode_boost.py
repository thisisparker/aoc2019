program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
program = [1102,34915192,34915192,7,4,7,99,0]
program = [104,1125899906842624,99]


with open('program.txt') as f:
    program = [int(x.strip()) for x in f.read().split(',')]

def load_mode(program, mode, parameter):
    try:
        if mode == '0':
            return program[parameter]
        elif mode == '1':
            return parameter
        elif mode == '2':
            return program[parameter + relative]
    except IndexError:
        extension = paramter + relative if mode == '2' else parameter
        extension -= len(program)
        program.extend([0] * extension)
        return 0

def write_mode(program, mode, parameter, index, value):
    global relative
    if mode == '0':
            new_index = parameter
    elif mode == '2':
            new_index = parameter + relative
    
    if new_index > len(program) - 1:
        extension = new_index - len(program) + 1
        program.extend([0] * extension)

    program[new_index] = value
        
    return program


def op_add(index, program, modes, *parameters):
    values = []
    values.append(load_mode(program, modes[0], parameters[0]))
    values.append(load_mode(program, modes[1], parameters[1]))

    program = write_mode(program, modes[2], parameters[2], index, 
                         sum([val for val in values]))

    index += len(parameters) + 1

    return index, program

def op_mult(index, program, modes, *parameters):
    values = []
    values.append(load_mode(program, modes[0], parameters[0]))
    values.append(load_mode(program, modes[1], parameters[1]))

    program = write_mode(program, modes[2], parameters[2], index, values[0] * values[1])

    index += len(parameters) + 1

    return index, program

def op_input(index, program, modes, parameter):
#     global phase_setting_used
#     global input_sig_used
#     if not phase_setting_used:
#         phase_setting_used = True
#         i = phase_setting
#     elif not input_sig_used:
#         input_sig_used = True
#         i = input_sig
#     else:
    i = input('input a value: ')
    program = write_mode(program, modes[0], parameter, index, int(i))

    index += 2 # len(parameter + 1)

    return index, program

def op_output(index, program, modes, parameter):
    val = load_mode(program, modes[0], parameter)
    print(val)

    index += 2 #len(parameter + 1)

    return index, program

def op_jit(index, program, modes, *parameters):
    check_value = load_mode(program, modes[0], parameters[0])
    if check_value != 0:
        index = load_mode(program, modes[1], parameters[1])
    else:
        index += len(parameters) + 1
    
    return index, program

def op_jif(index, program, modes, *parameters):
    check_value = load_mode(program, modes[0], parameters[0])
    if check_value == 0:
        index = load_mode(program, modes[1], parameters[1])
    else:
        index += len(parameters) + 1

    return index, program

def op_lt(index, program, modes, *parameters):
    values = []
    values.append(load_mode(program, modes[0], parameters[0]))
    values.append(load_mode(program, modes[1], parameters[1]))

    program = write_mode(program, modes[2], parameters[2], index,
                         1 if values[0] < values[1] else 0)

    index += len(parameters) + 1

    return index, program

def op_equal(index, program, modes, *parameters):
    values = []
    values.append(load_mode(program, modes[0], parameters[0]))
    values.append(load_mode(program, modes[1], parameters[1]))

    program = write_mode(program, modes[2], parameters[2], index,
                         1 if values[0] == values [1] else 0)

    index += len(parameters) + 1

    return index, program

def op_relative(index, program, modes, parameter):
    global relative
    relative += load_mode(program, modes[0], parameter)

    index += 2

    return index, program

def run_intcode(program): #, ps, isg):
    opcode = 0
    index = 0
    global relative
    relative = 0

#    global phase_setting_used 
#    phase_setting_used = False
#    global input_sig_used 
#    input_sig_used = False
#
#    global phase_setting
#    global input_sig
#
#    global output
#    output = None
#
#    phase_setting = ps
#    input_sig = isg

    opcode = program[index]

    while int(opcode) != 99:

        opcode = str(opcode)

        if opcode == '99':
            break

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

        elif opcode.endswith('9'):
            param_count = 1
            op = op_relative

        else:
            print('some kind of error')
            break

        opcode = opcode.rjust(param_count + 2, '0')

        modes = opcode[-3::-1]
 
        params = [program[index + c] for c in range(1, param_count + 1)]

#        print('running', op, 'with opcode', opcode, 'and parameters', *params, 'in modes', modes, 'relative value is', relative)
#        print(program)

        index, program = op(index, program, modes, *params)
#        print(program)

        opcode = program[index]

    print(program)

run_intcode(program)
