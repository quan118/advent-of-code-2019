HALT = 99
ADD = 1
MULT = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
ADJUST_RELATIVE_BASE = 9
POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2

def pick(mem, extra_mem, pos):
  if 0 <= pos and pos < len(mem):
    return mem[pos]
  if pos >= len(mem) and pos in extra_mem:
    return extra_mem[pos]
  return 0

def put(mem, extra_mem, pos, value):
  if 0 <= pos and pos < len(mem):
    mem[pos] = value
  elif pos >= len(mem):
    extra_mem[pos] = value

def get_value(mem, extra_mem, base, pos, mode):
  if mode == POSITION_MODE:
    idx = pick(mem, extra_mem, pos)
    return pick(mem, extra_mem, idx)
  elif mode == IMMEDIATE_MODE:
    return pick(mem, extra_mem, pos)
  elif mode == RELATIVE_MODE:
    offset = pick(mem, extra_mem, pos)
    return pick(mem, extra_mem, base+offset)
  return None

def set_value(mem, extra_mem, base, pos, mode, value):
  if mode == POSITION_MODE:
    put(mem, extra_mem, pos, value)
    return True
  elif mode == IMMEDIATE_MODE:
    print('FATAL ERROR')
    return False
  elif mode == RELATIVE_MODE:
    put(mem, extra_mem, base+pos, value)
    return True
  else:
    return False

def execute(mem, extra_mem, mem_idx, base, inputs):
  output = []
  input_idx = 0
  halt = True
  fatal_error = False
  ins = get_value(mem, extra_mem, base, mem_idx, IMMEDIATE_MODE)

  while ins != HALT:
    instruction = str(ins).rjust(5, '0')
    opcode = int(instruction[3:])
    if opcode == ADD:
      val1 = get_value(mem, extra_mem, base, mem_idx+1, int(instruction[2]))
      val2 = get_value(mem, extra_mem, base, mem_idx+2, int(instruction[1]))
      addr = get_value(mem, extra_mem, base, mem_idx+3, IMMEDIATE_MODE)
      result = set_value(mem, extra_mem, base, addr, int(instruction[0]), val1 + val2)
      if not result:
        halt, fatal_error = False, True
        break
      mem_idx += 4
    elif opcode == MULT:
      val1 = get_value(mem, extra_mem, base, mem_idx+1, int(instruction[2]))
      val2 = get_value(mem, extra_mem, base, mem_idx+2, int(instruction[1]))
      addr = get_value(mem, extra_mem, base, mem_idx+3, IMMEDIATE_MODE)
      result = set_value(mem, extra_mem, base, addr, int(instruction[0]), val1 * val2)
      if not result:
        halt, fatal_error = False, True
        break
      mem_idx += 4
    elif opcode == INPUT:
      if input_idx >= len(inputs):
        halt = False
        break
      addr = get_value(mem, extra_mem, base, mem_idx+1, IMMEDIATE_MODE)
      result = set_value(mem, extra_mem, base, addr, int(instruction[2]), inputs[input_idx])
      if not result:
        halt, fatal_error = False, True
        break
      mem_idx += 2
      input_idx += 1
    elif opcode == OUTPUT:
      val1 = get_value(mem, extra_mem, base, mem_idx+1, int(instruction[2]))
      output.append(val1)
      mem_idx += 2
    elif opcode == JUMP_IF_TRUE:
      val1 = get_value(mem, extra_mem, base, mem_idx+1, int(instruction[2]))
      val2 = get_value(mem, extra_mem, base, mem_idx+2, int(instruction[1]))
      if val1 != 0:
        mem_idx = val2
      else:
        mem_idx += 3
    elif opcode == JUMP_IF_FALSE:
      val1 = get_value(mem, extra_mem, base, mem_idx+1, int(instruction[2]))
      val2 = get_value(mem, extra_mem, base, mem_idx+2, int(instruction[1]))
      if val1 == 0:
        mem_idx = val2
      else:
        mem_idx += 3
    elif opcode == LESS_THAN:
      val1 = get_value(mem, extra_mem, base, mem_idx+1, int(instruction[2]))
      val2 = get_value(mem, extra_mem, base, mem_idx+2, int(instruction[1]))
      addr = get_value(mem, extra_mem, base, mem_idx+3, IMMEDIATE_MODE)
      if val1 < val2:
        result = set_value(mem, extra_mem, base, addr, int(instruction[0]), 1)
      else:
        result = set_value(mem, extra_mem, base, addr, int(instruction[0]), 0)
      if not result:
        halt, fatal_error = False, True
        break
      mem_idx += 4
    elif opcode == EQUALS:
      val1 = get_value(mem, extra_mem, base, mem_idx+1, int(instruction[2]))
      val2 = get_value(mem, extra_mem, base, mem_idx+2, int(instruction[1]))
      addr = get_value(mem, extra_mem, base, mem_idx+3, IMMEDIATE_MODE)
      if val1 == val2:
        result = set_value(mem, extra_mem, base, addr, int(instruction[0]), 1)
      else:
        result = set_value(mem, extra_mem, base, addr, int(instruction[0]), 0)
      if not result:
        halt, fatal_error = False, True
        break
      mem_idx += 4
    elif opcode == ADJUST_RELATIVE_BASE:
      base += get_value(mem, extra_mem, base, mem_idx+1, int(instruction[2]))
      mem_idx += 2
    else:
      print("OPCODE IS INVALID")
      print("opcode: %d mem_idx: %d" % (opcode, mem_idx))
      halt, fatal_error = False, True
      break
    ins = get_value(mem, extra_mem, base, mem_idx, IMMEDIATE_MODE)
  return (mem, extra_mem, mem_idx, base, output, halt, fatal_error)

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

  mem, extra_mem, mem_idx, base, output, halt, fatal_error = execute(program, {}, 0, 0, [1])

  if halt and not fatal_error:
    print('FINISHED')
    print(output)
  else:
    print('FINISHED WITH ERROR'); 

