from pathlib import Path

filePath = Path(__file__).with_name('input.txt')

with filePath.open('r') as file:
    ints = list(map(int, file.read().splitlines()))


biggerThanPrevious = 0
previousSum = sum(ints[:3])

for i in range(2, len(ints)):
    newSum = sum(ints[i-2:i+1])
    if newSum > previousSum:
        biggerThanPrevious += 1

    previousSum = newSum

print(biggerThanPrevious)
# 1518