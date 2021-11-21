import pygame
from cell import *

updated_cells = []


def draw_cells(self):
    cell_list = [cell for cell in self.cells]
    global updated_cells
    for cell in self.cells:
        if cell.state:
            pygame.draw.rect(self.window, self.white, cell.rect)

        else:
            pygame.draw.rect(self.window, self.grey, cell.rect)
        #print(updated_cells)

def draw_grid(self, grid_width, grid_height):
    for column_num in range(grid_width):
        for row_num in range(grid_height):
            rect = pygame.Rect((column_num * (self.width / grid_width)), (row_num * (self.height / grid_height)),
                               (self.height / grid_height),
                               (self.height / grid_height))
            self.cells.add(Cell(rect, [column_num, row_num], game))


class Game:
    def __init__(self):
        pygame.init()
        self.grid_width = 30  # int(input("Grid width: "))
        self.grid_height = 30  # int(input("Grid Height: "))
        self.size = self.width, self.height = 700, 700
        self.overlay_size = ((self.width / self.grid_width) * 1.5, (self.height / self.grid_height) * 1.5)
        self.black, self.white, self.grey = (0, 0, 0), (255, 255, 255), (128, 128, 128)
        self.setup = True
        self.sim = False
        self.running = True
        self.title = "Game of Life Practice"
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        self.cells = pygame.sprite.Group()

        window = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

    def events(self):
        ev = pygame.event.get()
        keys = pygame.key.get_pressed()
        if self.setup:
            if keys[pygame.K_q]:
                self.setup = False
                self.running = False
            if keys[pygame.K_RETURN]:
                self.setup = False
                self.sim = True
            pygame.time.delay(100)
            for event in ev:
                if event.type == pygame.QUIT:
                    self.running, self.setup = False, False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    clicked_cell = [cell for cell in self.cells if cell.rect.collidepoint(pos)]
                    if len(clicked_cell) == 1:
                        clicked_cell[0].state = True
        if self.sim:
            for event in ev:
                if event.type == pygame.QUIT:
                    self.running, self.sim = False, False
            if keys[pygame.K_q]:
                self.running = False
                self.sim = False
            if keys[pygame.K_r]:
                self.sim = False
                self.setup = True
                for cell in self.cells:
                    cell.state = False

    def game_loop(self):
        global updated_cells

        draw_grid(self, self.grid_width, self.grid_height)
        while self.running:
            while self.setup:
                self.events()
                self.window.fill(self.black)
                draw_cells(self)

                for i in range(game.grid_width):
                    pygame.draw.rect(game.window, game.black, (i * (game.width / game.grid_width), 0, 1, game.height))
                for i in range(game.grid_height):
                    pygame.draw.rect(game.window, game.black, (0, i * (game.height / game.grid_height), game.height, 1))
                pygame.display.flip()

            while self.sim:
                self.events()

                # pygame.time.delay(100)
                self.window.fill(self.black)

                for cell in self.cells:
                    cell.update()
                for cell in self.cells:
                    cell.state = cell.future_state
                draw_cells(self)

                for i in range(game.grid_width):
                    pygame.draw.rect(game.window, game.black, (i * (game.width / game.grid_width), 0, 1, game.height))
                for i in range(game.grid_height):
                    pygame.draw.rect(game.window, game.black, (0, i * (game.height / game.grid_height), game.height, 1))
                pygame.display.flip()
                # pygame.time.delay(100)
                updated_cells = []


game = Game()
