# to generate ending messages depending on what killed the player
#... or if they won



def death(player, race, type, alignment, level, mrace, mtype, turns):
    print("You have died.")
    print(f"Farewell, {player}.")
    print(f"{player}, the {race} {type} was killed by a {mrace} {mtype}.")
    print(f"{player}'s alignment was {alignment}.")
    print(f"{player} reached level {level}.")
    print(f"They survived {turns} turns in the Neverending Dungeon.")

def win(player, race, type, alignment, level, turns):
    print("You have found the Amulet of Serpents!")
    print(f"{player}, the {race} {type} found the Amulet of Serpents and acieved fame and fortune.")
    print(f"{player}'s alignment was {alignment}.")
    print(f"{player} reached level {level}.")
    print(f"They survived {turns} turns in the Neverending Dungeon.")