from data_collection import DataCollection
import random

client = DataCollection()

def __b():
    players = client.get_player_array(2)
    phase = client.get_instant_phase()
    sorcery = client.get_top_sorcery()

    return f"During {players[0]}'s {phase}, {players[1]} attempts an instant speed {sorcery}."

def __c():
    player = client.get_player()
    saltyCard = client.get_salty_card()

    return f"Moving to his second main phase, {player} tanks and jams {saltyCard}."

def __d():
    player = client.get_player()
    instant = client.get_top_instant()
    creature = client.get_top_creature()
    enchantment = client.get_top_enchantment()

    return f"Moving to combat with {creature}, {player} made sure to leave {instant} up to protect his {enchantment}."

def __e():
    player = client.get_player()

    return f"I'm sorry {player}, did you read the card?"

def __g():
    players = client.get_player_array(2)
    saltyCard = client.get_salty_card()
    instant = client.get_top_instant()

    return f"At a critical juncture, {players[0]} attempts to resolve {saltyCard}. {players[1]} snap responds with {instant}."

def __h():
    players = client.get_player_array(2)
    saltyCard = client.get_salty_card()
    creature = client.get_top_creature()
    reaction = client.get_reaction()

    return f"Victory is close. With {saltyCard} in hand, {players[0]} slams {creature}. {players[1]} {reaction}."

def __i():
    player = client.get_player()
    enchantment = client.get_top_enchantment()
    instant = client.get_top_instant()

    return f"An overwhelmed {player} decides {enchantment} is a threat on the board. He considers burning a {instant}."

def __j():
    player = client.get_player()
    decision = [
        "decides",
        "declines",
        "forgets",
        "wants",
        "encourages others"
    ]
    random.shuffle(decision)

    return f"{player} {decision[0]} to pay for Smothering Tithe."

def __k():
    player = client.get_player()
    card = client.get_top_card()

    return f"During a cut, {player} sighs while noticing his {card} at the bottom of his deck."

def __l():
    player = client.get_player()
    lands = client.get_top_lands_array(2)

    return f"{player} is trying to pretend they had {lands[0]} and {lands[1]} untapped the whole time."

def __n():
    players = client.get_player_array(2)
    saltyCard = client.get_salty_card()

    return f"{players[0]}'s crucial, game winning {saltyCard} is put on the stack. {players[1]} is already shuffling for the next game"

def __o():
    player = client.get_player()
    saltyCard = client.get_salty_card()

    return f"It's clear to everyone at the table that {player} has the {saltyCard}."

def __p():
    player = client.get_player()

    return f"\"No, {player} -- ETB and Cast are two different triggers.\""

def __q():
    player = client.get_player()
    saltyCard = client.get_salty_card()
    instant = client.get_top_instant()

    return f"Careful not to tap out, {player} casts {saltyCard} with {instant} backup."

def __r():
    players = client.get_player_array(2)
    instant = client.get_top_instant()

    return f"After looking at the top card of {players[0]}'s library, {players[1]} decided to leave {instant} right where it was"

def __s():
    players = client.get_player_array(4)
    instants = client.get_top_instant_array(3)
    sorcery = client.get_top_sorcery()

    return f"The stack is {players[0]}'s {instants[0]} and {players[1]}'s {instants[1]} responding to {players[2]}'s {sorcery}. {players[3]} clutches his {instants[2]}, wondering if now is the time."

def __t():
    players = client.get_player_array(2)
    creature = client.get_top_creature()
    card = client.get_top_card()

    return f"{players[0]} nearly punted the game for failing to read the text on {players[1]}'s {creature}. {card} should help him stabilize."

def __u():
    players = client.get_player_array(2)
    saltyCard = client.get_salty_card()

    return f"{players[0]} is miles away from his {saltyCard} while {players[1]} has him in the strip mine lock."

def __v():
    players = client.get_player_array(2)
    enchantment = client.get_top_enchantment()
    instant = client.get_top_instant()

    return f"{players[0]} notices {players[1]} forgot about the text on his {enchantment}. A copy of {instant} will be huge later."

def __w():
    players = client.get_player_array(2)

    return f"\"See for yourself, I'm done answering questions\" exclaims {players[0]} when {players[1]} asks if he's got any flying blockers."

def __y():
    player = client.get_player()
    enchantment = client.get_top_enchantment()
    creature = client.get_top_creature()

    return f"The playgroup pitched in and got {player} a copy of {enchantment} - which should pair well with his {creature}."

def __z():
    players = client.get_player_array(3)
    sorcery = client.get_top_sorcery()
    complaint = [
        "casual gameplay",
        "the board state",
        "Niv-Mizzet",
        "missed land drops",
        "Winter Orb",
        "Elspeth"
    ]
    random.shuffle(complaint)

    return f"{players[0]} and {players[1]} complain about {complaint[0]} as {players[2]} untaps and jams {sorcery}."

def __aa():
	players = client.get_player_array(2)

	return f"{players[0]} scrys a handful of cards during {players[1]}'s turn and decides to scoop it up"

def __a1():
    players = client.get_player_array(2)
    saltyCard = client.get_salty_card()
    card = client.get_top_card()

    return f"{players[0]} thinks it's pretty unfair {players[1]} runs a {card}. Ironic coming from a guy playing {saltyCard}."

