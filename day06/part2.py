def path_to_root(objects, obj_name):
  path = []
  cur = objects[obj_name]
  while cur["parent"] != None:
    path.append(cur["parent"])
    cur = objects[cur["parent"]]
  return path

if __name__=="__main__":
  f = open("input.txt", "r")
  objects = dict()
  for line in f:
    obj_name1, obj_name2 = line.strip("\n").split(")")
    if obj_name1 not in objects:
      objects[obj_name1] = {"parent": None}
    objects[obj_name2] = {"parent": obj_name1}

  path1 = path_to_root(objects, "YOU")
  path2 = path_to_root(objects, "SAN")
  
  total = 0
  for i in range(0, len(path1)):
    for j in range(0, len(path2)):
      if path2[j] == path1[i]:
        total = i + j
        break
    if total != 0:
      break
  
  print(total)