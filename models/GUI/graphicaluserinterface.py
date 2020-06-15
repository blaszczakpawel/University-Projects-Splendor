import tkinter as tk

from models.GUI import guiboard as gui_board
from  models.GUI import guiplayer as gui_player

SCREAN_HEIGH = 600
SCREAN_WEIGHT = 1200

#(column,row,padx,pady)
WIN_BOARD = (2, 0, 0, 0)
BOARD_PROPERTIES = (2, 1, 0, 0)
PLAYER_ONE_PROPERTIES = (1, 2, 70, 0)
PLAYER_TWO_PROPERTIES = (1, 1, 70, 40)

class GraphicalUserInterface:
    def __init__(self, game):
        self.__game = game
        self.__window = self.__set_window()
        self.__set_main_board(self.__window)
    def __set_window(self):
        window = tk.Tk()
        window.geometry(f"{str(SCREAN_WEIGHT)}x{str(SCREAN_HEIGH)}")
        window.title("Splendor")
        return window
    def __set_main_board(self, root):
        self.__frames = {}
        self.__players_frame = tk.Frame(root)
        self.__players_frame.grid(column=1, row=1)
        for i in [['board', 'board', *BOARD_PROPERTIES],
                  ['player', 'one', *PLAYER_ONE_PROPERTIES],
                  ['player', 'two', *PLAYER_TWO_PROPERTIES]]:
            if i[0] == 'board':
                self.__frames[i[1]] = gui_board.GuiBoard(root, self.__game)
            elif i[0] == 'player':
                self.__frames[i[1]] = gui_player.GuiPlayer(self.__players_frame,
                                                           self.__game.get_player(i[1]), self.__game)
            self.__frames[i[1]].get_frame().grid(column=i[2], row=i[3], padx=i[4], pady=i[5])
    def gui_refresh(self):
        for i in self.__frames:
            self.__frames[i].refresh()
    def win(self, player):
        pom = tk.Label(self.__window, text=f"Wygrał gracz {player}")
        pom.grid(column=WIN_BOARD[0], row=WIN_BOARD[1], padx=WIN_BOARD[2], pady=WIN_BOARD[3])


