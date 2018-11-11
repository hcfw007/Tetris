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
    
    def __init__(self, board_size, block_type = "Random"):
        self.type = random.choice(self.__BLOCK_TYPES) if block_type == "Random" else block_type
        self.blocks = random.choice(self.__BLOCK[self.type])
        self.board_size = board_size
        self.position = [board_size[0] // 2, board_size[1]]
        self.position[1] = 2 * board_size[1] - self.get_border()[0] - 3
        print("new " + self.type + " shaped tetrominoe")


    def drop(self):
        self.position[1] -= 1

    def retreat(self):
        self.position[1] += 1

    def rotate(self):
        index = self.__BLOCK[self.type].index(self.blocks)
        index = index + 1 if index < len(self.__BLOCK[self.type]) - 1 else 0
        self.blocks = self.__BLOCK[self.type][index]

    def get_border(self):
        left, top = right, bottom = self.position
        for coordinate in self.blocks:
            if self.position[0] + coordinate[0] < left: left =  self.position[0] + coordinate[0]
            if self.position[0] + coordinate[0] > right: right =  self.position[0] + coordinate[0]
            if self.position[1] + coordinate[1] < top: top =  self.position[1] + coordinate[1]
            if self.position[1] + coordinate[1] < bottom: bottom =  self.position[1] + coordinate[1]
        return top, bottom, left, right

    def move_left(self):
        self.position[0] -= 1
    
    def move_right(self):
        self.position[0] += 1
