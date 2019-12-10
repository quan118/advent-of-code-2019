WIDE, TALL = 25, 6
if __name__=="__main__":
  f = open("input.txt", "r")
  program = [int(n) for n in f.readline().strip("\n")]
  f.close()
  min_zeros = 99999999
  counters = [0, 0, 0]
  PIXELS_PER_LAYER = WIDE * TALL
  program_idx = 0
  result = None
  while program_idx < len(program):
    for i in range(PIXELS_PER_LAYER):
      val = program[program_idx + i]
      if val in [0, 1, 2]:
        counters[val] += 1

    if counters[0] < min_zeros:
      min_zeros = counters[0]
      result = counters[1] * counters[2]

    program_idx += PIXELS_PER_LAYER
    counters = [0, 0, 0]
  print(result)

