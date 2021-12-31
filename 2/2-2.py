from pathlib import Path

filePath = Path(__file__).with_name('input.txt')

with filePath.open('r') as file:
    inputData = file.read().splitlines()

horizontal = 0
depth = 0
aim = 0

for line in inputData:
    direction, distance = line.split(' ')
    if direction == 'forward':
        horizontal += int(distance)
        depth += aim * int(distance)
    if direction == 'down':
        aim += int(distance)
    if direction == 'up':
        aim -= int(distance)

print(horizontal*depth)
# 2120734350