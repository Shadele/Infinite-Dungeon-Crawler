# To generate the random enemies in the dungeon
from random import choice, randint
from character_generator import player #to scale monster level based on player level.


class Enemy:
	def __init__(self, race, type, aggression, hp, mp, level):
		self.race = race
		self.type = type
		self.aggression = aggression
		self.hp = hp
		self.mp = mp
		self.level = level

def RandomEncounterMonster():
    monster_races = ("human", "elf", "vampire", "orc", "dwarf", "lizardfolk", "ratkin", "goblin", "drow", "troll")
    monster_classes = ("fighter", "archer", "wizard", "druid", "necromancer", "assassin", "swordsman", "thief", "cultist", "nightwalker", "paladin", "fallen paladin")
    aggression = ("friendly", "neutral", "hostile")
    enemy_race = choice(monster_races)
    enemy_class = choice(monster_classes)
    aggression_level = choice(aggression)




RandomEncounterMonster()
random_monster = Enemy(enemy_race, enemy_class, aggression_level, randint(5,15), randint(0,20), randint(player.level, player.level+3))
