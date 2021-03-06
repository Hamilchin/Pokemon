EFFECTIVE = {'Normal': {'Normal': 1 , 'Fighting' : 1, 'Flying' : 1, 'Poison' : 1, 'Ground' : 1,'Rock' : 0.5, 'Bug' : 1, 'Ghost' : 0, 'Steel' : 0.5, 'Fire' : 1, 'Water' : 1, 'Grass' : 1, 'Electric' : 1, 'Psychic' : 1, 'Ice' : 1, 'Dragon' : 1, 'Dark' : 1, 'Fairy' : 1}, 
             'Fighting': {'Normal': 2 , 'Fighting' : 1, 'Flying' : 0.5, 'Poison' : 0.5, 'Ground' : 1,'Rock' : 2, 'Bug' : 0.5, 'Ghost' : 0, 'Steel' : 2, 'Fire' : 1, 'Water' : 1, 'Grass' : 1, 'Electric' : 1, 'Psychic' : 0.5, 'Ice' : 2, 'Dragon' : 1, 'Dark' : 2, 'Fairy' : 0.5},
            'Flying': {'Normal': 1 , 'Fighting' : 2, 'Flying' : 1, 'Poison' : 1, 'Ground' : 1,'Rock' : 0.5, 'Bug' : 2, 'Ghost' : 1, 'Steel' : 0.5, 'Fire' : 1, 'Water' : 1, 'Grass' : 2, 'Electric' : 0.5, 'Psychic' : 1, 'Ice' : 1, 'Dragon' : 1, 'Dark' : 1, 'Fairy' : 1},
            'Poison': {'Normal': 1 , 'Fighting' : 1, 'Flying' : 1, 'Poison' : 0.5, 'Ground' : 0.5,'Rock' : 0.5, 'Bug' : 1, 'Ghost' : 0.5, 'Steel' : 0, 'Fire' : 1, 'Water' : 1, 'Grass' : 2, 'Electric' : 1, 'Psychic' : 1, 'Ice' : 1, 'Dragon' : 1, 'Dark' : 1, 'Fairy' : 2},
            'Ground': {'Normal': 1 , 'Fighting' : 1, 'Flying' : 0, 'Poison' : 2, 'Ground' : 1,'Rock' : 2, 'Bug' : 0.5, 'Ghost' : 1, 'Steel' : 2, 'Fire' : 2, 'Water' : 1, 'Grass' : 0.5, 'Electric' : 2, 'Psychic' : 1, 'Ice' : 1, 'Dragon' : 1, 'Dark' : 1, 'Fairy' : 1},
            'Rock': {'Normal': 1 , 'Fighting' : 0.5, 'Flying' : 2, 'Poison' : 1, 'Ground' : 0.5,'Rock' : 1, 'Bug' : 2, 'Ghost' : 1, 'Steel' : 0.5, 'Fire' : 2, 'Water' : 1, 'Grass' : 1, 'Electric' : 1, 'Psychic' : 1, 'Ice' : 2, 'Dragon' : 1, 'Dark' : 1, 'Fairy' : 1},
            'Bug': {'Normal': 1 , 'Fighting' : 0.5, 'Flying' : 0.5, 'Poison' : 0.5, 'Ground' : 1,'Rock' : 1, 'Bug' : 1, 'Ghost' : 0.5, 'Steel' : 0.5, 'Fire' : 0.5, 'Water' : 1, 'Grass' : 2, 'Electric' : 1, 'Psychic' : 2, 'Ice' : 1, 'Dragon' : 1, 'Dark' : 2, 'Fairy' : 0.5},
            'Ghost': {'Normal': 0 , 'Fighting' : 1, 'Flying' : 1, 'Poison' : 1, 'Ground' : 1,'Rock' : 1, 'Bug' : 1, 'Ghost' : 2, 'Steel' : 1, 'Fire' : 1, 'Water' : 1, 'Grass' : 1, 'Electric' : 1, 'Psychic' : 2, 'Ice' : 1, 'Dragon' : 1, 'Dark' : 1, 'Fairy' : 1},
            'Steel': {'Normal': 1 , 'Fighting' : 1, 'Flying' : 1, 'Poison' : 1, 'Ground' : 1,'Rock' : 2, 'Bug' : 1, 'Ghost' : 1, 'Steel' : 0.5, 'Fire' : 0.5, 'Water' : 0.5, 'Grass' : 1, 'Electric' : 0.5, 'Psychic' : 1, 'Ice' : 2, 'Dragon' : 1, 'Dark' : 1, 'Fairy' : 2},
            'Fire': {'Normal': 1 , 'Fighting' : 1, 'Flying' : 1, 'Poison' : 1, 'Ground' : 1,'Rock' : 0.5, 'Bug' : 2, 'Ghost' : 1, 'Steel' : 2, 'Fire' : 0.5, 'Water' : 0.5, 'Grass' : 2, 'Electric' : 1, 'Psychic' : 1, 'Ice' : 2, 'Dragon' : 0.5, 'Dark' : 1, 'Fairy' : 1},
            'Water': {'Normal': 1 , 'Fighting' : 1, 'Flying' : 1, 'Poison' : 1, 'Ground' : 2,'Rock' : 2, 'Bug' : 1, 'Ghost' : 1, 'Steel' : 1, 'Fire' : 2, 'Water' : 0.5, 'Grass' : 0.5, 'Electric' : 1, 'Psychic' : 1, 'Ice' : 1, 'Dragon' : 0.5, 'Dark' : 1, 'Fairy' : 1},
            'Grass': {'Normal': 1 , 'Fighting' : 1, 'Flying' : 0.5, 'Poison' : 0.5, 'Ground' : 2,'Rock' : 2, 'Bug' : 0.5, 'Ghost' : 1, 'Steel' : 0.5, 'Fire' : 0.5, 'Water' : 2, 'Grass' : 0.5, 'Electric' : 1, 'Psychic' : 1, 'Ice' : 1, 'Dragon' : 0.5, 'Dark' : 1, 'Fairy' : 1},
            'Electric': {'Normal': 1 , 'Fighting' : 1, 'Flying' : 2, 'Poison' : 1, 'Ground' : 0,'Rock' : 1, 'Bug' : 1, 'Ghost' : 1, 'Steel' : 1, 'Fire' : 1, 'Water' : 2, 'Grass' : 0.5, 'Electric' : 0.5, 'Psychic' : 1, 'Ice' : 1, 'Dragon' : 0.5, 'Dark' : 1, 'Fairy' : 1},
            'Psychic': {'Normal': 1 , 'Fighting' : 2, 'Flying' : 1, 'Poison' : 2, 'Ground' : 1,'Rock' : 1, 'Bug' : 1, 'Ghost' : 1, 'Steel' : 0.5, 'Fire' : 1, 'Water' : 1, 'Grass' : 1, 'Electric' : 1, 'Psychic' : 0.5, 'Ice' : 1, 'Dragon' : 1, 'Dark' : 0, 'Fairy' : 1},
            'Ice': {'Normal': 1 , 'Fighting' : 1, 'Flying' : 2, 'Poison' : 1, 'Ground' : 2,'Rock' : 1, 'Bug' : 1, 'Ghost' : 1, 'Steel' : 0.5, 'Fire' : 0.5, 'Water' : 0.5, 'Grass' : 2, 'Electric' : 1, 'Psychic' : 1, 'Ice' : 0.5, 'Dragon' : 2, 'Dark' : 1, 'Fairy' : 1},
             'Dragon': {'Normal': 1 , 'Fighting' : 1, 'Flying' : 1, 'Poison' : 1, 'Ground' : 1,'Rock' : 1, 'Bug' : 1, 'Ghost' : 1, 'Steel' : 0.5, 'Fire' : 1, 'Water' : 1, 'Grass' : 1, 'Electric' : 1, 'Psychic' : 1, 'Ice' : 1, 'Dragon' : 2, 'Dark' : 1, 'Fairy' : 0},
            'Dark': {'Normal': 1 , 'Fighting' : 0.5, 'Flying' : 1, 'Poison' : 1, 'Ground' : 1,'Rock' : 1, 'Bug' : 1, 'Ghost' : 2, 'Steel' : 1, 'Fire' : 1, 'Water' : 1, 'Grass' : 1, 'Electric' : 1, 'Psychic' : 2, 'Ice' : 1, 'Dragon' : 1, 'Dark' : 0.5, 'Fairy' : 0.5},
            'Fairy': {'Normal': 1 , 'Fighting' : 2, 'Flying' : 1, 'Poison' : 0.5, 'Ground' : 1,'Rock' : 1, 'Bug' : 1, 'Ghost' : 1, 'Steel' : 0.5, 'Fire' : 0.5, 'Water' : 1, 'Grass' : 1, 'Electric' : 1, 'Psychic' : 1, 'Ice' : 1, 'Dragon' : 2, 'Dark' : 2, 'Fairy' : 1}}

