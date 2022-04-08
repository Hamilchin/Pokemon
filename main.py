import data
import time
import random as rand

class Pokemon:
  def __init__(self,name,level):
    '''
    takes in species and level and makes an instance of the Pokemon class
    '''
    self.name = name
    self.types = data.CHARACTERS[self.name]["Type"]
    self.baseHP = data.CHARACTERS[self.name]["HP"]
    self.moves = data.CHARACTERS[self.name]["Moves"]
    self.baseattack = data.CHARACTERS[self.name]["Attack"]
    self.basedefense = data.CHARACTERS[self.name]["Defense"]
    self.basespeed = data.CHARACTERS[self.name]["Speed"]
    self.xp = level ** 3 + .00001
    self.nickname = name

  def setnickname(self):
    '''
    take a user input to set the pokemon's nickname
    '''
    while True:
      poss = input(f"What would you like to name your {self.name}? ")
      yn = input(f"{poss} sounds like a great name. Are you sure? [y]/[n] ").lower()
      if yn not in "yn":
        print("invalid input. ")
      elif yn == "y":
        break
    self.nickname = poss
    
  @property
  def HP(self): 
    '''
    Set the max HP as a property of the Pokémon. The HP stat in Pokémon is calculated in a special way that scales based on the level
    '''
    return int((2*self.baseHP*self.level)//100 + self.level + 10)
  
  @property
  def atk(self): 
    '''
    All the other stats also scale based on the level, but in a slightly different way than HP
    '''
    return int((2*self.baseattack*self.level)//100 + 5)
  
  @property
  def defense(self): 
    return int((2*self.basedefense*self.level)//100 + 5)

  @property
  def speed(self): 
    return int((2*self.basespeed*self.level)//100 + 5)

  @property
  def level(self):
    '''
    The level stat is calculated using the xp of the pokemon
    '''
    level = int((self.xp ** (1 / 3))//1)
    return level if level < 100 else 100
  
  def damage_calc(self, movename, defender):
    '''
    calculate the damage dealt by a move given the attacker, move used, and defender
    '''
    attacker = self
    random = rand.randint(85, 100)/100
    critical = 2 if rand.randint(0, 511) < attacker.basespeed else 1 # random chance for critical hit which doubles damage
    typee = 1
    movetype = data.MOVES_DICTIONARY[movename]["type"]
    stab = 1.5 if movetype in self.types else 1 # STAB (same type attack bonus) is a mechanic in Pokémon where an attack deals 1.5x damage if the move is the same type as the attacking pokemon
    for i in defender.types:
      typee *= data.EFFECTIVE[movetype][i]
    modifier = critical * random * typee * stab
    damage = (((2*attacker.level/5 + 2) * data.MOVES_DICTIONARY[movename]["power"] * attacker.atk/defender.defense)/50) * modifier #calculate final damagee
    return round(damage)
    
  def battle(self, other):
    '''
    A function takes in 2 pokemon and initiates a battle.
    Updates your pokemon's XP if won
    Returns:
    True/False
    '''
    print(f"You stumbled upon a wild Lvl {other.level} {other.name}!")
    selfHP = self.HP #temporarily sets alterable variables for HP
    otherHP = other.HP

    while selfHP > 0 and otherHP > 0:
      
      print(f"{self.nickname}'s HP:")
      percentage = round(selfHP/self.HP * 100)
      x = round(percentage/5)
      print('[' + x*"█" + (20-x)*" " + "]" + str(percentage) + "%") #prints healthbar
      print(f"The opponent {other.name}'s HP:")
      percentage = round(otherHP/other.HP * 100)
      x = round(percentage/5)
      print('[' + x*"█" + (20-x)*" " + "]" + str(percentage) + "%")

      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("YOUR MOVES:")
      
      tags = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      for indx, move in enumerate(self.moves):
        print(f"[{tags[indx]}] : {move}") #prints all possible moves, including a tag for input

      movetag = input("What move would you like to choose? ")
      
      print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

      if self.speed >= other.speed: #checking which speed is higher; whoever's speed is higher goes first
        move = self.moves[tags.index(movetag.upper())] #finds the move given the tag input
        damage = self.damage_calc(move, other) #calculates damage
        print(f"{self.nickname} dealt {damage} damage to {other.nickname} using {move}.") #prints info
        otherHP -= damage #updates health
        if otherHP <= 0: #checks if defending pokemon is knocked out
          break
        othermove = rand.choice(other.moves)# if not, continues with the damage dealt by defending pokemon
        otherdamage = other.damage_calc(othermove, self)
        print(f"{other.nickname} dealt {otherdamage} damage to {self.nickname} using {othermove}.")
        selfHP -= otherdamage
        
      elif other.speed > self.speed: #same here
        othermove = rand.choice(other.moves)
        otherdamage = other.damage_calc(othermove, self)
        print(f"{other.nickname} dealt {otherdamage} damage to {self.nickname} using {othermove}.")
        selfHP -= otherdamage
        if selfHP <= 0:
          break
        move = self.moves[tags.index(movetag.upper())]
        damage = self.damage_calc(move, other)
        print(f"{self.nickname} dealt {damage} damage to {other.nickname} using {move}.")
        otherHP -= damage

    if otherHP <= 0: #checks if won
      expgain = int((data.CHARACTERS[other.nickname]["Experience"] * other.level)//7)
      print(f"You won the battle! {other.nickname} was knocked out. {other.nickname} will be added to your collection. {self.nickname} gained {expgain} exp. ")
      self.xp += expgain #updates the XP of your pokemon
      return True
    print(f"You lost the battle! {self.nickname} was knocked out. {self.nickname} will be removed from your collection. ")
    return False

  def __str__(self):
    return f"{self.nickname} ({self.name}) - level: {self.level}, HP: {self.HP}, attack: {self.atk}, defense: {self.defense}, speed: {self.speed}"


class Team:
  def __init__(self,starter):
    self.pokemon = [starter] # make a list of the player's Pokémon that starts out with the starter

  def remove(self, name):
    '''
    Takes in: nickname of a Pokémon in the user's party
    doesn't return anything but removes the pokemon from the team list
    '''
    for poke in self.pokemon:
      if poke.nickname == name:
        self.pokemon.remove(poke)

  def __iadd__(self,poke):
    '''
    the += function
    takes in a pokemon and adds it to the team list
    '''
    self.pokemon.append(poke)
    return self

  def __getitem__(self,key):
    '''
    method for indexing the list using square brackets
    works the same as a normal list (team[key] = team.pokemon[key])
    '''
    return self.pokemon[key]

  def __len__(self):
    '''
    returns the amount of pokemon in the team (the length of the team list)
    '''
    return len(self.pokemon)

  def __str__(self):
    '''
    string representation of the team for the user to see
    '''
    
    string = "The pokemon in your collection are:\n"
    for i,poke in zip(range(1,len(self) + 1),self.pokemon):
      string += f"[{i}]:  " + str(poke) + "\n"
    return string

  def choose_battler(self):
    '''
    the player inputs which pokemon they want to choose to go into battle 
    '''
    print(self)
    while True:
      try:
        poke = input("Choose a Pokémon you will bring to battle using the numbers above: ")
        return self[int(poke) - 1]
      except (KeyError,ValueError):
        print("invalid input")

def banner():
  '''
  Prints a large ASCII banner
  '''
  print("                                  ,'\ ")
  print("    _.----.        ____         ,'  _\   ___    ___     ____")
  print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`. ")
  print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
  print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
  print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
  print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
  print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
  print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
  print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
  print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
  print("                                `'                            '-._|")

def forest_scene():
  '''
  Prints an ascii animation of walking through the forest
  '''
  print("                             # #### ####")
  print("                         ### \/#|### |/####")
  print("                         ##\/#/ \||/##/_/##/_#")
  print("                       ###  \/###|/ \/ # ###")
  print("                     ##_\_#\_\## | #/###_/_####")
  print("                    ## #### # \ #| /  #### ##/##")
  print("                     __#_--###`  |{,###---###-~")
  print("                               \ }{")
  print("                                }}{")
  print("                                }}{")
  print("                                {{} ")
  print("                          , -=-~{ .-^- _")
  print("              ", end = "")
  for i in range(36):
    if i == 26:
      print(" 웃 ", end = "")
    time.sleep(0.1)
    print("~", end = "")
  print("~")


def main():
  '''
  Main function to run the game.
  '''
  
  banner() #prints banner
  print("        --------~~~~~~~~=========########========~~~~~~~~--------      ")
  starter_num = input("Welcome to the wonderful world of Pokémon! Choose your starter. Your options: Charmander [1], Squirtle [2], or Bulbasaur [3]: ")
  while starter_num not in "123":
    starter_num = input("Please choose a valid input. Your options: Charmander [1], Squirtle [2], or Bulbasaur [3]: ")
  starter = Pokemon(("Charmander","Squirtle","Bulbasaur")[int(starter_num) - 1],5)
  starter.setnickname() #runs setnickname, prompting user to name their first pokemon
  player_team = Team(starter) #adds that pokemon to the team
  while len(player_team) != 0: # runs a while loop that keeps playing the game until either the user is done or they run out of pokemon
    playing = input("Would you like to run through the forest to find wild Pokémon? (y for continue, n for done playing)? ").lower() # lets the user choose whether they want to continue playing
    while playing not in "yn":
      print("Invalid input.")
      playing = input("Would you like to run through the forest to find wild Pokémon? (y for continue, n for done playing)? ").lower()
    if playing == "n": break #ends the game if the user does not want to continue playing
    forest_scene() #runs the forest animation
    wild = Pokemon(rand.choice(data.POKEMON_NAMES),rand.choice(range(1,int(max([x.level for x in player_team.pokemon])) + 5))) # make a wild pokemon of a random species with a random level between 1 and the level of the user's highest leveled pokemon plus 4
    battler = player_team.choose_battler() # the user chooses which pokemon to bring into battle
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    win = battler.battle(wild)
    if win:
        player_team += wild #adds the other pokemon to the team
        wild.setnickname()
    else:
        player_team.remove(battler.nickname) #removes the pokemon that lost
    if len(player_team) == 0: #if you lose all your pokemon...
        print("\n ~~~~====### You lost all your Pokémon and blacked out. You lose! ###====~~~~")
        break
    all_pokemon = []
    for pokemon in player_team.pokemon:
      if pokemon.name not in all_pokemon:
        all_pokemon.append(pokemon.name)
    if len(all_pokemon) >= 14:#checks if all possible pokemon have been caught
      print("\n   ~~~~====### You caught em' all! Nice job. You win the game! ###====~~~~")
      break
    
  print("                          #######################")
  print("                          # Thanks for playing! #")
  print("                          #######################")
if __name__ == "__main__":
  main()
