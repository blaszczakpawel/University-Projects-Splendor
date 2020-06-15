import math
import random

GENERATE_TRANSITION_FUNCTION_B = 2
GENERATE_BIAS_PROPERTIES = (-300, 300)
GENERATE_BIAS_DIVIDER = 25
GENERATE_SIZE_PROPERTIES = (100, 1000)
GENERATE_WEIGHTS_PROPERTIES = (-100000, 100000)
GENERATE_WEIGHTS_DIVIDER = 5000

TEACHING_NON_ZERO_VARIABLE = 1
TEACHING_PROPORTION = 4
TEACHING_LAYERS_PROPORTION = 0.92

class Neurone:
    def __init__(self, **kwargs):
        self.__size = None
        self.__weights = []
        self.__bias = None
        self.__b = None
        self.__last_input = None
        if "size" in kwargs and "weights" in kwargs:
            raise Exception("You cannot run Neurone with size ane weights arguments")
        for k, v in kwargs.items():
            if k == "size":
                self.__size = v
            elif k == "bias":
                self.__bias = v
            elif k == "weights":
                self.__weights = v
                self.__size = len(self.__weights)
            elif k == "b":
                if v > 0:
                    self.__b = v
                else:
                    raise Exception("b must be larger then 0")
            elif k == "teaching":
                if v is True:
                    self.__last_input = []
                elif v is False:
                    self.__last_input = None
                else:
                    raise Exception("Bad value for teaching variable")
            else:
                raise Exception("This argument does not exist")
    def __calculate_weights_value(self, array):
        self.__last_input = array
        count = self.__bias
        for i in range(len(self.__weights)):
            count += self.__weights[i]*array[i]
        return count
    def __transition_fuction(self, value):
        return (math.tanh(value) + 1) / 2
    def get_output(self, input_array):
        for i in [self.__b, self.__size, self.__bias]:
            if i is None:
                raise Exception("Neuron is not ready for work")
        if type(input_array) != type([]):
            raise Exception("Argument must be array")
        if len(input_array) != self.__size:
            raise Exception("weights array and values array isnt same length")
        return self.__transition_fuction(self.__calculate_weights_value(input_array))
    def get_size(self):
        return self.__size
    def random_generate(self):
        if self.__b is None:
            self.__b = GENERATE_TRANSITION_FUNCTION_B
        if self.__bias is None:
            self.__bias = (random.randint(*GENERATE_BIAS_PROPERTIES)/GENERATE_BIAS_DIVIDER)
        if self.__size is None:
            self.__size = random.randint(*GENERATE_SIZE_PROPERTIES)
        if len(self.__weights) is 0:
            for i in range(self.__size):
                self.__weights.append(random.randint(*GENERATE_WEIGHTS_PROPERTIES)/GENERATE_WEIGHTS_DIVIDER)
    def transform_to_object(self):
        object = {}
        object['przejscie'] = self.__b
        object['neurone'] = {}
        object['neurone']['bias'] = self.__bias
        object['neurone']['weights'] = self.__weights
        object['lastInput'] = self.__last_input
        return object
    def transform_from_object(self, object):
        self.__b = object['przejscie']
        self.__bias = object['neurone']['bias']
        self.__weights = object['neurone']['weights']
        self.__size = len(self.__weights)
        self.__last_input = object['lastInput']
    def __mul__(self, other):
        if type(other) != type(self):
            raise Exception("You cannot multiplay")
        if self.get_size() != other.get_size():
            raise Exception("Size arent similar")
        array = []
        for i in range(self.__size):
            array.append((self.__weights[i]+other.__weights[i])/2)
        return Neurone(weights=array,
                       b=((self.__b+other.__b)/2),
                       bias=((self.__bias+other.__bias)/2))
    def back_propagation(self, teaching_ratio, teaching_variable):
        if self.__last_input is None:
            raise Exception("I cant teach")
        count_of_incrise = 0
        count_of_decrise = 0
        array_of_weights_change = []
        for i in range(self.__size):
            correct_weight = self.__weights[i]\
                if abs(self.__weights[i]) > TEACHING_NON_ZERO_VARIABLE else (-1 if self.__weights[i] < 0 else 1)
            teaching_stable = (correct_weight * self.__last_input[i])
            if teaching_stable > 0 and teaching_variable > 0:
                count_of_incrise += 1
                array_of_weights_change.append((teaching_variable * teaching_ratio * math.fabs(teaching_stable)))
            elif teaching_stable > 0 and teaching_variable < 0:
                count_of_decrise += 1
                array_of_weights_change.append((teaching_variable * teaching_ratio * math.fabs(teaching_stable)))
            elif teaching_stable < 0 and teaching_variable > 0:
                count_of_incrise += 1
                array_of_weights_change.append((teaching_variable * teaching_ratio * math.fabs(teaching_stable)))
            elif teaching_stable < 0 and teaching_variable < 0:
                count_of_decrise += 1
                array_of_weights_change.append((teaching_variable * teaching_ratio * math.fabs(teaching_stable)))
            else:
                array_of_weights_change.append(0)
        if count_of_decrise > TEACHING_PROPORTION * count_of_incrise or \
            count_of_incrise > TEACHING_PROPORTION * count_of_decrise:
            self.__bias += teaching_variable * teaching_ratio
        else:
            for i in range(self.__size):
                self.__weights[i] += array_of_weights_change[i]
                array_of_weights_change[i] *= TEACHING_LAYERS_PROPORTION
        return array_of_weights_change
    def teaching_switch(self):
        if self.__last_input is None:
            self.__last_input = []
        self.__last_input = None
    def set_bias(self, bias):
        self.__bias = bias
    def get_weights_size(self):
        return len(self.__weights)
    def set_weight(self, index, weight):
        self.__weights[index] = weight
    def get_bias(self):
        return self.__bias
    def get_weights(self):
        return self.__weights
    def get_b(self):
        return self.__b