# Concept:
# Build a small console-based word guessing game (kind of like Hangman, but simpler).

# Requirements:
# 	✅1.	Your program randomly picks a word from a list of words (you can hardcode 5–10 words).
# 	✅2.	The player sees underscores for each letter (e.g., _ _ _ _ for “lion”).
# 	✅3.	The player guesses one letter at a time.
# 	4.	If the letter is in the word → reveal it in the correct spot(s).
# 	5.	If the letter is not in the word → count it as a wrong guess.
# 	✅6.	Limit the player to a certain number of wrong guesses (like 6 or 7).
# 	7.	At the end, show whether the player won or lost and reveal the word.

# Bonus (optional for fun):
# 	•	Keep track of all letters guessed so far.
# 	•	Add a little ASCII art for each wrong attempt (stick figure hangman).
# 	•	Let the player play again without restarting the program.
#============================================================================================
# import random
# words = ["lion", "tiger", "wolf", "goat", "buffalo", 
#         "fox", "bird", "cat", "dog", "ferret", "fish", "gerbil", 
#         "guinea", "pig", "hamster", "lizard", "mouse", "rabbit", 
#         "rat", "snake", "turtle"]

# rand = random.choice(words)

# display = ["_"] * len(rand)

# guessed_letters = []
# max_attempt = 7
# attempt_left = max_attempt

# while
# for i in range(len(rand)):
#     print("_ ", end=" ")
    
# def player_guess():
#     for i in range(7):
#         player = input("Please guess a letter: ")
#         for r in rand:
#             if r == player:
#                 print("You are correct!")
#                 print("")
#============================================================================================
#=======================================================================================================
# import random

# # List of words
# words = [
#     "lion", "tiger", "wolf", "goat", "buffalo",
#     "fox", "bird", "cat", "dog", "ferret", "fish", "gerbil",
#     "guinea", "pig", "hamster", "lizard", "mouse", "rabbit",
#     "rat", "snake", "turtle"
# ]

# # Pick a random word
# rand_word = random.choice(words)

# # Create an empty list with underscores for each letter
# display = ["_"] * len(rand_word)

# # Track guessed letters
# guessed_letters = []

# # Set the number of allowed wrong guesses
# max_attempts = 7
# attempts_left = max_attempts

# print("Welcome to the Word Guessing Game!")
# print("Guess the animal name!")
# print("You have", attempts_left, "wrong guesses allowed.\n")

# # Main game loop
# while attempts_left > 0 and "_" in display:
#     print("Current word: ", " ".join(display))
#     print("Guessed letters: ", " ".join(guessed_letters))
    
#     # Take input and ensure it’s a single letter
#     guess = input("\nPlease guess a letter: ").lower()
#     if len(guess) != 1 or not guess.isalpha():
#         print("Please enter only one letter.")
#         continue

#     # Avoid repeating guesses
#     if guess in guessed_letters:
#         print("You already guessed that letter!")
#         continue

#     guessed_letters.append(guess)

#     # Check if guessed letter is in the word
#     if guess in rand_word:
#         print("✅ Correct!")
#         for index, letter in enumerate(rand_word):
#             if letter == guess:
#                 display[index] = guess
#     else:
#         attempts_left -= 1
#         print(f"❌ Wrong! You have {attempts_left} attempts left.")

# # After the loop ends
# if "_" not in display:
#     print("\n🎉 Congratulations! You guessed the word:", rand_word)
# else:
#     print("\n💀 Out of attempts! The correct word was:", rand_word)

#=======================================================================================================

import random

#List
words = [
    "lion", "tiger", "wolf", "goat", "buffalo",
    "fox", "bird", "cat", "dog", "ferret", "fish", "gerbil",
    "guinea", "pig", "hamster", "lizard", "mouse", "rabbit",
    "rat", "snake", "turtle"
]

random_word = random.choice(words)
guessed_word = []
dash = ["_"] * len(random_word)

max_attempt = 8
attempt_left = max_attempt

print("Welcome to the Word Guessing Game!")
print("Guess the animal name!")
print(f"You have {attempt_left} wrong guesses allowed.")

while attempt_left > 0 and "_" in dash:
    print("Current Word: ", " ".join(dash))
    print("Guessed Word: ", " ".join(guessed_word))

    guess = input("Please guess a letter: ")
    if(guess != 1 and not guess.isalpha):
        print("Enter a single digit letter")
        continue

    if guess in guessed_word:
        print("You already guessed that letter")
        continue
    
    guessed_word.append(guess)
    
    if guess in random_word:
        print("💯correct")
        for index, letter in enumerate(random_word):
            if letter == guess:
                dash[index] = guess
    else:
        attempt_left -= 1
        print("❌Wrong, try again")
    

if "_" not in dash:
    print(f"You have guessed the word {random_word}")
else:
    print(f"Sorry, you failed miserably! Correct answer is {random_word}")