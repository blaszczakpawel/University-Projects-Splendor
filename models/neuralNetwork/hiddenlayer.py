import models.neuralNetwork.neurone as Neurone

class HiddenLayer:
    def __init__(self, **kwargs):
        self.__size_of_input = None
        self.__count_of_neurons = None
        self.__array_of_neurons = []
        for k, v in kwargs.items():
            if k == 'sizeOfInput':
                self.__size_of_input = v
            elif k == "countOfNeurons":
                self.__count_of_neurons = v
            elif k == "arrayOfNeurons":
                self.__array_of_neurons = v
            else:
                raise Exception(f"Bad name of argument {k}")
    def random_generate(self):
        if self.__size_of_input is None or \
            self.__count_of_neurons is None or \
            len(self.__array_of_neurons) != 0:
            raise Exception("Hidden Layer is actualy generate")
        for i in range(self.__count_of_neurons):
            new_neurone = Neurone.Neurone(size=self.__size_of_input, teaching=True)
            new_neurone.random_generate()
            self.__array_of_neurons.append(new_neurone)
    def get_neuron_by_index(self, index_of_neuron):
        if index_of_neuron < 0 or index_of_neuron >= len(self.__array_of_neurons):
            raise Exception(f"Index out of neurons range {index_of_neuron} from {len(self.__array_of_neurons)}")
        else:
            return self.__array_of_neurons[index_of_neuron]
    def get_output(self, array_of_input):
        array_of_ouput = []
        for neurone in self.__array_of_neurons:
            array_of_ouput.append(neurone.get_output(array_of_input))
        return array_of_ouput
    def __mul__(self, other):
        if self.__size_of_input != other.__sizeOfInput:
            raise Exception("size of input into layers arent similar")
        if self.__count_of_neurons != other.__countOfNeurons:
            raise Exception("count of neurons isnt similar")
        return HiddenLayer(countOfNeurons=self.__count_of_neurons,
                           sizeOfInput=self.__size_of_input,
                           arrayOfNeurons=[(self.get_neuron_by_index(i) * other.get_neuron_by_index(i))
                                           for i in range(self.__count_of_neurons)])
    def transform_to_object(self):
        object_to_save = {}
        object_to_save['sizeOfInput'] = self.__size_of_input
        object_to_save['countOfNeurons'] = self.__count_of_neurons
        object_to_save['arrayOfNeurons'] = []
        for i in self.__array_of_neurons:
            object_to_save['arrayOfNeurons'].append(i.transform_to_object())
        return object_to_save
    def transform_from_object(self, obj):
        if len(self.__array_of_neurons) != 0:
            raise Exception("You cannot create")
        self.__count_of_neurons = obj['countOfNeurons']
        self.__size_of_input = obj['sizeOfInput']
        self.__array_of_neurons = []
        for i in obj['arrayOfNeurons']:
            new_neurone = Neurone.Neurone()
            new_neurone.transform_from_object(i)
            self.__array_of_neurons.append(new_neurone)
    def back_propagation(self, teaching_ratio, teaching_array):
        array_of_changes = [0 for i in range(self.__size_of_input)]
        for i in range(self.__count_of_neurons):
            for counter, change in enumerate(
                    self.__array_of_neurons[i].back_propagation(teaching_ratio, teaching_array[i]), 0):
                array_of_changes[counter] += change
                counter += 1
        return array_of_changes
    def get_size_of_input(self):
        return self.__size_of_input
    def get_count_of_neurons(self):
        return self.__count_of_neurons