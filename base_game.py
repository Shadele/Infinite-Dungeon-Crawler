# base game loop for Dungeon Crawler

from random import randint, choices #random elements
from time import sleep #implement delays so the player isnt overwhelmed by text
from character_generator import char_gen #character creation
from enemy_generator import RandomEncounterMonster #monster creation
from ending_generator import death, win #custom endings

play_game = True #i want to play a game
turns = 0 #how many turns have we taken
score = 0 #killed anything yet?
hasAmulet = False #win condition

def main():
    char_gen()
    while play_game:
        print("Welcome to the Infinite Dungeon!")