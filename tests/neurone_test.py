import unittest as test

from models.neuralNetwork import neurone

class NeuroneTest(test.TestCase):
    def test_get_output(self):
        testing_object = neurone.Neurone(b=2, bias=2, weights=[1, 2, 3, 4, 5, 6])
        self.assertEqual(testing_object.get_output([6, 7, 4, 19, 7, 1]), 1.0)
    def test_get_output2(self):
        testing_object = neurone.Neurone(b=2, bias=2, weights=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(testing_object.get_output([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 0.9820137900379085)
        """Trzy pierwsze testy back propagation sprawdzają czy ustawianie teaching_ratio i teaching_variable daje odpowiednie efekty"""
    def test_back_propagation(self):
        testing_object = neurone.Neurone(b=2, bias=2, weights=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(testing_object.get_output([1, 2, 7, 0, 19, 7.5, 4.32, 9, 181, -1083]), 0.9820137900379085)
        testing_object.back_propagation(0.23,0.5)
        self.assertEqual(testing_object.get_output([1, 2, 7, 0, 19, 7.5, 4.32, 9, 181, -1083]), 0.9856563439365119)
    def test_back_propagaion2(self):
        testing_object = neurone.Neurone(b=2, bias=2, weights=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(testing_object.get_output([1, 2, 7, 0, 19, 7.5, 4.32, 9, 181, -1083]), 0.9820137900379085)
        testing_object.back_propagation(0.23, 0.9)
        self.assertEqual(testing_object.get_output([1, 2, 7, 0, 19, 7.5, 4.32, 9, 181, -1083]), 0.9880381631007614)
    def test_back_propagation3(self):
        testing_object = neurone.Neurone(b=2, bias=2, weights=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(testing_object.get_output([1, 2, 7, 0, 19, 7.5, 4.32, 9, 181, -1083]), 0.9820137900379085)
        testing_object.back_propagation(0.88,0.5)
        self.assertEqual(testing_object.get_output([1, 2, 7, 0, 19, 7.5, 4.32, 9, 181, -1083]), 0.9924602654416266)
    """dwa poniższe testy sprawdzają czy neuron się nie uczy gdy nie musi"""
    def test_back_propagation4(self):
        testing_object = neurone.Neurone(b=2, bias=2, weights=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(testing_object.get_output([1, 2, 7, 0, 19, 7.5, 4.32, 9, 181, -1083]), 0.9820137900379085)
        testing_object.back_propagation(0,0.5)
        self.assertEqual(testing_object.get_output([1, 2, 7, 0, 19, 7.5, 4.32, 9, 181, -1083]), 0.9820137900379085)
    def test_back_propagation5(self):
        testing_object = neurone.Neurone(b=2, bias=2, weights=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(testing_object.get_output([1, 2, 7, 0, 19, 7.5, 4.32, 9, 181, -1083]), 0.9820137900379085)
        testing_object.back_propagation(77,0)
        self.assertEqual(testing_object.get_output([1, 2, 7, 0, 19, 7.5, 4.32, 9, 181, -1083]), 0.9820137900379085)
    def test_transform(self):
        testing_object = neurone.Neurone(b=3, bias=2, weights=[-5, 17, -4.67, 9, 0, -27, -13, 11, 99.2, 37])
        transformation = testing_object.transform_to_object()
        del testing_object
        testing_object_new = neurone.Neurone()
        testing_object_new.transform_from_object(transformation)
        del transformation
        self.assertEqual(testing_object_new.get_size(), 10)
        self.assertEqual(testing_object_new.get_weights_size(), 10)
        self.assertEqual(testing_object_new.get_bias(), 2)
        self.assertEqual(testing_object_new.get_b(), 3)
        self.assertEqual(testing_object_new.get_weights(), [-5, 17, -4.67, 9, 0, -27, -13, 11, 99.2, 37])
    def test_sets(self):
        testing_object = neurone.Neurone(b=3, bias=2, weights=[-5, 17, -4.67, 9, 0, -27, -13, 11, 99.2, 37])
        self.assertEqual(testing_object.get_b(), 3)
        self.assertEqual(testing_object.get_bias(), 2)
        self.assertEqual(testing_object.get_weights(),[-5, 17, -4.67, 9, 0, -27, -13, 11, 99.2, 37])
        testing_object.set_weight(4,17)
        self.assertEqual(testing_object.get_weights(),[-5, 17, -4.67, 9, 17, -27, -13, 11, 99.2, 37])
if __name__ == '__main__':
    test.main()