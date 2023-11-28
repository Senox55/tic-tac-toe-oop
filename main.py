import pygame

pygame.init()

white_color = (255, 255, 255)
green_color = (0, 255, 0)
red_color = (255, 0, 0)
black_color = (0, 0, 0)


class GameBoard:
    def __init__(self, width, height):
        self.__size = 3
        self.field = [' ' for i in range(self.__size ** 2)]
        self.width = width
        self.height = height

    def draw_cross(self):
        pass

    def draw_circle(self):
        pass

    def draw_field(self):
        pygame.display.set_caption("Крестики-Нолики")
        screen_size = [self.width, self.height]
        screen = pygame.display.set_mode(screen_size)
        screen.fill(white_color)
        pygame.display.flip()
        for width_indent in range(1, self.__size):
            start_pos = ((self.width / self.__size) * width_indent, 0)
            end_pos = ((self.width / self.__size) * width_indent, self.height)
            pygame.draw.line(screen, black_color, start_pos, end_pos, 3)
        for height_indent in range(1, self.__size):
            start_pos = (0, (self.height / self.__size) * height_indent)
            end_pos = (self.width, (self.height / self.__size) * height_indent)
            pygame.draw.line(screen, black_color, start_pos, end_pos, 3)
        pygame.display.flip()

    def draw_winner(self):
        pass

    def is_sell_free(self, number_sell: int) -> bool:
        if self.field[number_sell] == ' ':
            return True
        else:
            return False


class Player:
    def __init__(self, game_symbol):
        self.game_symbol = game_symbol

    def real_board_to_virtual(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        return (y // 200) * 3 + (x // 200)


class Game:
    def __init__(self, player1, player2):
        self.player_move = player1
        self.player1 = player1
        self.player2 = player2

    def real_board_to_virtual(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        return (y // 200) * 3 + (x // 200)

    def make_move(self, cell_number):
        game_board.field[cell_number] == self.player1.game_symbol
        print(game_board.field[cell_number])
        print(cell_number)
        print(game_board.field)

    def start_game(self):
        game_board.draw_field()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = event.pos
                    cell_number = self.real_board_to_virtual(mouse_pos)
                    if game_board.is_sell_free(cell_number) is True:
                        self.make_move(cell_number)


game_board = GameBoard(600, 600)
player1 = Player('X')
player2 = Player('O')
game = Game(player1, player2)
game.start_game()
