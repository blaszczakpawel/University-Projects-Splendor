import unittest as test

import models.simple.coin as coin

class CoinTest(test.TestCase):
    def test_constructor_1(self):
        testing_object = coin.Coin('emerald', 3)
        self.assertEqual(testing_object.get_type(), 'emerald')
    def test_constructor_2(self):
        testing_object = coin.Coin('emerald', 3)
        self.assertEqual(testing_object.get_count(), 3)
    def test_method_1(self):
        testing_object = coin.Coin('emerald', 4)
        self.assertEqual(testing_object.get_count(), 4)
        testing_object.change_count(3)
        self.assertEqual(testing_object.get_count(), 7)
    def test_str(self):
        testing_object = coin.Coin('emerald', 4)
        self.assertEqual(testing_object.__str__(), '4 of emerald')

if __name__== '__main__':
    test.main()
