# Movie Hangman

## Description

A hangman game in Python where you have to guess movie titles from [TheMovieDB](https://www.themoviedb.org/?language=en-GB) top rated movies.
This is my final project for Harvard University [CS50p Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/)

## Prerequisites

You will need an API Key from TheMovieDB. 
[Create your API key](https://developers.themoviedb.org/3/getting-started/introduction)
You can enter the api-key in the env file.

```
TMDB_API_KEY="<your api_key>"
# replace <your api_key> with your own api-key
```

## Libraries

- random: [https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)
- sys: [https://docs.python.org/3/library/sys.html](https://docs.python.org/3/library/sys.html)
- Figlet: [https://pypi.org/project/pyfiglet/0.7/](https://pypi.org/project/pyfiglet/0.7/)
- requests: [https://pypi.org/project/requests/](https://pypi.org/project/requests/)
- json: [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html)
- os: [https://docs.python.org/3/library/os.html](https://docs.python.org/3/library/os.html)
- dotenv: [https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/)

## Usage

```python project.py```

Welcome screen:

 ```
 __    __     _                            _
/ / /\ \ \___| | ___ ___  _ __ ___   ___  | |_ ___
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \
 \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/

                    _
   /\/\   _____   _(_) ___
  /    \ / _ \ \ / / |/ _ \
 / /\/\ \ (_) \ V /| |  __/
 \/    \/\___/ \_/ |_|\___|

                                                  _
   /\  /\__ _ _ __   __ _ _ __ ___   __ _ _ __   / \
  / /_/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ /  /
 / __  / (_| | | | | (_| | | | | | | (_| | | | /\_/
 \/ /_/ \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_\/
                    |___/

Press s to start a new game or e to exit: 
```

If the user enters s/S, a new game of Hangman will start and they will be asked to enter a letter:

```
Good luck!
Your movie contains 16 letters.
_ _ _   _ _ _ _ _   _ _ _ _ _ _ _ _
You have 8 guesses left
Enter a letter:
```

Correct guess:

```
Enter a letter:t
Correct!
T _ _   _ _ _ _ t   _ _ _ t _ t _ _
You have 8 guesses left
Enter a letter:
```

Incorrect guess:

```
Enter a letter:w
Wrong! Try again!
T _ _   _ _ _ _ t   _ _ _ t _ t _ _
You have 7 guesses left
Enter a letter:
```

Invalid guess:

```
Enter a letter:aa
Invalid input. Please enter a letter
T _ _   _ _ _ _ t   _ _ _ t _ t _ _
You have 7 guesses left
Enter a letter:
```

Letter has already been guessed:

```
Enter a letter:t
You already guessed this letter. Try a different one
T _ _   _ _ _ _ t   _ _ _ t _ t _ _
You have 7 guesses left
Enter a letter:
```

The game will continue until all the letters have been discovered or if the player runs out of guesses. Finally, they will be asked if they want to start a new game or exit.

```
Correct!
T h e   G r e a t   D i c t a t o r
You win!
Press s to start a new game or e to exit:
```