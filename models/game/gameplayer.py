from models.simple import pocket
from models.simple import coin

class Player:
    def __init__(self, name):
        self.__name = name
        self.__victory_points = 0
        self.__lords = []
        self.__pocket = pocket.Pocket()
        self.__cards = {}
        for i in ['diamond', 'emerald', 'sapphire',
                  'onyx', 'ruby', 'gold']:
            self.__pocket.push(coin.Coin(i, 0))
            self.__cards[i] = []
    def get_pocket(self):
        return self.__pocket
    def get_name(self):
        return self.__name
    def get_coin_count_by_type(self, coin_type):
        return self.__pocket.take_coin_by_type(coin_type).get_count()
    def get_card_count(self):
        count = 0
        for card_type in ['diamond', 'emerald', 'sapphire',
                          'onyx', 'ruby', 'gold']:
            count += len(self.__cards[card_type])
        return count
    def get_cards_count_by_type(self, card_type):
        return len(self.__cards[card_type])
    def get_last_card_by_type(self, card_type):
        return self.__cards[card_type][len(self.__cards[card_type])]
    def get_cards(self):
        return self.__cards
    def get_lords(self):
        return self.__lords
    def get_cards_by_type(self, card_type):
        return self.__cards[card_type]
    def add_card(self, card):
        self.__cards[card.get_type()].append(card)
    def add_card_to_reservation(self, card):
        self.__cards['gold'].append(card)
    def add_lord(self, lord):
        self.__lords.append(lord)
    def add_victory_points(self, points):
        self.__victory_points += points
    def get_victory_points(self):
        return self.__victory_points