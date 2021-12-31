from pathlib import Path

filePath = Path(__file__).with_name('input.txt')

with filePath.open('r') as file:
    inputData = file.read().splitlines()

ints = list(map(int, inputData))

biggerThanPrevious = 0

with open('output_int.txt','w') as file:
    for i, v in enumerate(ints):
        if i != 0:
            if v > ints[i-1]:
                biggerThanPrevious += 1
                file.writelines(f"{str(i)}\n")

# This is a good lesson in data types. '1006' is not greater than '998'

with open('output_str.txt','w') as file:
    for i, v in enumerate(inputData):
        if i != 0:
            if i == 227:
                print("wtf")
            if v > inputData[i-1]:
                biggerThanPrevious += 1
                file.writelines(f"{str(i)}\n")



print(biggerThanPrevious)