MOVES_DICTIONARY = {
    'Scratch': 
    {
        'name': 'Scratch',
        'power': 40, 
        'type': 'Normal', 
        'super effective against': ['N/A'], 
        'not very effective against': ['Rock', 'Steel']
    }, 
    'Tackle': 
    {
        'name': 'Tackle',
        'power': 40, 
        'type': 'Normal', 
        'super effective against': ['N/A'], 
        'not very effective against': ['Rock', 'Steel']
    }, 
    'Pound': {'name': 'Pound', 'power': 40, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Rage': {'name': 'Rage', 'power': 20, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Fury Attack': {'name': 'Fury Attack', 'power': 15, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Ember': {'name': 'Ember', 'power': 40, 'type': 'Fire', 'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'], 'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']}, 
    'Fire Spin': {'name': 'Fire Spin', 'power': 35, 'type': 'Fire', 'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'], 'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']}, 
    'Bubble': {'name': 'Bubble', 'power': 40, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'], 'not very effective against': ['Water', 'Grass', 'Dragon']}, 
    'Aqua Jet': {'name': 'Aqua Jet', 'power': 40, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'], 'not very effective against': ['Water', 'Grass', 'Dragon']}, 
    'Thunder Shock': {'name': 'Thunder Shock', 'power': 40, 'type': 'Electric', 'super effective against': ['Water', 'Flying'], 'not very effective against': ['Electric', 'Grass', 'Dragon']}, 
    'Thunderbolt': {'name': 'Thunderbolt', 'power': 90, 'type': 'Electric', 'super effective against': ['Water', 'Flying'], 'not very effective against': ['Electric', 'Grass', 'Dragon']}, 
    'Vine Whip': {'name': 'Vine Whip', 'power': 45, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Magical Leaf': {'name': 'Magical Leaf', 'power': 60, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Ice Shard': {'name': 'Ice Shard', 'power': 40, 'type': 'Ice', 'super effective against': ['Grass', 'Ground', 'Flying', 'Dragon'], 'not very effective against': ['Fire', 'Water', 'Ice', 'Steel']}, 
    'Double Kick': {'name': 'Double Kick', 'power': 30, 'type': 'Fighting', 'super effective against': ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'], 'not very effective against': ['Poison', 'Flying', 'Psychic', 'Bug', 'Fairy']}, 
    'Earthquake': {'name': 'Earthquake', 'power': 100, 'type': 'Ground', 'super effective against': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'], 'not very effective against': ['Grass', 'Bug']}, 
    'Wing Attack': {'name': 'Wing Attack', 'power': 60, 'type': 'Flying', 'super effective against': ['Grass', 'Fighting', 'Bug'], 'not very effective against': ['Electric', 'Rock', 'Steel']}, 
    'Peck': {'name': 'Peck', 'power': 35, 'type': 'Flying', 'super effective against': ['Grass', 'Fighting', 'Bug'], 'not very effective against': ['Electric', 'Rock', 'Steel']}, 
    'Confusion': {'name': 'Confusion', 'power': 50, 'type': 'Psychic', 'super effective against': ['Fighting', 'Poison'], 'not very effective against': ['Psychic', 'Steel']}, 
    'Twineedle': {'name': 'Twineedle', 'power': 25, 'type': 'Bug', 'super effective against': ['Grass', 'Psychic', 'Dark'], 'not very effective against': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']}, 
    'Rock Throw': {'name': 'Rock Throw', 'power': 50, 'type': 'Rock', 'super effective against': ['Fire', 'Ice', 'Flying', 'Bug'], 'not very effective against': ['Fighting', 'Ground', 'Steel']}, 
    'Rock Slide': {'name': 'Rock Slide', 'power': 75, 'type': 'Rock', 'super effective against': ['Fire', 'Ice', 'Flying', 'Bug'], 'not very effective against': ['Fighting', 'Ground', 'Steel']}, 
    'Lick': {'name': 'Lick', 'power': 30, 'type': 'Ghost', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Dark']}, 
    'Outrage': {'name': 'Outrage', 'power': 120, 'type': 'Dragon', 'super effective against': ['Dragon'], 'not very effective against': ['Steel']}, 
    'Crunch': {'name': 'Crunch', 'power': 80, 'type': 'Dark', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Fighting', 'Dark', 'Fairy']}, 
    'Bite': {'name': 'Bite', 'power': 60, 'type': 'Dark', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Fighting', 'Dark', 'Fairy']}, 
    'Flash Cannon': {'name': 'Flash Cannon', 'power': 80, 'type': 'Steel', 'super effective against': ['Ice', 'Rock', 'Fairy'], 'not very effective against': ['Fire', 'Water', 'Electric', 'Steel']}, 
    'Smog': {'name': 'Smog', 'power': 30, 'type': 'Poison', 'super effective against': ['Grass', 'Fairy'], 'not very effective against': ['Poison', 'Ground', 'Rock', 'Ghost']}, 
    'Dream Eater': {'name': 'Dream Eater', 'power': 100, 'type': 'Psychic', 'super effective against': ['Fighting', 'Poison'], 'not very effective against': ['Psychic', 'Steel']}, 
    'Body Slam': {'name': 'Body Slam', 'power': 85, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Double Slap': {'name': 'Double Slap', 'power': 15, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Razor Leaf': {'name': 'Razor Leaf', 'power': 55, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Headbutt': {'name': 'Headbutt', 'power': 70, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Absorb': {'name': 'Absorb', 'power': 20, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Fairy Wind': {'name': 'Fairy Wind', 'power': 40, 'type': 'Fairy', 'super effective against': ['Fighting', 'Dragon', 'Dark'], 'not very effective against': ['Fire', 'Poison', 'Steel']}, 
    'Struggle Bug': {'name': 'Struggle Bug', 'power': 50, 'type': 'Bug', 'super effective against': ['Grass', 'Psychic', 'Dark'], 'not very effective against': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']}, 
    'Draining Kiss': {'name': 'Draining Kiss', 'power': 50, 'type': 'Fairy', 'super effective against': ['Fighting', 'Dragon', 'Dark'], 'not very effective against': ['Fire', 'Poison', 'Steel']}, 
    'Shadow Ball': {'name': 'Shadow Ball', 'power': 80, 'type': 'Ghost', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Dark']}
}


CHARACTERS = {
    'Pikachu': {'Type': ['Electric'], 'HP': 35, 'Moves': ['Thunder Shock',  'Double Kick', 'Thunderbolt'], 'Attack': 55, 'Defense': 40, 'Speed': 90, 'Experience': 112},
    'Charizard': {'Type': ['Fire', 'Flying'], 'HP': 78, 'Moves': [ 'Crunch', 'Ember', 'Scratch', 'Wing Attack'], 'Attack': 84, 'Defense': 78, 'Speed': 100, 'Experience': 240},
    'Squirtle': {'Type': ['Water'], 'HP': 44, 'Moves': ['Tackle',  'Bubble', 'Bite'], 'Attack': 48, 'Defense': 65, 'Speed': 43, 'Experience': 63},
    'Jigglypuff': {'Type': ['Normal', 'Fairy'], 'HP': 115, 'Moves': ['Pound', 'Body Slam', 'Double Slap'], 'Attack': 45, 'Defense': 20, 'Speed': 20, 'Experience': 95},
    'Gengar': {'Type': ['Ghost', 'Poison'], 'HP': 60, 'Moves': ['Lick', 'Smog', 'Dream Eater', 'Shadow Ball'], 'Attack': 65, 'Defense': 60, 'Speed': 110, 'Experience':225},
    'Magnemite': {'Type': ['Electric', 'Steel'], 'HP': 25, 'Moves': [ 'Tackle', 'Flash Cannon', 'Thunder Shock', 'Thunderbolt'],  'Attack': 35, 'Defense': 70, 'Speed': 45, 'Experience': 65},
    'Bulbasaur': {'Type': ['Grass', 'Poison'], 'HP': 45, 'Moves': ['Tackle', 'Vine Whip', 'Razor Leaf'], 'Attack': 49, 'Defense': 49, 'Speed': 45, 'Experience': 64},
    'Charmander': {'Type': ['Fire'], 'HP': 39, 'Moves': ['Scratch', 'Ember', 'Fire Spin'], 'Attack': 52, 'Defense': 43, 'Speed': 65, 'Experience': 62},
    'Beedrill': {'Type': ['Bug', 'Poison'], 'HP': 65, 'Moves': ['Peck', 'Twineedle', 'Rage', 'Fury Attack', 'Outrage'], 'Attack': 90, 'Defense': 40, 'Speed': 75, 'Experience': 178},
    'Golem': {'Type': ['Rock', 'Ground'], 'HP': 80, 'Moves': [ 'Tackle', 'Rock Throw', 'Rock Slide', 'Earthquake'], 'Attack': 120, 'Defense': 130, 'Speed': 45, 'Experience': 223},
    'Dewgong': {'Type': ['Water', 'Ice'], 'HP': 90, 'Moves': ['Aqua Jet',  'Ice Shard', 'Headbutt'], 'Attack': 70, 'Defense': 80, 'Speed': 70, 'Experience': 166},
    'Hypno': {'Type': ['Psychic'],'HP': 85, 'Moves': ['Pound', 'Confusion', 'Dream Eater'], 'Attack': 73, 'Defense': 70, 'Speed': 67, 'Experience': 169},
    'Cleffa': {'Type': ['Fairy'], 'HP': 50, 'Moves': [ 'Pound', 'Magical Leaf'], 'Attack': 25, 'Defense': 28, 'Speed': 15, 'Experience': 44},
    'Cutiefly': {'Type': ['Fairy', 'Bug'], 'HP': 40, 'Moves': ['Absorb', 'Fairy Wind', 'Struggle Bug', 'Draining Kiss'], 'Attack': 45, 'Defense': 40, 'Speed': 84, 'Experience': 61}
}

POKEMON_NAMES = list(CHARACTERS.keys())
