import pygame

class Cell(pygame.sprite.Sprite):
    def __init__(self, rect, grid_pos: [int, int], game_obj):
        super().__init__()  # Initialize the pygame sprite class
        self.grid_pos = grid_pos
        self.state = False
        self.future_state = False
        self.rect: pygame.rect = rect
        self.obj = game_obj

    def update(self):
        live_neighbors = 0

        # This whole function needs to be reworked.

        # Normal Case
        if 0 < self.grid_pos[0] < (self.obj.grid_width - 1) and 0 < self.grid_pos[1] < (self.obj.grid_height - 1):
            for cell in self.obj.cells:
                if cell.grid_pos == [self.grid_pos[0] + 1, self.grid_pos[1]] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0], self.grid_pos[1] + 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] - 1, self.grid_pos[1]] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0], self.grid_pos[1] - 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] - 1, self.grid_pos[1] - 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] + 1, self.grid_pos[1] - 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] - 1, self.grid_pos[1] + 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] + 1, self.grid_pos[1] + 1] and cell.state:
                    live_neighbors += 1

        # Left Side
        if self.grid_pos[0] == 0 and 0 < self.grid_pos[1] < self.obj.grid_height - 1:
            for cell in self.obj.cells:
                if cell.grid_pos == [self.grid_pos[0] + 1, self.grid_pos[1]] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0], self.grid_pos[1] + 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0], self.grid_pos[1] - 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] + 1, self.grid_pos[1] - 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] + 1, self.grid_pos[1] + 1] and cell.state:
                    live_neighbors += 1

        # Right Side
        if self.grid_pos[0] == self.obj.grid_width - 1 and 0 < self.grid_pos[1] < self.obj.grid_height - 1:
            for cell in self.obj.cells:
                if cell.grid_pos == [self.grid_pos[0], self.grid_pos[1] + 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] - 1, self.grid_pos[1]] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0], self.grid_pos[1] - 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] - 1, self.grid_pos[1] - 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] - 1, self.grid_pos[1] + 1] and cell.state:
                    live_neighbors += 1

        # Top
        if 0 < self.grid_pos[0] < self.obj.grid_width - 1 and self.grid_pos[1] == 0:
            for cell in self.obj.cells:
                if cell.grid_pos == [self.grid_pos[0] + 1, self.grid_pos[1]] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0], self.grid_pos[1] + 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] - 1, self.grid_pos[1]] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] - 1, self.grid_pos[1] + 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] + 1, self.grid_pos[1] + 1] and cell.state:
                    live_neighbors += 1

        # Bottom
        if 0 < self.grid_pos[0] < self.obj.grid_width - 1 and self.grid_pos[1] == self.obj.grid_height - 1:
            for cell in self.obj.cells:
                if cell.grid_pos == [self.grid_pos[0] + 1, self.grid_pos[1]] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] - 1, self.grid_pos[1]] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0], self.grid_pos[1] - 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] - 1, self.grid_pos[1] - 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] + 1, self.grid_pos[1] - 1] and cell.state:
                    live_neighbors += 1

        # Top left corner
        if self.grid_pos == [0, 0]:
            for cell in self.obj.cells:
                if cell.grid_pos == [self.grid_pos[0] + 1, self.grid_pos[1]] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0], self.grid_pos[1] + 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] + 1, self.grid_pos[1] + 1] and cell.state:
                    live_neighbors += 1

        # Bottom Left corner
        if self.grid_pos == [0, self.obj.grid_height-1]:
            for cell in self.obj.cells:
                if cell.grid_pos == [self.grid_pos[0] + 1, self.grid_pos[1]] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0], self.grid_pos[1] - 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] + 1, self.grid_pos[1] - 1] and cell.state:
                    live_neighbors += 1

        # Top Right corner
        if self.grid_pos == [self.obj.grid_width - 1, 0]:
            for cell in self.obj.cells:
                if cell.grid_pos == [self.grid_pos[0], self.grid_pos[1] + 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] - 1, self.grid_pos[1]] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] - 1, self.grid_pos[1] + 1] and cell.state:
                    live_neighbors += 1

        # Bottom Right
        if self.grid_pos == [self.obj.grid_width - 1, self.obj.grid_height - 1]:
            for cell in self.obj.cells:
                if cell.grid_pos == [self.grid_pos[0] - 1, self.grid_pos[1]] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0], self.grid_pos[1] - 1] and cell.state:
                    live_neighbors += 1
                if cell.grid_pos == [self.grid_pos[0] - 1, self.grid_pos[1] - 1] and cell.state:
                    live_neighbors += 1

        # print(live_neighbors)
        if live_neighbors < 2:
            self.future_state = False
        elif self.state == False and live_neighbors == 3:
            self.future_state = True
        elif live_neighbors > 3:
            self.future_state = False
        elif live_neighbors == 2 and self.state:
            self.future_state = True
        elif live_neighbors == 3 and self.state:
            self.future_state = True
        elif live_neighbors == 2 and self.state == False:
            self.future_state = False
        else:
            print(f"Somethings Wrong {live_neighbors}")
        # Rules:
        # Any Cell with fewer than 2 live neighbors dies
        # Any live cell with two or three live neighbors lives
        # Any live cell with more than three live neighbors dies
        # Any dead cell with 3 live neighbors becomes live
