def dist(x, y):
  return abs(x) + abs(y)

def count_steps(l):
  return abs(l[0] - l[2]) + abs(l[1] - l[3])

def inside(x, y, l):
  x1, y1, x2, y2 = l
  if x1 <= x and x <= x2 and y1 <= y and y <= y2:
    return True
  return False

def handle_overlap(u1, u2, u3, u4, v):
  if u2 < u3 or u4 < u1:
    return None
  if u3 <= u1 and u4 <= u2:
    dist1 = dist(u1, v)
    dist2 = dist(u4, v)
    if dist1 < dist2:
      return (u1, v)
    return (u4, v)
  elif u3 <= u1 and u2 <= u4:
    dist1 = dist(u1, v)
    dist2 = dist(u2, v)
    if dist1 < dist2:
      return (u1, v)
    return (u2, v)
  elif u1 <= u3 and u2 <= u4:
    dist1 = dist(u3, v)
    dist2 = dist(u2, v)
    if dist1 < dist2:
      return (u3, v)
    return (u2, v)
  elif u1 <= u3 and u4 <= u2:
    dist1 = dist(u3, v)
    dist2 = dist(u4, v)
    if dist1 < dist2:
      return (u3, v)
    return (u4, v)

def sort_line(l):
  x1, y1, x2, y2 = l
  if x1 == x2:
    if y1 < y2:
      return (x1, y1, x2, y2)
    else:
      return (x2, y2, x1, y1)
  elif x1 < x2:
    return (x1, y1, x2, y2)
  else:
    return (x2, y2, x1, y1)

def get_intersection(l1, l2):
  l3 = sort_line(l1)
  l4 = sort_line(l2)
  x1, y1, x2, y2 = l3
  x3, y3, x4, y4 = l4
  x = None
  y = None
  if x1 == x2 and y3 == y4:
    x, y = x1, y3
  elif x3 == x4 and y1 == y2:
    x, y = x3, y1
  elif x1 == x2 and x3 == x4:
    if x1 != x3:
      return None
    result = handle_overlap(y1, y2, y3, y4, x1)
    if result != None:
      return (result[1], result[0])
    return result
  elif y1 == y2 and y3 == y4:
    if y1 != y3:
      return None
    result = handle_overlap(x1, x2, x3, x4, y1)
    return result

  if x != None and y != None:
    if inside(x, y, l3) and inside(x, y, l4):
      return (x, y)
  return None

def get_paths(input):
  x, y = 0, 0
  output = []
  steps = input.split(",")
  x1, y1 = x, y
  for step in steps:
    direction = step[0]
    distant = int(step[1:])
    if direction == 'U':
      y1 = y + distant
    elif direction == 'D':
      y1 = y - distant
    elif direction == 'R':
      x1 = x + distant
    elif direction == 'L':
      x1 = x - distant
    output.append((x, y, x1, y1))
    x, y = x1, y1
  return output

if __name__=="__main__":
  f = open("input.txt", "r")
  line1 = f.readline()
  line2 = f.readline()

  paths1 = get_paths(line1)
  paths2 = get_paths(line2)

  min_steps = 9999999999
  skip_first_paths = True
  stop = False
  cnt_steps = 0
  p1_steps = 0
  for p1 in paths1:
    p1_steps += count_steps(p1)
    cnt_steps = p1_steps
    for p2 in paths2:
      cnt_steps += count_steps(p2)
      if skip_first_paths:
        skip_first_paths = False
        continue
      intersection = get_intersection(p1, p2)
      if intersection != None:
        cnt_steps -= count_steps(p1)
        cnt_steps -= count_steps(p2)
        cnt_steps += abs(p1[0] - intersection[0]) + abs(p1[1] - intersection[1])
        cnt_steps += abs(p2[0] - intersection[0]) + abs(p2[1] - intersection[1])
        min_steps = min(min_steps, cnt_steps)
        # print("cnt_steps")
        # print(cnt_steps)
        stop = True
        break
    if stop:
      break

  cnt_steps = 0
  skip_first_paths = True
  stop = False
  p2_steps = 0
  for p2 in paths2:
    p2_steps += count_steps(p2)
    cnt_steps = p2_steps
    for p1 in paths1:
      cnt_steps += count_steps(p1)
      if skip_first_paths:
        skip_first_paths = False
        continue
      intersection = get_intersection(p1, p2)
      if intersection != None:
        cnt_steps -= count_steps(p1)
        cnt_steps -= count_steps(p2)
        cnt_steps += abs(p1[0] - intersection[0]) + abs(p1[1] - intersection[1])
        cnt_steps += abs(p2[0] - intersection[0]) + abs(p2[1] - intersection[1])
        min_steps = min(min_steps, cnt_steps)
        # print("cnt_steps")
        # print(cnt_steps)
        stop = True
        break
    if stop:
      break


  f.close()

  print(min_steps)