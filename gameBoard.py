from tetrominoe import Tetrominoe

class GameBoard:

    score = 0
    alive = True
    speed = 5

    BLOCK_COLOR = (255, 255, 0)

    def __init__(self, width = 10, height = 30):
        self.width, self.height = width, height
        self.game_board = [([0] * height) for i in range(width)]
        self.board_size = [width, height]
        self.current_tetrominoe = Tetrominoe(self.board_size)
        self.next_tetrominoe = Tetrominoe(self.board_size)

    def check_contact(self, tetrominoe):
        contact = False
        for blocks in tetrominoe.blocks:
            if tetrominoe.position[1] + blocks[1] < 0 or self.game_board[tetrominoe.position[0] + blocks[0]][tetrominoe.position[1] + blocks[1]] == 1:
                contact = True
                break
        return contact

    def settle(self):
        for blocks in self.current_tetrominoe.blocks:
            self.game_board[self.current_tetrominoe.position[0] + blocks[0]][self.current_tetrominoe.position[1] + blocks[1]] = 1
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
        self.next_tetrominoe = Tetrominoe(self.board_size)

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
            
    def draw(self, surface, grid_origin, block_length):

        def draw_block(block_coordinate):
            block_rect = ((grid_origin[0] + block_coordinate[0] * block_length, grid_origin[1] - (block_coordinate[1] + 1) * block_length), (block_length, block_length))
            surface.fill(self.BLOCK_COLOR, block_rect)

        for x in range(self.board_size[0]):
            for y in range(self.board_size[1]):
                if self.game_board[x][y] == 1:
                    draw_block([x, y])
        
        t = self.current_tetrominoe
        for i in t.blocks:
            x = t.position[0] + i[0]
            y = t.position[1] + i[1]
            if (x < self.width) and (y < self.height):
                draw_block([x, y])

    def next_tick(self):
        self.current_tetrominoe.drop()
        if self.check_contact(self.current_tetrominoe):
            self.current_tetrominoe.retreat()
            self.settle()