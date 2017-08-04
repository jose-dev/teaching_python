from game.hangman import hangman_game
import unittest

class HangmanGameTest(unittest.TestCase):

    def test_word_to_letters(self):
        word = 'hello'
        expected = ['h', 'e', 'l', 'l', 'o']
        self.assertEqual(hangman_game.word_to_letters(word), expected)


    def test_letters_to_word(self):
        letters = ['h', 'e', 'l', 'l', 'o']
        expected = 'hello'
        self.assertEqual(hangman_game.letters_to_word(letters), expected)


    def test_hide_word(self):
        word = 'hello'
        expected = '.....'
        self.assertEqual(hangman_game.hide_word(word), expected)


    def test_word_has_letter(self):
        letter = 'o'
        word = 'hello'
        self.assertTrue(hangman_game.word_has_letter(word, letter))


    def test_word_does_not_have_letter(self):
        letter = 'i'
        word = 'hello'
        self.assertFalse(hangman_game.word_has_letter(word, letter))


    def test_place_answered_letter(self):
        answer = 'hello'
        guess = 'h...o'
        letter = 'l'
        expected = 'h.llo'
        self.assertEqual(hangman_game.place_answered_letter(answer, guess, letter), expected)


    def test_word_has_not_been_guessed_yet(self):
        word_to_guess = 'hello'
        answer_so_far = 'h...o'
        self.assertFalse(hangman_game.word_has_been_guessed(word_to_guess, answer_so_far))


    def test_word_has_been_guessed(self):
        word_to_guess = 'hello'
        answer_so_far = 'hello'
        self.assertTrue(hangman_game.word_has_been_guessed(word_to_guess, answer_so_far))


    def test_all_words_have_not_been_guessed_yet(self):
        all_words = ['hello', 'world']
        already_done = ['hello']
        self.assertFalse(hangman_game.all_words_done(all_words, already_done))


    def test_all_words_have_been_guessed(self):
        all_words = ['hello', 'world']
        already_done = ['hello', 'world']
        self.assertTrue(hangman_game.all_words_done(all_words, already_done))


    def test_select_new_random_word(self):
        all_words = ['hello', 'world']
        already_done = ['hello']
        expected = 'world'
        self.assertEqual(hangman_game.select_new_random_word(all_words, already_done), expected)
