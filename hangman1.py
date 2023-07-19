#hangman

#need to disallow duplicate letter guesses
#update win condition

def main():
    hangman_word = split_word(word)
    length_hangman_word = word_length(hangman_word)
    while len(incorrect_guesses) < 6 and "_ " in word_stage():
        make_stage()
        letter = get_guess()
        check_guess(letter, hangman_word)
        
    make_stage()
    if len(incorrect_guesses) == 6:
        print("You lose")
    else:
        print("You win!")
    print("hi")
    
    
#user sets lowercase word
word = "parachute"

#list keeping track of letters guessed
letters_guessed = []
incorrect_guesses = []

#splits word into list of letters
def split_word(word):
    hangman_word = [*word]
    return hangman_word

#returns the length of the word
def word_length(hangman_word):
    return len(hangman_word)

#generates the spaces for the word, e.g. _ _ _ _
def word_stage():
    string_to_print = ""
    # if the character is in the guessed_list, use the character, otherwise use an underscore
    for character in word:
        if character in letters_guessed:
            string_to_print += character + " "
        else:
            string_to_print += "_ "
    print(string_to_print)
    return string_to_print

#guesser inputs letter
def get_guess():
        print("Incorrect guesses:" + str(incorrect_guesses))
        print("Enter your letter:")
        guess = input("> ").lower()
        if len(guess) > 1:
            print("Please guess only one letter")
        return str(guess)
    
#adds guesses to guess list and incorrect guess list
def check_guess(letter, hangman_word):
    letters_guessed.append(letter)
    if letter not in word:
        incorrect_guesses.append(letter)
        print("Sorry, bad guess. Try again.")
    elif letter in hangman_word:
        print("""Good guess!
        """)

#prints stage with body based on number of incorrect guesses      
def make_stage():
    print(stages[len(incorrect_guesses)])


stage = """
             ____
            |    |
                 |
                 |
                 |
                 |
              ------- """
              
    
head = """
             ____
            |    |
            O    |
                 |
                 |
                 |
              ------- """
              
    
body = """
             ____
            |    |
            O    |
            |    |
                 |
                 |
              ------- """

arm1 = """
             ____
            |    |
           \O    |
            |    |
                 |
                 |
              ------- """

arm2 = """
             ____
            |    |
           \O/   |
            |    |
                 |
                 |
              ------- """
              

leg1 = """
             ____
            |    |
           \O/   |
            |    |
           /     |
                 |
              ------- """
    
leg2 = """
             ____
            |    |
           \O/   |
            |    |
           / \   |
                 |
              ------- """

stages = [stage, head, body, arm1, arm2, leg1, leg2]

main()