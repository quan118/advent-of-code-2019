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

def get_value(mem, pos, mode):
  if mode == POSITION_MODE:
    return mem[mem[pos]]
  elif mode == IMMEDIATE_MODE:
    return mem[pos]
  return None

def execute(mem, mem_idx, inputs):
  output = []
  input_idx = 0
  halt = True
  while mem_idx < len(mem) and mem[mem_idx] != HALT:
    instruction = str(mem[mem_idx]).rjust(5, '0')
    opcode = int(instruction[3:])
    if opcode == ADD:
      val1 = get_value(mem, mem_idx+1, int(instruction[2]))
      val2 = get_value(mem, mem_idx+2, int(instruction[1]))
      mem[mem[mem_idx+3]] = val1 + val2
      mem_idx += 4
    elif opcode == MULT:
      val1 = get_value(mem, mem_idx+1, int(instruction[2]))
      val2 = get_value(mem, mem_idx+2, int(instruction[1]))
      mem[mem[mem_idx+3]] = val1 * val2
      mem_idx += 4
    elif opcode == INPUT:
      if input_idx >= len(inputs):
        halt = False
        break
      mem[mem[mem_idx+1]] = inputs[input_idx]
      mem_idx += 2
      input_idx += 1
    elif opcode == OUTPUT:
      val1 = get_value(mem, mem_idx+1, int(instruction[2]))
      output.append(val1)
      mem_idx += 2
    elif opcode == JUMP_IF_TRUE:
      val1 = get_value(mem, mem_idx+1, int(instruction[2]))
      val2 = get_value(mem, mem_idx+2, int(instruction[1]))
      if val1 != 0:
        mem_idx = val2
      else:
        mem_idx += 3
    elif opcode == JUMP_IF_FALSE:
      val1 = get_value(mem, mem_idx+1, int(instruction[2]))
      val2 = get_value(mem, mem_idx+2, int(instruction[1]))
      if val1 == 0:
        mem_idx = val2
      else:
        mem_idx += 3
    elif opcode == LESS_THAN:
      val1 = get_value(mem, mem_idx+1, int(instruction[2]))
      val2 = get_value(mem, mem_idx+2, int(instruction[1]))
      if val1 < val2:
        mem[mem[mem_idx+3]] = 1
      else:
        mem[mem[mem_idx+3]] = 0
      mem_idx += 4
    elif opcode == EQUALS:
      val1 = get_value(mem, mem_idx+1, int(instruction[2]))
      val2 = get_value(mem, mem_idx+2, int(instruction[1]))
      if val1 == val2:
        mem[mem[mem_idx+3]] = 1
      else:
        mem[mem[mem_idx+3]] = 0
      mem_idx += 4
    else:
      print("OPCODE IS INVALID")
      print("opcode: %d mem_idx: %d" % (opcode, mem_idx))
      break
  
  return (mem, mem_idx, output, halt)

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
  settings = [5,6,7,8,9]
  critical_error = False
  while settings != None:
    mems = []
    mems_idx = []
    inputs = []
    for i in range(0, n_amplifiers):
      mems.append(program[:])
      mems_idx.append(0)
      inputs.append([])
    first_loop = True
    output = 0
    halts = [False] * n_amplifiers

    while halts[-1] == False:
      for i in range(n_amplifiers):
        if first_loop:
          inputs[i] = [settings[i], output]
        else:
          inputs[i] = [output]
        mems[i], mems_idx[i], outputs, halts[i] = execute(mems[i], mems_idx[i], inputs[i])

        if len(outputs) == 0 or outputs[0] == None:
          print('Critical error')
          critical_error = True
          break
        output = outputs[0]
        if len(outputs) > 1:
          print("i: %d" % (i))
          print(outputs)

      first_loop = False
      if critical_error:
        break
      if halts[-1] == True:
        max_thruster = max(max_thruster, output)

    if critical_error:
      break

    settings = advance(settings)
  
  print("max thruster: %d" % (max_thruster))

