from models.neuralNetwork import hiddenlayer as hidden_layer

class NeuralNetwork:
    def __init__(self, **kwargs):
        self.__hidden_layers = []
        for k, v in kwargs.items():
            if k == 'cfg':
                for i in range(1, len(v)):
                    self.__hidden_layers.append(hidden_layer.HiddenLayer(countOfNeurons=v[i], sizeOfInput=v[i - 1]))
    def back_propagation(self, teaching_ratio, teaching_array):
        array = self.__hidden_layers[len(self.__hidden_layers) - 1].back_propagation(teaching_ratio, teaching_array)
        for i in range(len(self.__hidden_layers) - 2, 0, -1):
            array = self.__hidden_layers[i].back_propagation(teaching_ratio, array)
    def random_generate(self):
        for hidden_l in self.__hidden_layers:
            hidden_l.random_generate()
    def get_output(self, array_of_input):
        if len(array_of_input) != self.__hidden_layers[0].get_size_of_input():
            raise Exception("Bad input size")
        pom = array_of_input[:]
        for i in self.__hidden_layers:
            pom = i.get_output(pom)
        return pom
    def transform_to_object(self):
        object = {}
        object['hiddenLayers'] = []
        for hidden_l in self.__hidden_layers:
            object['hiddenLayers'].append(hidden_l.transform_to_object())
        return object
    def transform_from_object(self, object):
        if len(self.__hidden_layers) != 0:
            raise Exception("Błąd w luj")
        for hidden_l in object['hiddenLayers']:
            new_hidden_layer = hidden_layer.HiddenLayer()
            new_hidden_layer.transform_from_object(hidden_l)
            self.__hidden_layers.append(new_hidden_layer)
    def get_hidden_layer(self, index):
        return self.__hidden_layers[index]
    def get_count_of_hidden_layers(self):
        return len(self.__hidden_layers)
    def get_configuration(self):
        cfg = [self.__hidden_layers[0].get_size_of_input()]
        for i in self.__hidden_layers:
            cfg.append(i.get_count_of_neurons())
        return cfg
    def __mul__(self, other):
        if self.get_configuration() != other.get_configuration():
            raise Exception("Bad cfg")
        new_neural_network = NeuralNetwork(cfg=self.get_configuration())
        for i in range(len(new_neural_network.__hidden_layers)):
            new_neural_network.__hidden_layers[i] = self.__hidden_layers[i] * other.__hiddenLayers[i]
        return new_neural_network
