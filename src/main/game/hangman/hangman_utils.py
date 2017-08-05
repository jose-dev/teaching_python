import random
from os import system, listdir
from os.path import isfile, join


def read_file_with_words(filename):
    filein = open(filename, 'r')
    words = []
    for line in filein.readlines():
        words.append(line.strip('\n'))
    return words


def collect_dictionaries_from_directory(pathin="resources/"):
    dictionaries = []
    for f in sorted(listdir(pathin)):
        if isfile(join(pathin, f)):
            filepath = join(pathin, f)
            name = ((f.replace('.txt', '')).replace('_', ' ')).upper()
            dictionaries.append({'name': name, "file": filepath})
    return dictionaries


def all_words_done(words=None, already_done=[]):
    return len(words) == len(already_done)


def select_new_random_word(words=None, already_done=[]):
    possible_words = filter(lambda x: x not in already_done, words)
    return select_random_word(possible_words)


def select_random_word(words=None):
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
