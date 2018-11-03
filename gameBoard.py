from tetrominoe import Tetrominoe

class GameBoard:

    score = 0
    alive = True
    speed = 1

    def __init__(self, width = 10, height = 30):
        self.width, self.height = width, height
        self.game_board = [([0] * height) for i in range(width)]
        self.board_size = [width, height]
        self.current_tetrominoe = Tetrominoe(self.board_size, self.speed)
        self.next_tetrominoe = Tetrominoe(self.board_size, self.speed)

    def check_contact(self, tetrominoe):
        contact = False
        for blocks in tetrominoe.blocks:
            if self.game_board[tetrominoe.position[0] + dots[0], tetrominoe.position[1] + blocks[1]] == 1:
                contact = True
                break
        return contact

    def settle(self):
        for blocks in self.current_tetrominoe.blocks:
            self.game_board[tetrominoe.position[0] + dots[0], tetrominoe.position[1] + blocks[1]] = 1
        self.generate_new_block()

    def check_death(self):
        death = False
        for blocks in self.current_tetrominoe.blocks:
            if self.current_tetrominoe.position[1] + blocks[1] <2:
                death = True
                break
        return death

    def generate_new_block(self):
        self.current_tetrominoe = self.next_tetrominoe
        self.next_tetrominoe = Tetrominoe(self.board_size, speed)

    def try_to_clear(self):
        rows_to_clear = []
        for y in range(self.board_size[1]):
            row = [self.game_board[x][y] for x in range(self.board_size[0])]
            if min(row) == 1: rows_to_clear.append(y)
        if len(rows_to_clear) > 0: self.clear(rows_to_clear)

    def clear(self, rows):
        for y in range(min(rows), self.board_size[1]):
            for x in range(self.board_size[0]):
                y2 = y + len(rows)
                self.game_board[x][y] = self.game_board[x][y2] if y2 < (self.board_size[1] - 1) else 0

    def show_game_board(self):
        # display board in nomal view (smaller y at bottom)
        print("displaying game board:")
        for y in range(self.board_size[1] - 1, -1, -1):
            row = [self.game_board[x][y] for x in range(self.board_size[0])]
            print(row)