import json

from models.game import gameboard as board
from models.game import gameplayer as player
from models.GUI import graphicaluserinterface as gui
from models.conector import mainconector as connector
from models.neuralNetwork import neuralnetwork as network

class Game:
    def __init__(self):
        self.__players = {}
        self.__actual_player = "one"
        self.__board = board.GameBoard()
        self.__round = 0
        self.__is_gui = True
        self.__gui = None
        self.__ai = connector.MainConnecotr(0, 'AI/Brutus')
        self.__ai.load_object()
        for i in ['one', 'two']:
            self.__players[i] = player.Player(i)
    def run(self):
        self.__gui = gui.GraphicalUserInterface(self)
    def __load_ai(self):
        with open("AI/Brutus_0.json", 'r') as json_file:
            data = json.load(json_file)
            pom = network.NeuralNetwork()
            pom.transform_from_object(data['neuralNetwork'])
            self.__ai = connector.MainConnecotr(8, 'AI/Brutus', Obj=pom)
            json_file.close()

    def get_player(self, name_of_player):
        if name_of_player == 'actual':
            return self.__players[self.__actual_player]
        return self.__players[name_of_player]

    def get_actual_player(self):
        return self.__actual_player

    def get_oponent(self):
        if self.__actual_player == 'one':
            return 'two'
        return 'one'

    def get_board(self):
        return self.__board
    def move(self, moves_list):
        self.__move(moves_list)
        if self.__actual_player == 'two':
            self.__move(self.__ai.run(self, 'two'))

    def __move(self, moves_list):
        output = 0
        if len(moves_list) == 1:
            if moves_list[0]['type'] == 'lord':
                output = move_take_lord(self.__board,
                                        self.__players[self.__actual_player], moves_list)
            elif moves_list[0]['type'] == 'card':
                output = move_take_card(self.__board,
                                        self.__players[self.__actual_player], moves_list)
            elif moves_list[0]['type'] == "pass":
                output = 1
            elif moves_list[0]['type'] == 'byGoldenCard':
                output = move_by_golden_card(self.__board,
                                             self.__players[self.__actual_player], moves_list)
            else:
                output = -1
        elif len(moves_list) == 2:
            if moves_list[0]['type'] == 'coin' and moves_list[1]['type'] == 'coin' and\
                    moves_list[0]['name'] == moves_list[1]['name'] and \
                    moves_list[0]['name'] != 'gold':
                output = move_take_two_coins(self.__board.get_coins(),
                                             self.__players[self.__actual_player].get_pocket(),
                                             moves_list)
            elif moves_list[0]['type'] == 'coin' and moves_list[0]['name'] == 'gold' and \
                    moves_list[1]['type'] == 'card':
                output = move_reservation_card(self.__board,
                                               self.__players[self.__actual_player], moves_list)
            else:
                output = -1
        elif len(moves_list) == 3:
            if moves_list[0]['type'] == 'coin' and moves_list[1]['type'] == 'coin' and\
                    moves_list[2]['type'] == 'coin' and\
                    moves_list[0]['name'] != moves_list[1]['name'] and\
                    moves_list[0]['name'] != moves_list[2]['name'] and \
                    moves_list[2]['name'] != moves_list[1]['name'] and \
                    moves_list[0]['name'] != 'gold' and \
                    moves_list[1]['name'] != 'gold' and moves_list[2]['name'] != 'gold':
                output = move_take_coin(self.__board.get_coins(),
                                        self.__players[self.__actual_player].get_pocket(), \
                                        moves_list)
        else:
            raise Exception("Zła ilość poleceń")
        # zamieniam graczy
        if output == 1:
            if self.__actual_player == "one":
                self.__actual_player = "two"
            else:
                self.__actual_player = "one"
                self.__round += 1
                if self.__players['one'].get_victory_points() >= 2 or \
                        self.__players['two'].get_victory_points() >= 2:
                    if self.__players['one'].get_victory_points() > \
                            self.__players['two'].get_victory_points():
                        self.__gui.win('one')
                    if self.__players['one'].get_victory_points() < \
                            self.__players['two'].get_victory_points():
                        self.__gui.win('two')
        if self.__is_gui is True:
            self.__gui.gui_refresh()

    def move_check(self, moves_list, actual_player):
        player_to_check = self.__actual_player
        if actual_player is not None:
            player_to_check = actual_player
        output = 0
        if len(moves_list) == 1:
            if moves_list[0]['type'] == 'lord':
                output = move_take_lord_check(self.__board, self.__players[player_to_check], moves_list)
            elif moves_list[0]['type'] == 'card':
                output = move_take_card_check(self.__board, self.__players[player_to_check], moves_list)
            elif moves_list[0]['type'] == "pass":
                output = 1
            elif moves_list[0]['type'] == 'byGoldenCard':
                output = move_by_golden_card_check(self.__players[player_to_check], moves_list)
            else:
                output = -1
        elif len(moves_list) == 2:
            if moves_list[0]['type'] == 'coin' and moves_list[1]['type'] == 'coin' and \
                moves_list[0]['name'] == moves_list[1]['name'] and moves_list[0]['name'] != 'gold':
                output = move_take_two_coins_check(self.__board.get_coins(),
                                                   self.__players[player_to_check].get_pocket(), moves_list)
            elif moves_list[0]['type'] == 'coin' and moves_list[0]['name'] == 'gold' and moves_list[1]['type'] == 'card':
                output = move_reservation_card_check(self.__board, self.__players[player_to_check])
            else:
                output = -1
        elif len(moves_list) == 3:
            if moves_list[0]['type'] == 'coin' and moves_list[1]['type'] == 'coin' and \
                    moves_list[2]['type'] == 'coin' and moves_list[0]['name'] != \
                    moves_list[1]['name'] and moves_list[0]['name'] != moves_list[2]['name'] and \
                    moves_list[2]['name'] != moves_list[1]['name'] and moves_list[0]['name'] != 'gold' and \
                    moves_list[1]['name'] != 'gold' and moves_list[2]['name'] != 'gold':
                output = move_take_coin_check(self.__board.get_coins(),
                                              self.__players[player_to_check].get_pocket(), moves_list)
        else:
            raise Exception(f"Zła ilość poleceń\n{moves_list}")
        return output

    def get_round(self):
        return self.__round
