from pathlib import Path
import numpy as np


def readBingo(fileName: str, numberOfBoards: int, x: int, y: int):
    p = Path(__file__).with_name(fileName)

    with p.open('r') as f:
        allData = f.read()
        # First line are the draws, the rest are the boards
        draws = list(map(int, allData.split('\n', 1)[0].split(',')))
        # Strip all leading/trailing whitespace, separate into one big array
        rawBoards = list(map(int, allData.split('\n', 1)[1].strip().split()))

        # Convert each board into a 5x5 array
        npBoards = np.array(rawBoards)
        boards = npBoards.reshape(numberOfBoards, x, y)

    return draws, boards


if __name__ == "__main__":
    numberOfBoards = 100
    x, y = 5, 5

    # Get draws, boards and masking boards of zeros
    draws, boards = readBingo('input.txt', numberOfBoards, x, y)
    maskBoards = np.zeros_like(boards)

    for draw in draws:
        for boardNum, board in boards:
            finds = np.nonzero(board == draw)
            coords = list(zip(finds[0], finds[1]))
            for find in coords:
                print(f'{draw} found at {str(find)}')
                np.put(maskBoards[boardNum], find, True)
            
            if np.all(board):
                
