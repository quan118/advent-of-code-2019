
def run(nums, noun, verb):
  nums[1] = noun
  nums[2] = verb
  i = 0
  while i < len(nums) - 3 and nums[i] in [1, 2]:
    if nums[i] == 1:
      nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
    elif nums[i] == 2:
      nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
    i += 4
  return nums[0]

if __name__=="__main__":
  f = open("input.txt", "r")
  line = f.readline()
  f.close()
  nums = [int(n) for n in line.split(',')]
  result = None
  for noun in range(100):
    for verb in range(100):
      numbers = list(nums)
      if run(numbers, noun, verb) == 19690720:
        result = 100 * noun + verb
        break
    if result != None:
      break
  print(result)