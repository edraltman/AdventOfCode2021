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

# Convert list of strings (as binary) to decimal
gamma = int(''.join(gammaArray),2)
epsilon = int(''.join(epsilonArray),2)

print(gamma*epsilon)
