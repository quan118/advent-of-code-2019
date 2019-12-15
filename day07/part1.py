HALT = 99
ADD = 1
MULT = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
POSITION_MODE = 0
IMMEDIATE_MODE = 1

SYSTEM_ID = 5

def get_value(mem, pos, mode):
  if mode == POSITION_MODE:
    return mem[mem[pos]]
  elif mode == IMMEDIATE_MODE:
    return mem[pos]
  return None

def execute(program, inputs):
  input_counter = 0
  counter = 0
  output = None
  while counter < len(program) and program[counter] != HALT:
    instruction = str(program[counter]).rjust(5, '0')
    opcode = int(instruction[3:])
    if opcode == ADD:
      val1 = get_value(program, counter+1, int(instruction[2]))
      val2 = get_value(program, counter+2, int(instruction[1]))
      program[program[counter+3]] = val1 + val2
      counter += 4
    elif opcode == MULT:
      val1 = get_value(program, counter+1, int(instruction[2]))
      val2 = get_value(program, counter+2, int(instruction[1]))
      program[program[counter+3]] = val1 * val2
      counter += 4
    elif opcode == INPUT:
      if input_counter >= len(inputs):
        print('ERROR: input_counter > inputs')
        break
      program[program[counter+1]] = inputs[input_counter]
      counter += 2
      input_counter += 1
    elif opcode == OUTPUT:
      output = get_value(program, counter+1, int(instruction[2]))
      # print("output: %d" % (output))
      counter += 2
    elif opcode == JUMP_IF_TRUE:
      val1 = get_value(program, counter+1, int(instruction[2]))
      val2 = get_value(program, counter+2, int(instruction[1]))
      if val1 != 0:
        counter = val2
      else:
        counter += 3
    elif opcode == JUMP_IF_FALSE:
      val1 = get_value(program, counter+1, int(instruction[2]))
      val2 = get_value(program, counter+2, int(instruction[1]))
      if val1 == 0:
        counter = val2
      else:
        counter += 3
    elif opcode == LESS_THAN:
      val1 = get_value(program, counter+1, int(instruction[2]))
      val2 = get_value(program, counter+2, int(instruction[1]))
      if val1 < val2:
        program[program[counter+3]] = 1
      else:
        program[program[counter+3]] = 0
      counter += 4
    elif opcode == EQUALS:
      val1 = get_value(program, counter+1, int(instruction[2]))
      val2 = get_value(program, counter+2, int(instruction[1]))
      if val1 == val2:
        program[program[counter+3]] = 1
      else:
        program[program[counter+3]] = 0
      counter += 4
    else:
      print("OPCODE IS INVALID")
      print("opcode: %d counter: %d" % (opcode, counter))
      break
  return output

def advance(settings):
  settings_len = len(settings)
  if settings_len == 2:
    if settings[0] < settings[1]:
      return [settings[1], settings[0]]
    return None

  sub_advance = advance(settings[1:])
  if sub_advance == None:
    if settings[0] > settings[1]:
      return None

    pos = settings_len - 1
    for i in range(1, settings_len - 1):
      if settings[0] < settings[i] and settings[0] > settings[i+1]:
        pos = i
        break
 
    settings[0], settings[pos] = settings[pos], settings[0]

    for i in range(0, (settings_len - 2)//2+1):
      settings[1+i], settings[-1-i] = settings[-1-i], settings[1+i]
    return settings

  return [settings[0]] + sub_advance

if __name__=="__main__":
  f = open("input.txt", "r")
  program = [int(n) for n in f.readline().split(",")]
  f.close()
  n_amplifiers = 5
  max_thruster = 0
  settings = [4,3,2,1,0]

  while settings != None:
    output = 0
    for i in range(n_amplifiers):
      output = execute(program, [settings[i], output])
      print(output)
    max_thruster = max(max_thruster, output)
    settings = advance(settings)
  
  print("max thruster: %d" % (max_thruster))

  # tmp = [0,1,2,3]
  # while (tmp):
  #   tmp = advance(tmp)
  #   print(tmp)
