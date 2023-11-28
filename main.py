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
        self.screen_size = [self.width, self.height]
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.__size
        self.cell_height = self.height // self.__size
        self.distance_from_walls = 25

    def draw_cross(self, center_figure):
        pygame.draw.line(self.screen, red_color, (center_figure[0] - (self.cell_width // 2 - self.distance_from_walls),
                                                  center_figure[1] - (
                                                          self.cell_height // 2 - self.distance_from_walls)),
                         (center_figure[0] + (self.cell_width // 2 - self.distance_from_walls),
                          center_figure[1] + (self.cell_height // 2 - self.distance_from_walls)), 10)

        pygame.draw.line(self.screen, red_color, (center_figure[0] + (self.cell_width // 2 - self.distance_from_walls),
                                                  center_figure[1] - (
                                                          self.cell_height // 2 - self.distance_from_walls)),
                         (center_figure[0] - (self.cell_width // 2 - self.distance_from_walls),
                          center_figure[1] + (self.cell_height // 2 - self.distance_from_walls)), 10)
        pygame.display.flip()

    def draw_circle(self, center_figure):
        pygame.draw.circle(self.screen, green_color, center_figure, self.cell_width // 2 - self.distance_from_walls, 10)
        pygame.display.flip()

    def draw_field(self):
        pygame.display.set_caption("Крестики-Нолики")
        self.screen.fill(white_color)
        pygame.display.flip()
        for width_indent in range(1, self.__size):
            start_pos = ((self.width / self.__size) * width_indent, 0)
            end_pos = ((self.width / self.__size) * width_indent, self.height)
            pygame.draw.line(self.screen, black_color, start_pos, end_pos, 3)
        for height_indent in range(1, self.__size):
            start_pos = (0, (self.height / self.__size) * height_indent)
            end_pos = (self.width, (self.height / self.__size) * height_indent)
            pygame.draw.line(self.screen, black_color, start_pos, end_pos, 3)
        pygame.display.flip()

    def draw_winner(self, winner):
        screen = pygame.display.set_mode(self.screen_size)
        screen.fill(white_color)
        f1 = pygame.font.Font(None, 72)
        if winner == 'X':
            X_win = f1.render('Победили X!!', True,
                              (180, 0, 0))
            screen.blit(X_win, (10, 50))
            pygame.display.flip()
        elif winner == 'O':
            O_win = f1.render('Победили O!!', True,
                              (180, 0, 0))
            screen.blit(O_win, (10, 50))
            pygame.display.flip()
        else:
            draw = f1.render('Ничья', True,
                             (180, 0, 0))
            screen.blit(draw, (10, 50))
            pygame.display.flip()

    def real_board_to_virtual(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        return (y // (self.height // self.__size)) * self.__size + x // (self.width // self.__size)

    def is_sell_free(self, number_sell: int) -> bool:
        if self.field[number_sell] == ' ':
            return True
        else:
            return False

    def find_center_figure(self, cell_number):
        row = cell_number // self.__size
        col = cell_number % self.__size
        x = col * self.cell_width + self.cell_width // 2
        y = row * self.cell_height + self.cell_height // 2
        return x, y


class Player:
    def __init__(self, game_symbol):
        self.game_symbol = game_symbol


class Game:
    def __init__(self, player1, player2):
        self.player_move = player1
        self.player1 = player1
        self.player2 = player2
        self.counter_move = 0

    def make_move(self, cell_number):
        game_board.field[cell_number] = self.player_move.game_symbol
        center_figure = game_board.find_center_figure(cell_number)
        if self.player_move == player1:
            game_board.draw_cross(center_figure)
        else:
            game_board.draw_circle(center_figure)

    def change_move_player(self):
        if self.player_move == player1:
            self.player_move = player2
        else:
            self.player_move = player1

    def check_winner(self):
        winner = ''
        winning_options = [[0, 1, 2],
                           [3, 4, 5],
                           [6, 7, 8],
                           [0, 3, 6],
                           [1, 4, 7],
                           [2, 5, 8],
                           [0, 4, 8],
                           [2, 4, 6]]
        for i in winning_options:
            if game_board.field[i[0]] == 'X' and game_board.field[i[1]] == 'X' and game_board.field[i[2]] == 'X':
                winner = 'X'
            if game_board.field[i[0]] == 'O' and game_board.field[i[1]] == 'O' and game_board.field[i[2]] == 'O':
                winner = 'O'
            elif self.counter_move == 9:
                winner = 'draw'
        return winner

    def start_game(self):
        game_board.draw_field()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = event.pos
                    cell_number = game_board.real_board_to_virtual(mouse_pos)
                    if game_board.is_sell_free(cell_number) is True:
                        self.counter_move += 1
                        self.make_move(cell_number)
                        self.change_move_player()
                        if self.check_winner() != '':
                            winner = self.check_winner()
                            game_board.draw_winner(winner)


game_board = GameBoard(600, 600)
player1 = Player('X')
player2 = Player('O')
game = Game(player1, player2)
game.start_game()
