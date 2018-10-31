import random

class Tetrominoe:

    __BLOCK_TYPES = ("I", "S", "Z", "O", "L", "J", "T")

    __BLOCK = {}
    __BLOCK["I"] = (((0, 0), (0, 1), (0, 2), (0, 3)), ((0, 0), (1, 0), (2, 0), (3, 0)))
    __BLOCK["S"] = (((0, 0), (0, 1), (1, 1), (1, 2)), ((0, 0), (0, -1), (1, -1), (1, -2)))
    __BLOCK["Z"] = (((0, 0), (1, 0), (1, -1), (2, -1)), ((0, 0), (0, 1), (1, 1), (1, 2)))
    __BLOCK["O"] = (((0, 0), (0, 1), (1, 1), (1, 0)), )
    __BLOCK["L"] = (((0, 0), (-1, 0), (-1, 1), (-1, 2)), ((0, 0), (0, 1), (1, 1), (2, 1)), ((0, 0), (1, 0), (1, -1), (1, -2)), ((0, 0), (0, -1), (-1, -1), (-2, -1)))
    __BLOCK["J"] = (((0, 0), (-1, 0), (-1, -1), (-1, -2)), ((0, 0), (0, -1), (1, -1), (2, -1)), ((0, 0), (1, 0), (1, 1), (1, 2)), ((0, 0), (0, 1), (-1, 1), (-2, 1)))
    __BLOCK["T"] = (((0, 0), (0, 1), (-1, 0), (1, 0)), ((0, 0), (1, 0), (0, 1), (0, -1)), ((0, 0), (0, -1), (1, 0), (-1, 0)), ((0, 0), (-1, 0), (0, -1), (0, 1)))

    position = [5, 0]
    
    def __init__(self, board_size, speed = 1):
        self.type = random.choice(self.__BLOCK_TYPES)
        self.blocks = random.choice(self.__BLOCK[self.type])
        self.board_size = board_size
        self.speed = speed

        print(self.blocks)
        print(self.type)

    def drop(self):
        self.position[1] += speed

    def rotate(self):
        index = self.__BLOCK[self.type].index(self.blocks)
        index = index + 1 if index < len(self.__BLOCK[self.type]) - 1 else 0
        print(index)
        self.blocks = self.__BLOCK[self.type][index]

    def get_border(self):
        left, top = right, bottom = self.position
        for coordinate in self.blocks:
            if self.position[0] + coordinate[0] < left: left =  self.position[0] + coordinate[0]
            if self.position[0] + coordinate[0] > right: right =  self.position[0] + coordinate[0]
            if self.position[1] + coordinate[1] < top: top =  self.position[1] + coordinate[1]
            if self.position[1] + coordinate[1] < bottom: bottom =  self.position[1] + coordinate[1]
        return top, bottom, left, right

    def moveLeft(self):
        if self.get_border()[2] > 0: self.position[0] -= 1
    
    def moveRight(self):
        if self.get_border()[2] < self.board_size[0] - 1: self.position[0] += 1
