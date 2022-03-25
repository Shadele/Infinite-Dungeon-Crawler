# base game loop for Dungeon Crawler

from random import randint, choices #random elements
from time import sleep #implement delays so the player isnt overwhelmed by text
from character_generator import char_gen #character creation
from enemy_generator import RandomEncounterMonster #monster creation
from ending_generator import death, win #custom endings