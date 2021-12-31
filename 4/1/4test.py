from pathlib import Path
import numpy as np

t = [65, 69, 73, 60, 66, 79, 23, 95, 32, 56, 36, 51,
     26, 1, 28, 76, 9, 3, 71, 77, 41, 15, 61, 68, 14, 65, 69, 73, 60, 66, 79, 23, 95, 32, 56, 36, 51,
     26, 1, 28, 76, 9, 3, 71, 77, 41, 15, 61, 68, 14]

draws = [65, 60, 66]

npBoards = np.array(t)
boards = npBoards.reshape(2, 5, 5)
maskBoards = np.zeros_like(boards)

for draw in draws:
    for boardNum, board in enumerate(boards):
        finds = np.nonzero(board == draw)
        coords = list(zip(finds[0],finds[1]))
        for i, find in enumerate(coords):
            np.put(maskBoards[boardNum], find, 1)
