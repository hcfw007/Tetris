from tetrominoe import Tetrominoe

class GameBoard:

    score = 0
    score_list = (0, 1, 4, 9, 16)
    alive = True
    speed = 9
    pause = False

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
        return self.try_to_clear()

    def check_death(self):
        death = False
        for blocks in self.current_tetrominoe.blocks:
            if self.current_tetrominoe.position[1] + blocks[1] <2 and self.check_contact(self.current_tetrominoe):
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
        if len(rows_to_clear) > 0:
            self.score += self.score_list[len(rows_to_clear)]
            self.clear(rows_to_clear)
            return True
        return False

    def clear(self, rows):
        rows.sort(reverse = True)
        for row in rows:
            for y in range(row, self.board_size[1]):
                for x in range(self.board_size[0]):
                    self.game_board[x][y] = self.game_board[x][y + 1] if y + 1 < (self.board_size[1] - 1) else 0

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
        if self.pause:
            return {
                'dead': False,
                'score_change': False,
            }
        else:
            score_change = False
            self.current_tetrominoe.drop()
            if self.check_contact(self.current_tetrominoe):
                self.current_tetrominoe.retreat()
                score_change = self.settle()
            return {
                'dead': self.check_death(),
                'score_change': score_change,
            }
    
    def move_left(self):
        if self.check_left(self.current_tetrominoe): self.current_tetrominoe.move_left()
        
    def move_right(self):
        if self.check_right(self.current_tetrominoe): self.current_tetrominoe.move_right()

    def rotate(self):
        if self.check_current_rotate(): self.current_tetrominoe.rotate()

    def check_left(self, tetrominoe):
        left = tetrominoe.get_border()[2]
        if left < 1: return False
        for block in tetrominoe.blocks:
            if tetrominoe.position[1] + block[1] > self.board_size[1] - 1: continue
            if self.game_board[tetrominoe.position[0] + block[0] - 1][tetrominoe.position[1] + block[1]] == 1: return False
        return True

    def check_right(self, tetrominoe):
        right = tetrominoe.get_border()[3]
        if right > self.board_size[0] - 2: return False
        for block in tetrominoe.blocks:
            if tetrominoe.position[1] + block[1] > self.board_size[1] - 1: continue
            if self.game_board[tetrominoe.position[0] + block[0] + 1][tetrominoe.position[1] + block[1]] == 1: return False
        return True

    def check_current_rotate(self):
        index = self.current_tetrominoe._Tetrominoe__BLOCK[self.current_tetrominoe.type].index(self.current_tetrominoe.blocks)
        index = index + 1 if index < len(self.current_tetrominoe._Tetrominoe__BLOCK[self.current_tetrominoe.type]) - 1 else 0
        new_lattice = self.current_tetrominoe._Tetrominoe__BLOCK[self.current_tetrominoe.type][index]
        for block in new_lattice:
            x, y = self.current_tetrominoe.position[0] + block[0], self.current_tetrominoe.position[1] + block[1]
            if x < 0 or x >= self.board_size[0]: return False
            if y < 0: return False
            if self.game_board[x][y] != 0: return False
        return True
            
    def toggle_pause(self):
        self.pause = not self.pause