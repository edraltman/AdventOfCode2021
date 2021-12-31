from pathlib import Path

# import file
filePath = Path(__file__).with_name('input.txt')
with filePath.open('r') as file:
    strings = file.read().splitlines()

# Build empty lists
def emptyListOfLists(i):
    return [[] for x in range(i)]

a = emptyListOfLists(len(strings[0]))
gammaArray = emptyListOfLists(len(strings[0]))
epsilonArray = emptyListOfLists(len(strings[0]))


# build "columnular" data
for string in strings:
    for i, v in enumerate(list(string)):
        a[i].append(v)

# Get the most common bit from each list
for i, element in enumerate(a):
    gammaArray[i] = max(set(element), key=element.count)
    epsilonArray[i] = min(set(element), key=element.count)

# Oxygen = most common
# CO2    = least common
oxygenList = []
oxygenList = strings
oxygenListTemp = []
for i, element in enumerate(gammaArray):
    for string in oxygenList:
        if string[i] == element:
            oxygenListTemp.append(string)
    oxygenList = oxygenListTemp
    oxygenListTemp = []

# CO2    = least common
co2List = []
co2List = strings
co2ListTemp = []
for i, element in enumerate(epsilonArray):
    for string in co2List:
        if string[i] == element:
            co2ListTemp.append(string)
    co2List = co2ListTemp
    co2ListTemp = []




# Convert list of strings (as binary) to decimal
gamma = int(''.join(gammaArray),2)
epsilon = int(''.join(epsilonArray),2)

