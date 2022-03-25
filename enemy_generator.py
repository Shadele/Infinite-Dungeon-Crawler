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

def RandomGeneratorMonster():
    monster_races = ("human", "elf", "vampire", "orc", "dwarf", "lizardfolk", "ratkin", "goblin", "drow", "troll")
    monster_classes = ("fighter", "archer", "wizard", "druid", "necromancer", "assassin", "swordsman", "thief", "cultist", "nightwalker", "paladin", "fallen paladin")
    aggression = ("friendly", "neutral", "hostile")
    enemy_race = choice(monster_races)
    enemy_class = choice(monster_classes)
    aggression_level = choice(aggression)
    monster = Enemy(enemy_race, enemy_class, aggression_level, randint(80,110), randint(80, 110), range(player.level,player.level+3))
    return monster

def MonsterEncounter(monster):
    print(f"You have encountered a {monster.race}, {monster.type}.")
    print(f"It looks to be level {monster.level}.")
    if monster.aggression != "hostile":
        print(f"It looks {monster.aggression}.")
    else:
        print("It looks hostile...")
        while player.hp > 0:
            print("It attacks!")
            damage = randint(1, 5) + monster.level
            player.hp -= damage
            if player.hp > 0:
                print(f"You take {damage} damage.\nYou now have {player.hp} HP remaining.")
            else:
                print("You die...")
                break
            print("Do you wish to 1. Fight?\n2. Flee?")