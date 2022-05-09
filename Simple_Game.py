import random

player_name = ""
player_attack = 0
player_health = 0

enemy_name = ""
enemy_attack = 0
enemy_health = 0

def stat_gen():
    global player_attack
    global player_health
    global enemy_attack
    global enemy_health
    player_attack = random.randrange(1,10)
    player_health = random.randrange(1,100)
    enemy_attack = random.randrange(1,10)
    enemy_health = random.randrange(1,100)

def press_to_continue():
    input("...")

def title_screen():
    print("What is your name?")
    global player_name
    player_name = input()
    print(f"Look over yonder, {player_name}.")
    press_to_continue()
    print("An enemy approaches, what do you see?")
    press_to_continue()
    print("Is it a rat? A skeleton?")
    global enemy_name
    enemy_name = input()
    print(f"{enemy_name}, you say?")
    press_to_continue()
    print("To battle!")
    press_to_continue()

def combat_screen():
    print(f"{player_name} vs {enemy_name}")
    press_to_continue()
    global player_attack
    global player_health
    global enemy_attack
    global enemy_health
    while player_health and enemy_health >= 0:
        print("Attack?")
        if "y" in str.lower(input()):
            enemy_health = enemy_health-player_attack
            print(f"{player_name} hit {enemy_name}!")
            print(f"{enemy_name} has {enemy_health} health left.")
            victory()
            press_to_continue()
            player_health = player_health-enemy_attack
            print(f"{enemy_name} hit {player_name}!")
            print(f"{player_name} has {player_health} health left.")
            defeat()

def victory():
    if enemy_health <= 0:
        print(f"{enemy_name} died!")
        press_to_continue()
        print("You Won!")
        press_to_continue()
        ending()

def defeat():
    if player_health <= 0:
        print(f"{player_name} died!")
        press_to_continue()
        print("You Lost.")
        press_to_continue()
        ending()

def ending():
    print("The End")
    quit()

stat_gen()
title_screen()
combat_screen()