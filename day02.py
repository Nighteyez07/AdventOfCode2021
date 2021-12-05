x = 0
y = 0
aim = 0

with open("day02.txt", "r") as f_file:
  for line in f_file:
    move = line.split()
    direction = move[0][0]
    distance = int(move[1])

    if direction == "f":
      x = x + distance
      y = (aim * distance) + y

    if direction == "d":
      #y = y + distance
      aim = aim + distance
    
    if direction == "u":
      #y = y - distance
      aim = aim - distance

    print(distance)
    print(direction)
    print(x)
    print(y)
    print(aim)
    

print(x)
print(y)
print(aim)
print(x*y)
    