import random

word = ['Melom', 'Jackfruit', 'Durian',
          'Orange', 'Papaya', 'Tomato',
          'Mango', 'Strawberry', 'Grape', 'Cherry']
correct_word = random.choice(word)

store_fruit = ''
limit = 5

print('Welcome to "Guess the Fruit Game!"')
print('You have 5 attempts at guessing fruit in a word')
print('Let\'s begin!')
print()

for guess_count in range(limit):
    while True:
        fruit_guess = input('Guess a fruit: ')

        if len(fruit_guess) == 1:
            break
        else:
            print("Oops! Guess a fruit!")

    if fruit_guess in correct_word:
        print('yes!')
        store_fruit += fruit_guess
    else:
        print('no!')

print()
print('Now its time to guess. You have guessed', len(store_fruit), 'fruits correctly.')
print('These fruits are: ', store_fruit)

word_guess = input('Guess the whole word: ')
if word_guess.lower() == correct_word:
    print('Congrats!')
else:
    print('Unlucky! The answer was,', correct_word)

print()
input('Press Enter to leave the program')