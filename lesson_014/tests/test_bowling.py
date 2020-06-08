from bowling import BowlingScore, NotEnoughFrames, StrikeError
import unittest

class BowlingScoreTest(unittest.TestCase):

    def test(self):
        game = BowlingScore('42174/34723/X21X33')
        result = game.run()
        self.assertEqual(result, 109)

    def test_value_error_1(self):
        game = BowlingScore('46174/34723/X21X33')
        result = game.run()
        self.assertEqual(result, ValueError)

    def test_value_error_2(self):
        game = BowlingScore('06174/34723/X21X33')
        result = game.run()
        self.assertEqual(result, ValueError)

    def test_value_error_3(self):
        game = BowlingScore('/6174/34723/X21X33')
        result = game.run()
        self.assertEqual(result, ValueError)

    def test_not_enough_frames(self):
        game = BowlingScore('174/34723/X21X33')
        result = game.run()
        self.assertEqual(result, NotEnoughFrames)

    def test_strike_error(self):
        game = BowlingScore('1X174/34723/X21X33')
        result = game.run()
        self.assertEqual(result, StrikeError)


if __name__ == '__main__':
    unittest.main()