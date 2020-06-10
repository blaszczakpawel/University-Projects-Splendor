import functools
import tkinter as tk

import models.GUI.frame as my_frame
import models.GUI.acceptionboard as acception_board

BORDER_LORDS_X = 10
BORDER_LORDS_Y = 10

BORDER_CRYSTAL_X = 10
BORDER_CRYSTAL_Y = 8

LIST_OF_CARDS = [['high', 1], ['medium', 2], ['low', 3]]
LIST_OF_COINS = [[0, 'diamond'], [1, 'ruby'], [2, 'onyx'], [3, 'sapphire'], [4, 'emerald'], [5, 'gold']]
LIST_OF_CRYSTALS = ['diamond', 'ruby', 'onyx', 'sapphire', 'emerald', 'gold']

ACCEPTION_BOARD_PROPERTIES = (3, 1, 100, 0)

class GuiBoard:
    def __init__(self, root, game):
        self.__acception_board = acception_board.AcceptionBoard(root, game)
        self.__acception_board.get_frame().grid(column=ACCEPTION_BOARD_PROPERTIES[0],
                                                row=ACCEPTION_BOARD_PROPERTIES[1],
                                                padx=ACCEPTION_BOARD_PROPERTIES[2],
                                                pady=ACCEPTION_BOARD_PROPERTIES[3])
        self.__main_board_frame = my_frame.MyFrame(root)
        self.__card_board_frame = my_frame.MyFrame(self.__main_board_frame.get_frame())
        self.__card_board_frame.get_frame().grid(row=1, column=0)
        self.__card_coins_frame = my_frame.MyFrame(self.__main_board_frame.get_frame())
        self.__card_coins_frame.get_frame().grid(row=1, column=1)
        self.__main_board = game.get_board()
        self.__crystal_cards = {}
        self.__coins_list = {}
        self.__lords_list = []
        for i in range(4):
            lord = self.__main_board.get_card(0, i)
            self.__lords_list.append(tk.Button(self.__card_board_frame.get_frame(),
                                               image=lord.get_image(),
                                               command=functools.partial(self.__acception_board.execute_move,
                                                                         f"Lord z pozycji {i} ",
                                                                         {'type': "lord", "number":i})))
            self.__lords_list[len(self.__lords_list) - 1].grid(column=i, row=0,
                                                               padx=BORDER_LORDS_X,
                                                               pady=BORDER_LORDS_Y)
            self.__card_board_frame.add_to_widgetes(self.__lords_list[len(self.__lords_list) - 1])
        for i in LIST_OF_CARDS:
            self.__crystal_cards[i[0]] = []
            for j in range(4):
                card = self.__main_board.get_card(i[1], j)
                self.__crystal_cards[i[0]].append(tk.Button(self.__card_board_frame.get_frame(),
                                                            image=card.get_image(),
                                                            command=functools.partial(self.__acception_board.execute_move,
                                                                                      f"Karta z pozycji (x,y)=({j + 1} , {i[1]})",
                                                                                      {'type': "card", "x": j + 1, 'y':i[1]})))
                self.__crystal_cards[i[0]][j].grid(column=j, row=i[1],
                                                   padx=BORDER_CRYSTAL_X, pady=BORDER_CRYSTAL_Y)
                self.__card_board_frame.add_to_widgetes(self.__crystal_cards[i[0]][j])
        for i in LIST_OF_COINS:
            self.__coins_list[i[1]] = tk.Label(self.__card_coins_frame.get_frame(),
                                               text=str(self.__main_board.get_coin_by_type(i[1]).get_count()))
            button = tk.Button(self.__card_coins_frame.get_frame(),
                               image=self.__main_board.get_coin_by_type(i[1]).get_image(),
                               command=functools.partial(self.__acception_board.execute_move,
                                                         f"Moneta o nazwie {i[1]}",
                                                         {'type': "coin", "name":i[1]}))
            self.__coins_list[i[1]].grid(column=1, row=i[0])
            button.grid(column=0, row=i[0], padx=4, pady=4)
            self.__card_coins_frame.add_to_widgetes(self.__coins_list[i[1]])
            self.__card_coins_frame.add_to_widgetes(button)
    def get_frame(self):
        return self.__main_board_frame.get_frame()
    def refresh(self):
        #print("odświerzam Board")
        self.__acception_board.refresh()
        for i in range(4):
            lord = self.__main_board.get_card(0, i)
            self.__lords_list[i].configure(image=lord.get_image())
        for i in LIST_OF_CRYSTALS:
            self.__coins_list[i].configure(
                text=str(self.__main_board.get_coin_by_type(i).get_count()))
        for i in LIST_OF_CARDS:
            for j in range(4):
                card = self.__main_board.get_card(i[1], j)
                self.__crystal_cards[i[0]][j].configure(image=card.get_image())







