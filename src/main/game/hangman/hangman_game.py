import random
from os import system

#WORDS = ['rojo', 'verde', 'amarillo', 'negro', 'gris', 'azul']
WORDS = ['rojo', 'verde', 'amarillo']
ALLOWED_NUMBER_OF_WRONG_GUESS = 5


def all_words_done(words=WORDS, already_done=[]):
    return len(words) == len(already_done)

def select_new_random_word(words=WORDS, already_done=[]):
    possible_words = filter(lambda x: x not in already_done, words)
    return select_random_word(possible_words)

def select_random_word(words=WORDS):
    return random.choice(words)

def word_to_letters(word):
    return list(word)

def letters_to_word(letters):
    return ''.join(letters)

def hide_word(word):
    return '.' * len(word)

def word_has_letter(word, letter):
    return letter in word


def place_answered_letter(word_to_guess, answer_so_far, letter_guess):
    word_to_guess = word_to_letters(word_to_guess)
    answer_so_far = word_to_letters(answer_so_far)
    for i in range(len(word_to_guess)):
        if word_to_guess[i] == letter_guess:
            answer_so_far[i] = letter_guess
    return letters_to_word(answer_so_far)


def word_has_been_guessed(word_to_guess, answer_so_far):
    return word_to_guess == answer_so_far


def messages_to_player(message=None, talk=False):
    if talk:
        system("say {0}".format(message))
    else:
        print(message)


if __name__ == "__main__":

    messages_to_player("Let's play hangman...")

    words_done = []
    play_on = True
    while play_on:
        number_of_guess_left = ALLOWED_NUMBER_OF_WRONG_GUESS
        wrong_guess = []
        word_to_guess = select_new_random_word(words=WORDS, already_done=words_done)
        answer_so_far = hide_word(word_to_guess)
        words_done.append(word_to_guess)
        while number_of_guess_left > 0 and not word_has_been_guessed(word_to_guess, answer_so_far):
            # messages to user
            messages_to_player("Word to guess: {0}".format(answer_so_far))
            if len(wrong_guess) > 0:
                messages_to_player("Letters not in word: {0}".format(letters_to_word(wrong_guess)))
            messages_to_player("you have {0} chances left".format(str(number_of_guess_left)))
            letter_guess = raw_input('Enter guess: ')
            print("\n\n\n")

            # check that the letter is part of word to guess
            if word_has_letter(word_to_guess, letter_guess):
                messages_to_player("Well done the letter {0} is in the word".format(letter_guess))
                answer_so_far = place_answered_letter(word_to_guess, answer_so_far, letter_guess)
                if word_has_been_guessed(word_to_guess, answer_so_far):
                    messages_to_player("splendid, you guessed that the word: {0}".format(word_to_guess))
            else:
                messages_to_player("the letter {0} is not in the word".format(letter_guess))
                wrong_guess.extend(letter_guess)
                number_of_guess_left = number_of_guess_left - 1
                if number_of_guess_left == 0:
                    messages_to_player("no more chances my friend, you are dead!")
                    messages_to_player("The secret word was: {0}".format(word_to_guess))
            print("\n\n\n")

        # decide whether you want or can keep playing
        if all_words_done(WORDS, words_done):
            messages_to_player("Game over. No more words left to guess")
            play_on = False
        else:
            message = raw_input("Would you like another game? (yes or no): ")
            if message == 'no':
                play_on = False
                messages_to_player("Bye bye")




