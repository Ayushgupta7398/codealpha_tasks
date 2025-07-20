
                            # Task 1 Hungman Game 

import random

# list of predefined animals name 
words_list = ['cat', 'dog', 'elephant', 'giraffe', 'zebra']
  

def Hangman_game ():

 # Randomly select a word
 secret_word = random.choice(words_list)

 # Create a list of underscores to show hidden letters
 guessed_word = ['_'] *len (secret_word)

 # Store guessed letters
 guessed_letters = []

 # number of attempt
 attempts = len(secret_word) + 2 

 print("🎮 Welcome to Hangman!")
 print('Guess the word! HINT: The word is the name of an animal.')

 while attempts > 0 and  "_" in guessed_word:
  print("\nword"," ".join(guessed_word)) # Displays the current state of the word with spaces between letters 
  print("Guessed letters:", ", ".join(guessed_letters)) # show which letters had chosen 
  print(f"Attempts left: {attempts}") # show how many attempts are left 

  guess = input("guess a letter ").lower()

  if  not guess.isalpha():
   print('Please enter only a letter ')
   continue
  elif len(guess)> 1 :
   print("Please enter only one letter at time ")
   continue
  elif  guess in guessed_letters:
   print("You already guess this letter ")
   continue
  
  guessed_letters.append(guess)

  if guess in secret_word:
            print("✅ Correct!")
            attempts -=1
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
  else:
         print("❌ Wrong guess!")
         attempts -= 1

 # Game result
 if "_" not in guessed_word:
     print("\n🎉 Congratulations! You guessed the word:", secret_word)
 else:
     print("\n💀 Game Over! The word was:", secret_word)



# Main loop to allow replaying
while True:
 Hangman_game()
 play_again = input("\n Do you want to play the game agin !(yes/no )").lower()
 if play_again != 'yes':
  print("Thanks for visit and plying ! BYE BYE")
  break 
 











  


