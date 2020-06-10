import json
import random

import models.simple.lord as L

class LordsDeck:
    def __init__(self, path):
        self.__deck = []
        with open(path, 'r') as f:
            distros_dict = json.load(f)
        for i in distros_dict:
            self.__deck.append(L.Lord(i['victoryPoints'], i['photo'], i['coasts']))
    def getNext(self):
        if len(self.__deck) != 0:
            random_number = random.randint(0, len(self.__deck)-1)
            return self.__deck[random_number]

