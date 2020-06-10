import tkinter as tk
import models.GUI.frame as my_frame

CRYSTAL_LIST_OPTIONS = [['diamond', 1, 5],
                        ['emerald', 1, 4],
                        ['sapphire', 1, 3],
                        ['ruby', 1, 2],
                        ['onyx', 1, 1],
                        ['gold', 1, 6]]
CRYSTAL_LIST = ['diamond', 'emerald', 'sapphire',
                'ruby', 'onyx', 'gold']

class GuiPlayer:
    def __init__(self, root, player, game):
        self.__player = player
        self.__crystals = {}
        self.__frame = my_frame.MyFrame(root)
        self.__board = game.get_board()
        self.__crystals['main'] = {}
        self.__crystals['main']['frame'] = my_frame.MyFrame(self.__frame.get_frame())
        self.__crystals['main']['frame'].get_frame().grid(column=0, row=0)
        self.__crystals['main']['vp'] = tk.Label(
            self.__crystals['main']['frame'].get_frame(), text="VP: 0")
        self.__crystals['main']['vp'].grid(column=0, row=0)
        for i in CRYSTAL_LIST_OPTIONS:
            self.__crystals[i[0]] = {}
            self.__crystals[i[0]]['frame'] = my_frame.MyFrame(self.__frame.get_frame())
            self.__crystals[i[0]]['frame'].get_frame().grid(row=1, column=i[2])
            #lordowie
            self.__crystals[i[0]]['lord'] = tk.Label(self.__crystals[i[0]]['frame'].get_frame())
            self.__crystals[i[0]]['lord'].grid(column=0, row=i[1])
            #coinsy
            coin = self.__player.get_pocket().takeCoinByType(i[0])
            self.__crystals[i[0]]['coinCountLabel'] = tk.Label(
                self.__crystals[i[0]]['frame'].get_frame(), text=coin.getCount())
            self.__crystals[i[0]]['coinCountLabel'].grid(column=0, row=i[1]+1)
            self.__crystals[i[0]]['coinPhotoLabel'] = tk.Label(
                self.__crystals[i[0]]['frame'].get_frame(), image=coin.getImage())
            self.__crystals[i[0]]['coinPhotoLabel'].grid(column=0, row=i[1]+2)
            #cards
            cards = self.__player.get_cards_by_type(i[0])
            self.__crystals[i[0]]['cardsCountLabel'] = tk.Label(
                self.__crystals[i[0]]['frame'].get_frame(), text=len(cards))
            self.__crystals[i[0]]['cardsCountLabel'].grid(column=0, row=i[1]+3)

            self.__crystals[i[0]]['cardsPhotoLabel'] = tk.Label(self.__crystals[i[0]]['frame'].get_frame(),
                                                                image=self.__board.get_card(1, 1).getBack())
            self.__crystals[i[0]]['cardsPhotoLabel'].grid(column=0, row=i[1]+4)

    def get_frame(self):
        return self.__frame.get_frame()
    def refresh(self):
        #print(f"odświerzam gracza {self.__player.getName()}")
        self.__crystals['main']['vp'].configure(text=f"VP: {self.__player.get_victory_points()}")
        lords = self.__player.get_lords()
        counter = 0
        for crystal in CRYSTAL_LIST:
            self.__crystals[crystal]['coinCountLabel'].configure(
                text=self.__player.get_pocket().takeCoinByType(crystal).getCount())
            if len(self.__player.get_cards_by_type(crystal)) > 0:
                self.__crystals[crystal]['cardsCountLabel'].configure(
                    text=len(self.__player.get_cards_by_type(crystal)))
                self.__crystals[crystal]['cardsPhotoLabel'].configure(
                    image=self.__player.get_cards_by_type(crystal)[
                        len(self.__player.get_cards_by_type(crystal)) - 1].getSmallImage())
            else:
                self.__crystals[crystal]['cardsPhotoLabel'].configure(
                    image=self.__board.get_card(1, 1).getBack())
            if counter < len(lords):
                self.__crystals[crystal]['lord'].configure(image=lords[counter].getSmallImage())
                counter += 1