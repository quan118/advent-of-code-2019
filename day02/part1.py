
if __name__=="__main__":
  f = open("input.txt", "r")
  line = f.readline()
  f.close()
  nums = [int(n) for n in line.split(',')]
  # print(nums)
  nums[1] = 12
  nums[2] = 2
  i = 0
  while i < len(nums) - 3 and nums[i] in [1, 2]:
    if nums[i] == 1:
      nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
    elif nums[i] == 2:
      nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
    i += 4
  print(nums[0])