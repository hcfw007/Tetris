import random

class Blocks:

    __BLOCK_TYPES = ("I", "S", "Z", "O", "L", "J", "T")

    __BLOCK = {}
    __BLOCK["I"] = (((0, 0), (0, 1), (0, 2), (0, 3)), ((0, 0), (1, 0), (2, 0), (3, 0)))
    __BLOCK["S"] = (((0, 0), (0, 1), (1, 1), (1, 2)), ((0, 0), (0, -1), (1, -1), (1, -2)))
    __BLOCK["Z"] = (((0, 0), (1, 0), (1, -1), (2, -1)), ((0, 0), (0, 1), (1, 1), (1, 2)))
    __BLOCK["O"] = (((0, 0), (0, 1), (1, 1), (1, 0)), )
    __BLOCK["L"] = (((0, 0), (-1, 0), (-1, 1), (-1, 2)), ((0, 0), (0, 1), (1, 1), (2, 1)), ((0, 0), (1, 0), (1, -1), (1, -2)), ((0, 0), (0, -1), (-1, -1), (-2, -1)))
    __BLOCK["J"] = (((0, 0), (-1, 0), (-1, -1), (-1, -2)), ((0, 0), (0, -1), (1, -1), (2, -1)), ((0, 0), (1, 0), (1, 1), (1, 2)), ((0, 0), (0, 1), (-1, 1), (-2, 1)))
    __BLOCK["T"] = (((0, 0), (0, 1), (-1, 0), (1, 0)), ((0, 0), (1, 0), (0, 1), (0, -1)), ((0, 0), (0, -1), (1, 0), (-1, 0)), ((0, 0), (-1, 0), (0, -1), (0, 1)))

    blockType = None
    blockDots = None
    position = [5, 0]
    speed = 1
    
    def __init__(self):
        self.blockType = random.choice(self.__BLOCK_TYPES)
        self.blockDots = random.choice(self.__BLOCK[self.blockType])
        
        print(self.blockDots)
        print(self.blockType)

    def drop(self):
        self.position[1] += speed

    def rotate(self):
        index = self.__BLOCK[self.blockType].index(self.blockDots)
        index = index + 1 if index < len(self.__BLOCK[self.blockType]) - 1 else 0
        print(index)
        self.blockDots = self.__BLOCK[self.blockType][index]

    def getBorder(self):
        left, top = right, bottom = self.position
        for coordinate in self.blockDots:
            if self.position[0] + coordinate[0] < left left =  self.position[0] + coordinate[0]
            if self.position[0] + coordinate[0] > right right =  self.position[0] + coordinate[0]
            if self.position[1] + coordinate[1] < top top =  self.position[1] + coordinate[1]
            if self.position[1] + coordinate[1] < bottom bottom =  self.position[1] + coordinate[1]
        return top, bottom, left, right