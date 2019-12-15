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

if __name__=="__main__":
  f = open("input.txt", "r")
  program = [int(n) for n in f.readline().split(",")]
  f.close()
  counter = 0
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
      program[program[counter+1]] = SYSTEM_ID
      counter += 2
    elif opcode == OUTPUT:
      val1 = get_value(program, counter+1, int(instruction[2]))
      print("output: %d" % (val1))
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
