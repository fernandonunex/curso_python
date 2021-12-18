import unidecode
import random
import os


def read_words():
    """This function read data form a file.
    For this game the words in the file must be one word per line
    Example: 
    Car
    Helicopter
    etc.
    """
    words_crude = []
    with open("./archivos/data.txt", "r") as f:
        words = f.readlines()

    # print(words)
    return words


def choose_a_word(list_of_words):
    # Generating a random number to choose a word from the list words
    n_words = len(list_of_words)
    n = random.randint(0, n_words)
    chose_word_accent = list_of_words[n-1].strip()
    chose_word = unidecode.unidecode(chose_word_accent).upper()
    # print(n_words)
    # print(n)
    # print(choosed_word)

    return chose_word


def comparision_words(word_selected, level):
    len_word = len(word_selected)
    lives_wasted = 0

    #Converting word_selected to a dict
    dict_word = {}
    i = 0
    for word in word_selected:
        dict_word[i] = word
        i += 1
    #print(dict_word)
    
    #Creating a dict empty ("_") for adding words 
    dict_comparision = {i:"_" for i in range(len_word)}

    
    #print(dict_comparision)


    while dict_word != dict_comparision:
        print("Guess the word")
        for value in dict_comparision.values():
            print(f"{value}", end=" ")
        print("\n")

        #Getting a letter from input
        while True:
            try:
                letter_introduced = input("Enter a letter: ").upper()
                if letter_introduced.isalpha():
                    break
                raise ValueError    
            except ValueError:
                print("Pleas enter letter")

        #Checking if the letter is in the word
        if letter_introduced in dict_word.values():
            dict_comparision = dict_comparision|{i:letter_introduced for i in range(len_word) if letter_introduced == dict_word[i]}
            continue
        else:
            print(f"oops, the {letter_introduced} is not in the word :C")

        #If the letter is not in the word selected, then -1 life
        lives_wasted += 1
        if level <= lives_wasted:
            print("You are dead, max lives reached")
            break

def run():
    set_1_words = read_words()
    word_select = choose_a_word(set_1_words)
    os.system("clear")
    print("*** Welcome to HANGMAN GAME **")
    print("Enter how many lives you want 0(infinites) - 9")
    level = 0
    while True:
        try:
            level = int(input(": "))
            if level < 0 or level > 9:
                raise ValueError

        except ValueError:
            print("Please enter a number between 0 - 9")

        else:
            if level == 0:
                print("Now you have infinite lives")
                level = 99
                break
            print(f"Now you have {level} lives ♥")
            break

    comparision_words(word_select, level)


if __name__ == "__main__":
    run()
