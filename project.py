import random
import sys
from pyfiglet import Figlet
import requests
import json
import config

# Setting up header font 

figlet = Figlet()
fonts = figlet.getFonts()
figlet.setFont(font='ogre')

# Retrieve top rated movies in TheMovieDB

pages = {'results': []}
for i in range(5):
    page = requests.get(f'https://api.themoviedb.org/3/movie/top_rated?api_key={config.api_key}&language=en-US&page={i+1}').json()
    pages['results'].extend(page['results'])

# Create a list that will contain the names of the movies to be guessed by the player

list_of_movies = []

for result in pages['results']:
    if result['original_language'] == 'en' and len(result['title']) < 40:
        list_of_movies.append(result['title'].strip())

def main():
    print(figlet.renderText('Welcome to\n Movie\n Hangman!'))

    while True:
        user_input = input('Press s to start a new game or e to exit: ').strip()
        try:
            start = start_new_game(user_input)
        except ValueError:
            print('Invalid input')
            continue
        else:
            if start:
                movie_to_guess = get_movie(list_of_movies)
                game(movie_to_guess)
            else:
                sys.exit()

# Checks user input on the main screen to start a new game, exit the program or ask for input again if it was not valid

def start_new_game(play):
    if play.lower() == "s":
        print("Good luck!")
        return True
    elif play.lower() == "e":
        print("Ok. Goodbye!")
        return False
    else:
        raise ValueError('Invalid input')

# Selects a random movie from the list if available movies

def get_movie(list_of_movies):
    return random.choice(list_of_movies)

# Returns a list containing a '_' for each letter in the movie to guess

def hide_movie(movie):
    hidden_movie = ['_' if letter.isalpha() else letter for letter in movie]
    return hidden_movie

# Starts up a game of Hangman.

def game(title):

    hidden_movie = hide_movie(title) # a list containing a '_' for each letter in the movie to guess
    movie = title # name of the movie to be guessed as a string
    number_of_guesses = 8 # number of tries that the player has left.
   
    print(f'Your movie contains {hidden_movie.count("_")} letters.')
    print(' '.join(hidden_movie))

    # The following block will run while the player has guesses left. It will be interrupted if the player
    # guesses the correct word before running out of guesses.

    while number_of_guesses > 0:

        # As long as there are any '_' remaining in hidden_movie , the player will be asked to make a guess.

        if '_' in hidden_movie:

            print(f"You have {number_of_guesses} {'guess' if number_of_guesses == 1 else 'guesses'} left")
            user_guess = input('Enter a letter:').lower().strip()
            result = play_round(user_guess, movie, hidden_movie)
            if result is None:
                print(' '.join(hidden_movie))
                continue
            elif result:
                # If the player's guess was correct, any '_' in hidden_movie will be replaced with the correct letter
                indices = [i for i, x in enumerate(movie) if x.lower() == user_guess]
                for index in indices:
                    hidden_movie[index] = movie[index]
                print(' '.join(hidden_movie))
            else:
                number_of_guesses -= 1
                print(' '.join(hidden_movie))

        # If there aren't any '_' left in hidden_movie it means that all the letters have been
        # discovered and the player has won.

        else:
            print('You win!')
            break

    # If the player doesn't have any guesses left, a message including the correct word is shown.

    if number_of_guesses == 0:
        print(f"You Lose! The movie was {movie}")

def play_round(guess, title, hidden_title):

    if len(guess) != 1 or not guess.isalpha() :
        print('Invalid input. Please enter a letter')  
        return None

    elif guess in hidden_title or guess.upper() in hidden_title:
        print('You already guessed this letter. Try a different one')
        return None

    elif guess in title.lower():
        print('Correct!')
        return True

    elif guess not in title.lower():
        print('Wrong! Try again!')
        return False
        
if __name__ == '__main__':
    main()
