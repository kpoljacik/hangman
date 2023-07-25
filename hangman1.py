#hangman

#user sets lowercase word
hangman_word = "parachute"

#list keeping track of letters guessed
letters_guessed = []
incorrect_guesses = []

def main():
    while not game_lost() and not game_won():
        make_stage()
        word_stage()
        letter = get_guess()
        check_guess(letter, hangman_word)
        
    make_stage()
    if game_lost():
        print("You lose")
    else:
        print("You win!")

#returns true or false depending on if number of guesses exceeds number of hangman body parts
def game_lost():
    allowed_guesses = get_allowed_guesses()
    return len(incorrect_guesses) >= allowed_guesses

#return the number of guesses that are allowed based on stages
def get_allowed_guesses():
    return len(stages) - 1

#returns true or false depending on if all letters guessed
def game_won():
    for character in hangman_word:
        if character not in letters_guessed:
            return False
    return True

#prints stage with body based on number of incorrect guesses      
def make_stage():
    print(stages[len(incorrect_guesses)])

#generates the spaces for the word, e.g. _ _ _ _
def word_stage():
    string_to_print = ""
    # if the character is in the guessed_list, use the character, otherwise use an underscore
    for character in hangman_word:
        if character in letters_guessed:
            string_to_print += character + " "
        else:
            string_to_print += "_ "
    print(string_to_print)
    print("\n")

#guesser inputs letter, letter must meet criteria
def get_guess():
        print("Incorrect guesses:" + str(incorrect_guesses))
        while True:
            print("Enter your letter:")
            guess = input("> ").lower()
            if len(guess) > 1 or not guess.isalpha():
                print("Please guess only one letter")
            elif guess in letters_guessed:
                print("You already guessed this letter. Choose again.")
            else:
                return guess
    
#adds guesses to guess list and incorrect guess list
def check_guess(letter, hangman_word):
    letters_guessed.append(letter)
    if letter not in hangman_word:
        incorrect_guesses.append(letter)
        print("Sorry, bad guess. Try again.")
    else:
        print("""Good guess!
        """)

stage = """
             ____
            |    |
                 |
                 |
                 |
                 |
              ------- 
              """
              
    
head = """
             ____
            |    |
            O    |
                 |
                 |
                 |
              ------- 
              """
              
    
body = """
             ____
            |    |
            O    |
            |    |
                 |
                 |
              ------- 
              """

arm1 = """
             ____
            |    |
           \O    |
            |    |
                 |
                 |
              ------- 
              """

arm2 = """
             ____
            |    |
           \O/   |
            |    |
                 |
                 |
              ------- 
              """
              

leg1 = """
             ____
            |    |
           \O/   |
            |    |
           /     |
                 |
              ------- 
              """
    
leg2 = """
             ____
            |    |
           \O/   |
            |    |
           / \   |
                 |
              ------- 
              """

stages = [stage, head, body, arm1, arm2, leg1, leg2]

main()