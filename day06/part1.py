if __name__=="__main__":
  f = open("input.txt", "r")
  objects = dict()
  for line in f:
    obj_name1, obj_name2 = line.strip("\n").split(")")
    if obj_name1 not in objects:
      objects[obj_name1] = {"parent": None}
    objects[obj_name2] = {"parent": obj_name1}

  cnt = 0
  for key in objects:
    cur = objects[key]
    while cur["parent"] != None:
      cnt += 1
      cur = objects[cur["parent"]]

  print(cnt)