def calculate_fuel_required(mass):
  return mass // 3 - 2

if __name__ == "__main__":
  f = open("input.txt", "r")
  total = 0
  for line in f:
    tmp = calculate_fuel_required(int(line))
    while tmp > 0:
      total += tmp
      tmp = calculate_fuel_required(tmp)

  print(total)
