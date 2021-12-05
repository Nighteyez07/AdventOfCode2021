#https://adventofcode.com/2021/day/3

def split(item):
    return list(item)

dataset = []
gamma = ""
epsilon = ""

with open("day03.txt", "r") as f_file:
  for line in f_file:
    dataset.append(split(line.strip()))

listLen = len(dataset[0])

for x in range(listLen):
  on = 0
  off = 0

  for item in dataset:
    if item[x] == "1":
      on += 1
    else:
      off +=1

  if on > off:
    gamma += "1"  
    epsilon += "0"  
  else:
    gamma += "0"  
    epsilon += "1"  

gammaVal = int(gamma, 2)
epiVal = int(epsilon, 2)

print(gammaVal * epiVal)



#convert to array
#find gamma by most common bit in each position
#find epsilon by least common bit (reverse of gamma in each position

#convert gamma to decimal
#convert epsilon to decimal
#multiply them together
