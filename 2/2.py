from pathlib import Path

filePath = Path(__file__).with_name('input.txt')

with filePath.open('r') as file:
    inputData = file.read().splitlines()

horizontal = 0
depth = 0
for line in inputData:
    direction, distance = line.split(' ')
    if direction == 'forward':
        horizontal += int(distance)
    if direction == 'down':
        depth += int(distance)
    if direction == 'up':
        depth -= int(distance)

print(horizontal*depth)
# 1893605