def __b1():
    player = client.get_player()
    saltyCard = client.get_salty_card()

    return f"{player}'s ordered his phases draw, untap, declare attackers, undeclare, redeclare, cast {saltyCard}, missed upkeep trigger, discard, land for turn."

def __c1():
    players = client.get_player_array(1)
    artifact = client.get_top_artifact()

    return f"No, {players[0]} - we can't rewind because you forgot to activate your {artifact}."

def __d1():
    players = client.get_player_array(1)

    return f"{players[0]} plays with his lands at the top of his playmat."

def __e1():
    players = client.get_player_array(2)
    creature = client.get_top_creature()
    instant = client.get_top_instant()

    return f"{players[0]} should have waited on his {creature}. {players[1]} was practically telegraphing the {instant}."

def __f1():
    players = client.get_player_array(1)
    sorcery = client.get_top_sorcery()

    return f"Sorry {players[0]}, {sorcery} won't save you this time."

def __g1():
    players = client.get_player_array(2)
    creatures = client.get_top_creature_array(2)

    return f"In careless combat, {players[0]} swings {creatures[0]} into {players[1]}'s {creatures[1]}."

def __h1():
    players = client.get_player_array(2)
    creature = client.get_top_creature()

    return f"No spells will resolve if {players[0]} has anything to say about it. Looks like {players[1]} is on the {creature} beat down plan."

def __i1():
    players = client.get_player_array(2)
    enchantment = client.get_top_enchantment()
    card = client.get_salty_card()

    return f"Still unsure what {players[0]}'s {enchantment} does, {players[1]} assumes his {card} will handle it."

def __j1():
    land = client.get_top_lands()
    player = client.get_player()

    return f"\"{land}, tapped. Pass.\", exclaims {player}."

def __k1():
    players = client.get_player_array(1)
    creature = client.get_top_creature()
    enchantment = client.get_top_enchantment()

    return f"Fully tilted, {players[0]} puts {creature} and {enchantment} on the board at the same time - paying for each after he cast them."

def __l1():
    players = client.get_player_array(1)

    return f"{players[0]} is absolutely in the tank."

def __m1():
    players = client.get_player_array(1)
    salt = client.get_salty_card()

    return f"It was a long road, but {salt} finally brought {players[0]} kicking and screaming across the finish line."

def __n1():
    card = [
        'Pyroblast',
        'Hydroblast',
        'Veil',
        'a Lily plus',
        'the Dack minus'
    ]

    reaction = [
        'a real beating',
        'a bit overkill',
        'a little late',
        'pretty irrelevant'
    ]
    random.shuffle(card)
    random.shuffle(reaction)

    return f"Actually {card[0]} is {reaction[0]} here."

def __o1():
    player = client.get_player()
    saltyCard = client.get_salty_card()

    return f"The threat has been identified - it's {player}'s {saltyCard}."

def __p1():
    player = client.get_player()
    topCreature = client.get_top_creature()
    topSorcery = client.get_top_sorcery()
    saltyCard = client.get_salty_card()

    return f"For {player}, 8 life is chump change when Sylvan offers {topCreature}, {topSorcery}, and {saltyCard}."

def __q1():
    player = client.get_player()
    topInstant = client.get_top_instant()

    return f"Tanking on a pre-combat {topInstant}, {player} is finally starting to get on everyone's nerves."

def __r1():
    player = client.get_player()
    topCard = client.get_top_card()

    return f"The Ashiok downtick is particularly brutal for {player} as the only copy of {topCard} gets sent to the the shadow realm."

def __s1():
    player = client.get_player()

    return f"\"Well, I'm out of win cons\" - {player}."

def __t1():
    player = client.get_player()
    phase = client.get_instant_phase()
    sorcery = client.get_top_sorcery()

    return f"Little tef finally {player} achieve the dream of a {phase} {sorcery}. Absolutley no one is impressed."

def __u1():
    player = client.get_player()
    topCard = client.get_top_card()

    return f"{player} was always dead to a top deck {topCard}."

def __v1():
    player = client.get_player()
    topSaltyCard = client.get_salty_card()

    return f"{player} is turbo-mulling to a {topSaltyCard}."

def __w1():
    player = client.get_player()
    topCreature = client.get_top_creature()

    return f"\"Hey you bet. {topCreature}. You absolutely bet, pal\" - {player}."

def __x1():
    player = client.get_player()
    topSaltyCard = client.get_salty_card()

    return f"After the game, {player} entertained the playgroup with stories of past tourneys and showed off a binder page full of mint {topSaltyCard} proxies."

def get_sentence():
    funct_array = [
        __c, __d, __e, __g, __i, __j, __l,
        __n, __p, __q, __s, __u, __v, __w, __z,
        __aa, __a1, __b1, __c1, __e1, __f1, __h1,
        __i1, __l1, __m1, __n1, __o1, __p1, __q1,
        __r1, __s1, __t1, __u1, __v1, __x1
    ]
    my_length = len(funct_array)
    my_index = random.randrange(0, my_length)

    random.shuffle(funct_array)

    return funct_array[my_index]()

