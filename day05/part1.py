HALT = 99
ADD = 1
MULT = 2
INPUT = 3
OUTPUT = 4
POSITION_MODE = 0
IMMEDIATE_MODE = 1

SYSTEM_ID = 1

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
      program[program[counter+1]] = SYSTEM_ID # hard coded input from user
      counter += 2
    elif opcode == OUTPUT:
      val1 = get_value(program, counter+1, int(instruction[2]))
      print("output: %d" % (val1))
      counter += 2
    else:
      print("OPCODE IS INVALID")
      print("opcode: %d counter: %d" % (opcode, counter))
      break
