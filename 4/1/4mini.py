
import numpy as np

t = [0, 1, 2, 3, 4, 5, 6, 7, 8]

draws = [0, 3, 6]

npBoards = np.array(t)
boards = list(npBoards.reshape(3, 3))
maskBoards = np.zeros_like(boards)

for draw in draws:
    for boardNum, board in enumerate(boards):
        finds = np.nonzero(board == draw)
        coords = list(zip(finds[0], finds[1]))
        for i, find in enumerate(coords):
            np.put(maskBoards[boardNum], find, 1)

        if np.all(maskBoards):
            print("hi")