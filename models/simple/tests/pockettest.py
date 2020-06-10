import unittest as test

import models.simple.pocket as pocket
import models.simple.coin as coin

class Mook(coin.Coin):
    def __init__(self, type, count):
        pass
    def __str__(self):
        return ""
    def get_type(self):
        return "ruby"
    def get_count(self):
        return 1
    def get_coin(self, count):
        return 0
    def change_count(self, count):
        pass
    def get_image(self):
        raise NotImplementedError
class PocketTest(test.TestCase):
    def test_constructor(self):
        testing_object = pocket.Pocket()
        self.assertEqual(testing_object.get_all_coins(), [])
    def test_get_all_coins(self):
        testing_object = pocket.Pocket()
        mook = Mook('aa', 1)
        testing_object.push(mook)
        self.assertEqual(testing_object.get_all_coins(), [mook])
        mook2 = Mook('bb', 2)
        testing_object.push(mook2)
        self.assertEqual(testing_object.get_all_coins(), [mook, mook2])
    def test_get_count(self):
        testing_object = pocket.Pocket()
        self.assertEqual(testing_object.coins_count(), 0)
        for i in range(4):
            testing_object.push(Mook('aa', 2))
        self.assertEqual(testing_object.coins_count(), 4)
if __name__== '__main__':
    test.main()