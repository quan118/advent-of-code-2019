def is_valid(n):
  digits = str(n)
  has_double = False
  decrease = False
  for i in range(len(digits)-1):
    if digits[i] > digits[i+1]:
      decrease = True
      break
    if digits[i] == digits[i+1]:
      has_double = True

  return not decrease and has_double 


if __name__=="__main__":
  cnt = 0
  for n in range(235741, 706949):
    if is_valid(n):
      cnt += 1
  print(cnt)
