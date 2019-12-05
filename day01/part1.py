def calculate_fuel_required(mass):
  return mass // 3 - 2

if __name__ == "__main__":
  f = open("input.txt", "r")
  total = 0
  for line in f:
    total += calculate_fuel_required(int(line))
  print(total)
