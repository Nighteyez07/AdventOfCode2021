#https://adventofcode.com/2021/day/3

def split(item):
    return list(item)

def filterOxy(array, position):
    returnArr = []
    onCnt = 0
    offCnt = 0
    keep = ""

    for item in array:
        if item[position] == "1":
            onCnt = onCnt + 1
        else:
            offCnt = offCnt + 1

    if onCnt >= offCnt:
        keep = "1"
    else:
        keep = "0"

    for item in array:
        if item[position] == keep:
            returnArr.append(item)    

    return returnArr

def filterCO2(array, position):
    returnArr = []
    onCnt = 0
    offCnt = 0
    keep = ""

    for item in array:
        if item[position] == "1":
            onCnt = onCnt + 1
        else:
            offCnt = offCnt + 1

    if offCnt <= onCnt:
        keep = "0"
    else:
        keep = "1"

    for item in array:
        if item[position] == keep:
            returnArr.append(item)    

    return returnArr

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

oxyarr = dataset
pos = 0

while len(oxyarr) > 1:
    oxyarr = filterOxy(oxyarr, pos)
    pos = pos + 1

co2rr = dataset
pos = 0

while len(co2rr) > 1:
    co2rr = filterCO2(co2rr, pos)
    pos = pos + 1

oxyVal = int(''.join(oxyarr[0]), 2)
co2Val = int(''.join(co2rr[0]), 2)

print(oxyVal * co2Val)