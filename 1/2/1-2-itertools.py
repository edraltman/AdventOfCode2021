from pathlib import Path
import itertools

filePath = Path(__file__).with_name('input.txt')

with filePath.open('r') as file:
    ints = list(map(int, file.read().splitlines()))


biggerThanPrevious = 0

chunked = [sum(list(itertools.islice(ints, i, i + 3)))
           for i in range(0, len(ints), 1)]

for i in range(1, len(chunked)):
    if chunked[i] > chunked[i-1]:
        biggerThanPrevious += 1

print(biggerThanPrevious)
# 1518
