from blocks import Blocks

class GameBoard:

    score = 0
    alive = True

    def __init__(self, width = 10, height = 30):
        self.width, self.height = width, height
        self.gameBoard = [[0] * height] * width
        self.borderSize = [width, height]
        self.currentBlock = Blocks(self.boardSize)
        self.nextBlock = Blocks(self.boardSize)

    def checkContact(self, block):
        contact = False
        for dots in block.blockDots:
            if self.gameBoard[block.position[0] + dots[0], block.position[1] + dots[1]] == 1:
                contact = True
                break
        return contact

    def settle(self):
        for dots in self.currentBlock.blockDots:
            self.gameBoard[block.position[0] + dots[0], block.position[1] + dots[1]] = 1
        self.currentBlock = self.nextBlock
        self.nextBlock = BLocks(self.borderSize)

    def checkDeath(self):
        death = False
        for dots in self.currentBlock.blockDots:
            if self.currentBlock.position[1] + dots[1] <2:
                death = True
                break
        return death