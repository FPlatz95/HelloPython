#!/usr/bin/env python3

#Importing packages
from random import choice

#Defining functions
## Convenience functions
def create_tunnel(cave_from, cave_to):
    """ Create a tunnel between cave_from and cave_to """
    caves[cave_from].append(cave_to)
    caves[cave_to].append(cave_from)

def visit_cave(cave_number):
    """ mark a cave as visited """
    visited_caves.append(cave_number)
    unvisited_caves.remove(cave_number)

def choose_cave(cave_list):
    """ Pick a cave from a list,
    provided that the cave has less the three tunnels """
    cave_number = choice(cave_list)
    while len(caves[cave_number]) >= 3:
        cave_number = choice(cave_list)
    return cave_number

def print_caves():
    """ Print out the current cave structure """
    for number in cave_numbers:
        print(number, ":", caves[number])
    print("----------")

## Cave creating functions
def setup_caves(cave_numbers):
    """ Create the starting list of caves """
    caves = []
    for cave in cave_numbers:
        caves.append([])
    return caves

def link_caves():
    """ Connecting all caves with two way tunnels """
    while unvisited_caves != []:
        this_cave = choose_cave(visited_caves)
        next_cave = choose_cave(unvisited_caves)
        create_tunnel(this_cave, next_cave)
        visit_cave(next_cave)

def finish_caves():
    """ Link the rest of the caves with one way tunnels """
    for cave in cave_numbers:
        while len(caves[cave]) < 3:
            passage_to = choose_cave(cave_numbers)
            caves[cave].append(passage_to)

## Player interaction functions
def print_location(player_location):
    """ Tell the player where they are """
    print("You are in cave ", player_location)
    print("From here you can see caves:")
    print(caves[player_location])
    if wumpus_location in caves[player_location]:
        print("I smell a wumpus")

"""
This function is replaced with the ask_for_cave function
def get_next_location():
    ### Get the players next location ###
    player_input = input(">")
    if not player_input.isdigit() or int(player_input) not in caves[player_location]:
        print(player_input, " ?")
        print("That is not a direction i can see")
        return None
    else:
        return int(player_input)
"""

def ask_for_cave():
    """ Ask the player to choose a cave from their current location """
    player_input = input("Which cave?")
    if not player_input.isdigit() or int(player_input) not in caves[player_location]:
        print(player_input, " ?")
        print("That is not a direction i can see")
        return None
    else:
        return int(player_input)

def get_action():
    """ Find out what the player would like to do next """
    print("What do you do next")
    print("m) move")
    print("a) Fire an arrow")
    action = input(">")
    if action == "m" or action == "a":
        return(action)
    else:
        print(action,"?"," That is not an action you dumb fool")
        return None

def do_movement():
    """ Doing a movement """
    print("Moving...")
    new_location = ask_for_cave()
    if new_location is None:
        return player_location
    else:
        return new_location

def do_shooting():
    print("Firing...")
    shoot_at = ask_for_cave()
    if shoot_at is None:
        return False

    if shoot_at == wumpus_location:
        print("Twang ... You shot the Wumpus!")
        print("Congratulations dick head <3")
    else:
        print("Twang .. clatter, clatter!")
        print("You wasted your arrow")
    return True

# Main game

cave_numbers = range(0,20)
unvisited_caves = list(range(0,20))
visited_caves = []
caves = setup_caves(cave_numbers)

visit_cave(0)
link_caves()
finish_caves()
print_caves()

wumpus_location = choice(cave_numbers)
print(wumpus_location)
player_location = choice(cave_numbers)
while player_location == wumpus_location:
    player_location = choice(cave_numbers)

while 1:
    print_location(player_location)

    action = get_action()

    if action == "m":
        player_location = do_movement()
        if player_location == wumpus_location:
            print("Aargh! You got eaten by a wumpus!")
            break

    if action == "a":
        game_over = do_shooting()
        if game_over:
            break

"""
while True:
    print_location(player_location)
    new_location = get_next_location()
    if new_location != wumpus_location:
        player_location = new_location
    if new_location == wumpus_location:
        print("Arghh you got eaten by a wumpus!")
        break
"""
