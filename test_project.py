from project import hide_movie, start_new_game, play_round
import pytest
import re

def test_start_new_game():
    assert start_new_game('s') == True
    assert start_new_game('S') == True
    assert start_new_game('e') == False
    assert start_new_game('E') == False

def test_start_new_game_invalid_input():  
    with pytest.raises(ValueError):
        start_new_game('w')

def test_hide_movie():
    assert hide_movie('hello') == ['_', '_', '_', '_', '_']
    assert hide_movie('h') == ['_']

def test_play_round():
    hidden_movie = hide_movie('once')
    assert play_round('o', 'once', hidden_movie) == True
    assert play_round('u', 'once', hidden_movie) == False

def test_play_round_uppercase():
    hidden_movie = hide_movie('Once')
    assert play_round('o', 'Once', hidden_movie) == True

def test_play_round_already_guessed():
    assert play_round('o', 'once', ['o', '_', '_', '_']) == None

def test_play_round_invalid():
    assert play_round('oo', 'once', ['_', '_', '_', '_']) == None
    assert play_round('1', 'once', ['_', '_', '_', '_']) == None

    
