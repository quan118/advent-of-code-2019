def is_valid(n):
  digits = str(n)
  has_double = False
  decrease = False
  found_group = False
  group_count = 0
  for i in range(len(digits)-1):
    if digits[i] > digits[i+1]:
      decrease = True
      break
    if has_double:
      continue
    if digits[i] == digits[i+1]:
      if not found_group:
        group_count = 2
      else:
        group_count += 1
      found_group = True
    else:
      if found_group == True and group_count == 2 and has_double == False:
        has_double = True
      found_group = False
      group_count = 0
    
  if found_group == True and group_count == 2 and has_double == False:
    has_double = True

  return not decrease and has_double 


if __name__=="__main__":
  cnt = 0
  for n in range(235741, 706949):
    if is_valid(n):
      cnt += 1
  print(cnt)
  # print(is_valid(122223))
  # print(is_valid(123444))
  # print(is_valid(111122))