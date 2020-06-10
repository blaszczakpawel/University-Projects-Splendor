import json
import models.GeneticAlgoritm.Person as Person
import models.neuralNetwork.neuralnetwork as Network

CFG_FOR_NEURAL_NETWORK = (251, 450, 450, 450, 450, 450, 450, 450, 47)
TEACHING_VARIABLE = 0.72

class MainConecotr(Person.Person):
    def __init__(self, number, path, **kwargs):
        super().__init__(number, path)
        self.__moves = None
        self.load_output()
        self.__object = None
        self.__stats = None
        self.__teaches = 0
        for k, v in kwargs.items():
            if k == "Obj":
                self.__object = v
            else:
                raise Exception("Bad argument")
    def get_object(self):
        return self.__object
    def save_object(self):
        if self.__object is None or self.__stats is None:
            raise Exception
        with open(self.getPath()+".json", 'w') as outfile:
            data = {'stats':self.__stats, 'neuralNetwork':self.__object.transform_to_object()}
            json.dump(data, outfile)
            outfile.close()
            del self.__object
            del self.__stats
            self.__object = None
            self.__stats = None
    def load_object(self):
        if self.__stats is not None or self.__object is not None:
            raise Exception
        with open(self.getPath()+".json", 'r') as json_file:
            data = json.load(json_file)
            self.__object = Network.NeuralNetwork()
            self.__object.transform_from_object(data['neuralNetwork'])
            self.__stats = data['stats']
            json_file.close()
            self.__teaches = 0
        if self.__object is None or self.__stats is None:
            raise Exception("Coś nie tak")
    def run(self, game, player):
        input_values_for_network = create_input(game, game.get_actual_player(), game.get_oponent())
        posible_moves = []
        for i in self.__moves:
            pom = {}
            pom['move'] = i
            pom['posible'] = game.move_check(i, player)
            posible_moves.append(pom)
        possible = -1
        count = 0
        while possible == -1:
            output = self.__object.get_output(input_values_for_network)
            highest_score = 0
            count += 1
            #znajdowanie najlepszej odpowiedzi
            for i in range(1, 47):
                if output[i] > output[highest_score]:
                    highest_score = i
            possible = posible_moves[highest_score]['posible']
            #sprawdzanie czy można zrobić inną opcje niż pass
            if highest_score == 46:
                posible_counter = 0
                for i in range(46):
                    if posible_moves[i]['posible'] == 1:
                        posible_counter += 1
                        break
                if posible_counter == 0:
                    break
            #wychodzenie jeśli jest to możliwe
            elif possible == 1:
                break
            #uczenie
            teach = []
            for i in range(47):
                if i == 46:
                    teach.append(-(output[i]*3) if output[i] != 0 else 0)
                elif posible_moves[i]['posible'] == -1:
                    teach.append(-(output[i]*2) if output[i] != 0 else 0)
                else:
                    teach.append((output[i]*2) if output[i] < 0.97 else 0)
            self.__object.back_propagation(TEACHING_VARIABLE, teach)
            self.__teaches += 1
        return posible_moves[highest_score]['move']

    def load_output(self):
        with open("AI\\moves.json", 'r') as json_file:
            moves = json.load(json_file)
            json_file.close()
        self.__moves = moves



def create_input(game, player, oponent):
    output = []
    for i in [player, oponent]:
        output.append(game.get_player(i).get_victory_points())
        for j in ['ruby', 'emerald', 'diamond', 'onyx', 'sapphire']:
            output.append(int(game.get_player(i).get_cards_count_by_type(j)))
            output.append(int(game.get_player(i).get_coin_count_by_type(j)))
        golds = game.get_player(i).get_cards_by_type('gold')
        count = 0
        for gold in golds:
            output += gold.get_stats_for_conector()
            count += 1
        for k in range(count, 3):
            output += [0 for l in range(11)]
    # game
    output.append(game.get_round())
    for i in ['ruby', 'emerald', 'diamond', 'onyx', 'sapphire', 'gold']:
        output.append(game.get_board().get_coin_by_type(i).get_count())
    for i in range(0, 4):
        for j in range(1, 4):
            output += game.get_board().get_card(j, i).get_stats_for_conector()
    for i in range(0, 4):
        output += game.get_board().get_card(0, i).get_lords_stats_for_conector()
    return output
