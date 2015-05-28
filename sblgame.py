#!/usr/bin/env python
"""
game.py - This is where objects are created and the game is played.

Author: mpmsimo
Created: 2/21/2015

To-do:
 * Fix error handling for menus (they current accept strings where they shouldnt)
"""

import weapon
import player
import soulgem
import game_information as gi

souls = gi.souls
weapons = gi.weapons
enemies = gi.enemies
affinity = None

def character_creation():
    """Choose a character name"""
    player_name = name_character()
    affinity = choose_affinity()
    soulgem = choose_soulgem(affinity)
    weapon = choose_weapon()
    player = generate_player(player_name, soulgem, weapon)
    player = generate_player("Reulan", soulgem, weapon)
    return player

def name_character():
    """Renames the player"""
    player_name = raw_input("Please choose a name for your character: ")
    return player_name

def choose_affinity():
    """Option to see str/dex/int heroes."""
    affinities = ["Strength", "Dexterity", "Intelligence"]
    for i in range(len(affinities)):
        print("{0}. {1}".format(i+1, affinities[i]))
    print("")
    choice = int(raw_input("Show aligned souls for affinity (0 to start over): "))
    if choice in range(1, len(affinities)+1):
        print("\nYou chose {0}.\n".format(affinities[choice-1]))
    elif choice == 0:
        character_creation()
    else:
        print(range(1, len(affinities)+1))
        print("You have entered an incorrect choice, please try again.\n")
        choose_affinity()
    return affinities[choice-1]

def choose_soulgem(affinity):
    """Soulgem choice"""
    count = 1
    soul_list = []
    for hero in souls:
        sg = soulgem.Soulgem(souls[hero][0], souls[hero][1], souls[hero][2], souls[hero][3], souls[hero][4], souls[hero][5], souls[hero][6], souls[hero][7], souls[hero][8])
        if affinity == sg.affinity:
            soul_list.append(hero)
            print("{0}\n{1}. {2}".format(80 * "=", count, sg.name))
            sg.print_soulgem()
            count+=1
        elif affinity == None:
            soul_list.append(hero)
            print("{0}\n{1}. {2}".format(80 * "=", count, sg.name))
            sg.print_soulgem()
            count+=1
    print(80 * "=")
    choice = int(raw_input("\nChoose the soul you would like to control (0 to start over): "))
    if choice in range(1, len(soul_list)+1):
        print("\nYou chose {0}.\n".format(soul_list[choice-1]))
    elif choice == 0:
        character_creation()
    else:
        print("You have entered an incorrect choice, please try again.\n")
        choose_soulgem(affinity)
    return soul_list[choice-1]

def choose_weapon():
    """Weapon choice"""
    count = 1
    weapon_list = []
    for wep in weapons:
        item = weapon.Weapon(weapons[wep][0], weapons[wep][1], weapons[wep][2], weapons[wep][3], weapons[wep][4], weapons[wep][5])
        weapon_list.append(wep)
        print("{0}\n{1}. {2}".format(80 * "=", count, item.name))
        item.print_weapon()
        count+=1
    print(80 * "=")
    choice = int(raw_input("\nChoose the weapon you would like to use (0 to start over): "))
    if choice in range(1, len(weapon_list)+1):
        print("\nYou chose {0}.\n".format(weapon_list[choice-1]))
    elif choice == 0:
        character_creation()
    else:
        print("You have entered an incorrect choice, please try again.\n")
        choose_weapon()
    return weapon_list[choice-1]

def generate_player(name, selected_soulgem, selected_weapon):
    for hero in souls:
        if hero == selected_soulgem:
            sg = soulgem.Soulgem(souls[hero][0], souls[hero][1], souls[hero][2], souls[hero][3], souls[hero][4], souls[hero][5], souls[hero][6], souls[hero][7], souls[hero][8])
            sblplayer = player.Player(name, 1, 0, 50, 1, 0, 0, 0)
            sblplayer.equip_soulgem(sg)
    for wep in weapons:
        if wep == selected_weapon:
            item = weapon.Weapon(weapons[wep][0], weapons[wep][1], weapons[wep][2], weapons[wep][3], weapons[wep][4], weapons[wep][5])
            sblplayer.equip_weapon(item)
            break
    return sblplayer

def generate_enemy():
    for enemy in enemies:
        print(enemies[enemy])
        e = player.Enemy(enemies[enemy][0], enemies[enemy][1], enemies[enemy][2], enemies[enemy][3], enemies[enemy][4], enemies[enemy][5])
        e.print_basic()

def main():
    print("Welcome to the Spellblade: Legacy!")
    sblplayer = character_creation()
    sblplayer.print_basic()
    sblplayer.print_advanced()
    sblplayer.show_abilities()
    #sblplayer.attack_menu()
    #sblplayer.parse_sg_ability()

if __name__ == "__main__":
    #main()
    generate_enemy()