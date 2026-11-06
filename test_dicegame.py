# test_dicegame.py
# Unit tests for DiceGame assignment

'''
A unit test is a type of software test that checks whether an individual part of a program—called a unit (such as a function, method, or class)—works correctly on its own.

A unit test verifies that a specific piece of code produces the expected output for a given input.

'''

import unittest
from main import Die, DiceGame

class TestDie(unittest.TestCase):
    def test_roll_within_bounds(self):
        die = Die(sides=6)
        for _ in range(100):
            roll = die.roll()
            self.assertIn(roll, range(1, 7))

class TestDiceGame(unittest.TestCase):
    def setUp(self):
        self.game = DiceGame()

    def test_evaluate_win(self):
        for total in [7, 11]:
            self.assertEqual(self.game.evaluate_roll(total), "Win")

    def test_evaluate_lose(self):
        for total in [2, 3, 12]:
            self.assertEqual(self.game.evaluate_roll(total), "Lose")

    def test_evaluate_roll_again(self):
        for total in [4, 5, 6, 8, 9, 10]:
            self.assertEqual(self.game.evaluate_roll(total), "Roll Again")


    def test_die_default_sides(self):
        die = Die()
        self.assertEqual(die.sides, 6)


    def test_play_round_output_structure(self):
        result = self.game.play_round()

        self.assertEqual(len(result), 4)

        self.assertIsInstance(result[0], int)

        self.assertIsInstance(result[1], int)

        self.assertIsInstance(result[2], int)

        self.assertIsInstance(result[3], str)

    
    #This tests if two rolls are independently generating random numbers.
    #This will catch errors such as one die always return a unique number.
    def test_two_dice_independent(self):
        roll1_list = []
        roll2_list = []

	#try 50 games
        for _ in range(50):
            roll1, roll2, _, _ = self.game.play_round()
	    #This saves all the numbers returned by each die.
            roll1_list.append(roll1)
            roll2_list.append(roll2)
        #Test if unique return numbers from each die are more than 1
        #Less likely for 50 trials you always get one same number. If so, likely somewhere there is a bug.
        self.assertGreater(len(set(roll1_list)), 1)
        self.assertGreater(len(set(roll2_list)), 1)

    # --- Students: Add 3 more test cases below ---






if __name__ == '__main__':
    unittest.main()
