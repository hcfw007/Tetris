from blocks import Blocks

class GameBoard:

    score = 0
    alive = True

    def __init__(self, width = 10, height = 30):
        self.width, self.height = width, height
        self.gameBoard = [[0] * height] * width
        self.borderSize = [width, height]
        self.nextBlock = Blocks(self.borderSize)