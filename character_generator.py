#this is where the character generation things live

class PlayerCharacter:
	def __init__(self, name, race, type, alignment, hp, mp, speed, strength, defense, level):
		self.name = name
		self.race = race
		self.type = type
		self.alignment = alignment
		self.hp = hp
		self.mp = mp
		self.speed = speed
		self.strength = strength
		self.defense = defense
		self.level = level

#temporary test character. Eventually choice will be implemented
#but Testbert is here to make sure things work

player = PlayerCharacter(Testbert, human, fighter, neutral, 100, 100, 100, 10, 10, 1)


'''def char_gen():
    print("Would you like to:\n1. Create a character?\n2. Randomly generate a character?")
    print("Select 1 or 2.")
    gen_choice = input()
    player = PlayerCharacter()
    if gen_choice == "1":
        while True:
            print("Choose a character race:")
            print("1. Halfling\n2. Human\n3. Elf\n4. Dwarf\n5. Orc\n6. Drow")
            valid_choice = ["1", "2", "3", "4", "5", "6"]
            race_choice = input()
            if race_choice not in valid_choice:
                print("Invalid choice.")
            else:
                break
        if race_choice == "1":
            PlayerCharacter.race = Halfling
            print(f"You are a {PlayerCharacter.race}. Your current stats are as follows:\nHP: {Halfling.hp}\nMP: {Halfling.mp}\nSpeed: {Halfling.speed}\nStrength: {Halfling.strength}\nDefense: {Halfling.defense}.")
            print(f"Your alignment is {Halfling.alignment}.")
        if race_choice == "2":
            PlayerCharacter.race = "human"
        if race_choice == "3":
            PlayerCharacter.race = "elf"
        if race_choice == "4":
            PlayerCharacter.race = "dwarf"
        if race_choice == "5":
            PlayerCharacter.race = "orc"
        if race_choice == "6":
            PlayerCharacter.race = "drow"
        
        return player'''