def move_by_golden_card(game_board, actual_player, move):
    vard_want_to_take = actual_player.get_cards_by_type('gold')[move[0]['index']]
    coast_of_card = vard_want_to_take.get_coasts()
    player_coins = actual_player.get_pocket()
    neaded_resources = {}
    for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
        neaded_resources[i] = coast_of_card.take_coin_by_type(i).get_count()
        # tu powinienem od neededResources odjąć ilość kart danego typu które posiadam
        if (len(actual_player.get_cards_by_type(i)) + player_coins.take_coin_by_type(i).get_count())\
                - neaded_resources[i] < 0:
            #print("nie możesz kupić karty")
            return -1
    #print("Możesz kupić kartę")
    for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
        # tu trzeba będzie odjąć karty
        neaded_resources[i] -= len(actual_player.get_cards_by_type(i))
        if neaded_resources[i] > 0:
            player_coins.take_coin_by_type(i).change_count((-1) * neaded_resources[i])
            game_board.get_coins().take_coin_by_type(i).change_count(neaded_resources[i])
    actual_player.get_cards_by_type('gold').remove(vard_want_to_take)
    actual_player.get_pocket().take_coin_by_type('gold').change_count(-1)
    game_board.get_coins().take_coin_by_type('gold').change_count(1)
    actual_player.add_card(vard_want_to_take)
    actual_player.add_victory_points(vard_want_to_take.get_victory_points())
    return 1
def move_by_golden_card_check(actual_player, moves_list):
    if (len(actual_player.get_cards_by_type('gold'))-1 < moves_list[0]['index'] or \
            len(actual_player.get_cards_by_type('gold')) < 1):
        return -1
    card_want_to_take = actual_player.get_cards_by_type('gold')[moves_list[0]['index']]
    card_coast = card_want_to_take.get_coasts()
    player_coasts = actual_player.get_pocket()
    neaded_resources = {}
    for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
        neaded_resources[i] = card_coast.take_coin_by_type(i).get_count()
        # tu powinienem od neaded_resources odjąć ilość kart danego typu które posiadam
        if (len(actual_player.get_cards_by_type(i)) + player_coasts.take_coin_by_type(i).get_count())\
                - neaded_resources[i] < 0:
            #print("nie możesz kupić karty")
            return -1
    return 1
def move_reservation_card(game_board, actual_player, move):
    if actual_player.get_pocket().coins_count()+1 > 15:
        return -1
    if game_board.get_coins().take_coin_by_type('gold').get_count() == 0:
        return -1
    if len(actual_player.get_cards_by_type('gold')) == 3:
        return -1
    card_want_to_reserv = game_board.get_card(move[1]['y'], move[1]['x'] - 1)
    actual_player.add_card_to_reservation(card_want_to_reserv)
    actual_player.get_pocket().take_coin_by_type('gold').change_count(1)
    game_board.get_coins().take_coin_by_type('gold').change_count(-1)
    game_board.remove_card(card_want_to_reserv)
    game_board.update_cards_and_lords()
    return 1
