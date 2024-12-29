#Guess a word game
import random
animals = ["cat", "dog", "elephant", "lion", "tiger"]
fruits = ["apple", "banana", "cherry", "grape", "mango"]
stationery = ["pen", "pencil", "eraser", "notebook", "marker"]


wordList = animals + fruits + stationery

word = random.choice(wordList)
if word in animals:
    print("Hint-It is a animal")
elif word in fruits:
    print("Hint-It is a fruit")
else:
    print("Hint-It is a stationery item")

guessedWord = ['_'] * len(word)

attempts = 10

while attempts > 0:
   
    print("\nCurrent word: " + ' '.join(guessedWord))

    guess = input("Guess a letter: ").lower()
   
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Great guess!")
    else:
        attempts -= 1
        print("Wrong guess! Attempts left: " + str(attempts))
    if '_' not in guessedWord:
        print("\nCongratulations!! You guessed the word: " + word)
        break
else:
    print("\nYou've run out of attempts! The word was: " + word)
