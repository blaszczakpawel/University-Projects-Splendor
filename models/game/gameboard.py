import models.simple.crystalcarddeck as card_deck
import models.simple.lordsdeck as lord_deck
import models.simple.pocket as pocket
import models.simple.coin as coin

GOLD_COINS_START_COUNT = 5
DESOR_COINS_START_COUNT = 7

class GameBoard:
    def __init__(self):
        self.__decks = {}
        self.__cards = [[]]
        self.__coins = pocket.Pocket()
        self.__coins.push(coin.Coin('gold', GOLD_COINS_START_COUNT))
        for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
            self.__coins.push(coin.Coin(i, DESOR_COINS_START_COUNT))
        self.__lords = lord_deck.LordsDeck("cards/LordsList.json")
        for i in [['low', 'cards/LowCrystalList.json'],
                  ['medium', 'cards/MediumCrystalList.json'],
                  ['high', 'cards/HighCrystalList.json']]:
            self.__decks[i[0]] = card_deck.CrystalCardDeck(i[1])
        self.__decks['lords'] = lord_deck.LordsDeck('cards/LordsList.json')
        for i in range(4):
            self.__cards[0].append(self.__lords.getNext())
        for i in [['high', 1], ['medium', 2], ['low', 3]]:
            self.__cards.append([])
            for j in range(4):
                self.__cards[i[1]].append(self.__decks[i[0]].getNext())
    def get_card(self, x_position, y_position):
        return self.__cards[x_position][y_position]
    def get_coin_by_type(self, type):
        return self.__coins.take_coin_by_type(type)
    def get_coins(self):
        return self.__coins
    def remove_card(self, card):
        for i in [['high', 1], ['medium', 2], ['low', 3]]:
            if card in self.__cards[i[1]]:
                self.__cards[i[1]].remove(card)
    def update_cards_and_lords(self):
        if len(self.__cards[0]) < 4:
            self.__cards[0].append(self.__decks['lords'].getNext())
        for i in [['high', 1], ['medium', 2], ['low', 3]]:
            if len(self.__cards[i[1]]) != 4:
                self.__cards[i[1]].append(self.__decks[i[0]].getNext())
    def get_lord_by_id(self, number):
        return self.__cards[0][number]
    def remove_lord(self, lord):
        self.__cards[0].remove(lord)