def move_reservation_card_check(game_board, actual_player):
    if actual_player.get_pocket().coins_count()+1 > 15:
        return -1
    if game_board.get_coins().take_coin_by_type('gold').get_count() == 0:
        return -1
    if len(actual_player.get_cards_by_type('gold')) == 3:
        return -1
    return 1

def move_take_lord(game_board, actual_player, move):
    lord_card = game_board.get_lord_by_id(move[0]['number'])
    lord_coasts = lord_card.get_coasts()
    player_cards = actual_player.get_cards()
    for i in lord_coasts:
        if i['count'] > len(player_cards[i['name']]):
            return -1
    actual_player.add_lord(lord_card)
    game_board.remove_lord(lord_card)
    game_board.update_cards_and_lords()
    actual_player.add_victory_points(lord_card.get_victory_points())
    return 1
def move_take_lord_check(game_board, actual_player, move):
    lord = game_board.get_lord_by_id(move[0]['number'])
    lord_coasts = lord.get_coasts()
    player_cards = actual_player.get_cards()
    for i in lord_coasts:
        if i['count'] > len(player_cards[i['name']]):
            return -1
    return 1
def move_take_two_coins(bord_pocket, player_pocket, moves):
    if bord_pocket.take_coin_by_type(moves[0]['name']).get_count() < 4:
        return -1
    if player_pocket.coins_count()+len(moves) > 15:
        return -1
    bord_pocket.take_coin_by_type(moves[0]['name']).change_count(-2)
    player_pocket.take_coin_by_type(moves[0]['name']).change_count(2)
    return 1
def move_take_two_coins_check(board_pocket, player_pocket, moves):
    if board_pocket.take_coin_by_type(moves[0]['name']).get_count() < 4:
        return -1
    if player_pocket.coins_count()+len(moves) > 15:
        return -1
    return 1
def move_take_coin(board_pocket, player_pocket, moves):
    if player_pocket.coins_count()+len(moves) > 15:
        return -1
    for i in moves:
        for j in board_pocket.get_all_coins():
            if i['name'] == j.get_type():
                if j.get_count() == 0:
                    return -1
                else:
                    break
    for i in moves:
        for j in board_pocket.get_all_coins():
            if i['name'] == j.get_type():
                player_pocket.take_coin_by_type(i['name']).change_count(1)
                j.change_count(-1)
                break
    return 1
def move_take_coin_check(board_pocket, player_pocket, moves):
    if player_pocket.coins_count()+len(moves) > 15:
        return -1
    for i in moves:
        for j in board_pocket.get_all_coins():
            if i['name'] == j.get_type():
                if j.get_count() == 0:
                    return -1
                else:
                    break
    return 1
def move_take_card(game_board, actual_player, move):
    card_want_to_take = game_board.get_card(move[0]['y'], move[0]['x'] - 1)
    card_coasts = card_want_to_take.get_coasts()
    player_coins = actual_player.get_pocket()
    needed_resources = {}
    for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
        needed_resources[i] = card_coasts.take_coin_by_type(i).get_count()
        #tu powinienem od neededResources odjąć ilość kart danego typu które posiadam
        if (len(actual_player.get_cards_by_type(i)) + player_coins.take_coin_by_type(i).get_count())\
                - needed_resources[i] < 0:
            #print("nie możesz kupić karty")
            return -1
    #print("Możesz kupić kartę")
    for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
        #tu trzeba będzie odjąć karty
        needed_resources[i] -= len(actual_player.get_cards_by_type(i))
        if needed_resources[i] > 0:
            player_coins.take_coin_by_type(i).change_count((-1) * needed_resources[i])
            game_board.get_coins().take_coin_by_type(i).change_count(needed_resources[i])
    game_board.remove_card(card_want_to_take)
    game_board.update_cards_and_lords()
    actual_player.add_card(card_want_to_take)
    actual_player.add_victory_points(card_want_to_take.get_victory_points())
    return 1
def move_take_card_check(game_board, actual_player, move):
    card_want_to_take = game_board.get_card(move[0]['y'], move[0]['x'] - 1)
    card_want_to_take_coast = card_want_to_take.get_coasts()
    player_coins = actual_player.get_pocket()
    needed_resources = {}
    for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
        needed_resources[i] = card_want_to_take_coast.take_coin_by_type(i).get_count()
        #tu powinienem od neededResources odjąć ilość kart danego typu które posiadam
        if (len(actual_player.get_cards_by_type(i)) + player_coins.take_coin_by_type(i).get_count())\
                - needed_resources[i] < 0:
            #print("nie możesz kupić karty")
            return -1
    return 1