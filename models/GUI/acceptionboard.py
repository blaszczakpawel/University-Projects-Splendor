import tkinter as tk
import functools

import models.GUI.frame as my_frame

class AcceptionBoard:
    def __init__(self, root, game):
        self.__cfg = []
        self.__game = game
        self.__count = 0
        self.__str = tk.StringVar()
        self.__text = "Twój ruch to:\n"
        self.__str.set(self.__text)
        self.__board = my_frame.MyFrame(root)
        self.__board.get_frame().grid(row=1, column=2)
        self.__golden_cards = []
        label = tk.Label(self.__board.get_frame(), textvariable=self.__str)
        label.grid(column=1, row=1)
        self.__board.add_to_widgetes(label)
        for i in range(3):
            self.__golden_cards.append(
                tk.Button(self.__board.get_frame(), command=functools.partial(self.buy_golden_card, i)))
        for i in [["Wyczyść ruch", self.clear_moves, 1, 2],
                  ["Wykup kartę", self.print_golden_cards, 1, 3],
                  ["pass", self.move_pass, 1, 4], ["Akceptuj ruch", self.accept_move, 1, 5]]:
            button = tk.Button(self.__board.get_frame(), text=i[0], command=i[1])
            button.grid(column=i[2], row=i[3])
            self.__board.add_to_widgetes(button)

    def refresh(self):
        self.clear_moves()
        for i in range(3):
            self.__golden_cards[i].grid_remove()

    def print_golden_cards(self):
        counter = 0
        for i in self.__game.get_player('actual').get_cards_by_type('gold'):
            self.__golden_cards[counter].configure(image=i.getSmallImage())
            self.__golden_cards[counter].grid(row=0, column=counter)
            counter += 1

    def buy_golden_card(self, index):
        self.execute_move(f" wykupienie złotej karty o indeksie {index + 1}",
                          {"type": "byGoldenCard", "index": index})

    def get_frame(self):
        return self.__board.get_frame()

    def move_pass(self):
        self.execute_move(" odpuszczenie tej kolejki", {"type": "pass"})

    def clear_moves(self):
        self.__text = "Twój ruch\n"
        self.__str.set(self.__text)
        self.__count = 0
        self.__cfg = []

    def accept_move(self):
        self.__game.move(self.__cfg)

    def execute_move(self, moves_list, cfg):
        self.__count += 1
        if self.__count < 4:
            self.__text += f"{moves_list}\n"
            self.__str.set(self.__text)
            self.__cfg.append(cfg)
        else:
            self.__str.set("Nie za dużo tych ruchów?")