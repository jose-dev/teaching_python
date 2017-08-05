import hangman_utils

ALLOWED_NUMBER_OF_WRONG_GUESS = 5
DICTIONARIES = hangman_utils.collect_dictionaries_from_directory()

def main():
    hangman_utils.messages_to_player("Let's play hangman...")

    # select dictionary to use
    hangman_utils.messages_to_player("Select dictionary")
    for n in range(len(DICTIONARIES)):
        hangman_utils.messages_to_player("{0} - {1}".format(str(n), DICTIONARIES[n]['name']))
    selected_dictionary = int(raw_input('Which dictionary you want? Provide number: '))
    word_dictionary = hangman_utils.read_file_with_words(DICTIONARIES[selected_dictionary]['file'])
    hangman_utils.messages_to_player("\n\n\n")

    # play :)
    words_done = []
    play_on = True
    while play_on:
        number_of_guess_left = ALLOWED_NUMBER_OF_WRONG_GUESS
        wrong_guess = []
        word_to_guess = hangman_utils.select_new_random_word(words=word_dictionary, already_done=words_done)
        answer_so_far = hangman_utils.hide_word(word_to_guess)
        words_done.append(word_to_guess)
        while number_of_guess_left > 0 and not hangman_utils.word_has_been_guessed(word_to_guess, answer_so_far):
            # messages to user
            hangman_utils.messages_to_player("Word to guess: {0}".format(answer_so_far))
            if len(wrong_guess) > 0:
                hangman_utils.messages_to_player("Letters not in word: {0}".format(hangman_utils.letters_to_word(wrong_guess)))
            hangman_utils.messages_to_player("you have {0} chances left".format(str(number_of_guess_left)))
            letter_guess = raw_input('Enter guess: ')
            print("\n\n\n")

            # check that the letter is part of word to guess
            if hangman_utils.word_has_letter(word_to_guess, letter_guess):
                hangman_utils.messages_to_player("Well done the letter {0} is in the word".format(letter_guess), True)
                answer_so_far = hangman_utils.place_answered_letter(word_to_guess, answer_so_far, letter_guess)
                if hangman_utils.word_has_been_guessed(word_to_guess, answer_so_far):
                    hangman_utils.messages_to_player("splendid, you guessed that the word", True)
                    hangman_utils.messages_to_player("The secret word was: {0}".format(word_to_guess), True)
                    hangman_utils.messages_to_player("The secret word was: {0}".format(word_to_guess))
            elif letter_guess not in wrong_guess:
                hangman_utils.messages_to_player("the letter {0} is not in the word".format(letter_guess), True)
                wrong_guess.extend(letter_guess)
                number_of_guess_left = number_of_guess_left - 1
                if number_of_guess_left == 0:
                    hangman_utils.messages_to_player("no more chances my friend, I am afraid you lost!", True)
                    hangman_utils.messages_to_player("The secret word was: {0}".format(word_to_guess), True)
                    hangman_utils.messages_to_player("The secret word was: {0}".format(word_to_guess))
            else:
                hangman_utils.messages_to_player("You already tried the letter {0} before".format(letter_guess), True)

            hangman_utils.messages_to_player("\n\n\n")

        # decide whether you want or can keep playing
        if hangman_utils.all_words_done(word_dictionary, words_done):
            hangman_utils.messages_to_player("Game over. No more words left to guess", True)
            play_on = False
        else:
            message = raw_input("Would you like another game? (yes or no): ")
            if message == 'no':
                play_on = False
                hangman_utils.messages_to_player("Hasta la vista baby", True)
            else:
                hangman_utils.messages_to_player("\n\n\n")


if __name__ == "__main__":
    main()




