import random
from Hangman_words import word_list
from Hangman_art import logo, stages

chosen_word = random.choice(word_list)

display_list = ['-']*len(chosen_word)

end_of_game = False

lives = 6
print(logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display_list:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        if chosen_word[position]==guess:
            display_list[position] = chosen_word[position]

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display_list)}")

    print(display_list)
    if '-' not in display_list:
        end_of_game = True
        print("You Win")
    print(stages[lives])