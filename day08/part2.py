WIDE, TALL = 25, 6
PIXELS_PER_LAYER = WIDE * TALL
BLACK, WHITE, TRANSPARENT = 0, 1, 2

def get_color(program, i):
  while i < len(program) and program[i] == TRANSPARENT:
    i += PIXELS_PER_LAYER
  return program[i]

def display(image):
  i = 0
  while i < PIXELS_PER_LAYER:
    print(image[i:WIDE+i])
    i += WIDE


if __name__=="__main__":
  f = open("input.txt", "r")
  program = [int(n) for n in f.readline().strip("\n")]
  f.close()

  final_image = []

  for i in range(PIXELS_PER_LAYER):
    final_image.append(get_color(program, i))
  display(final_image)