import os
import re
from MenuModule import Menu, Option
from DatabaseService import DatabaseService

menu_stack = []
dbs = DatabaseService()

def search_weapon_menu():
    return Menu(
        "Search weapons by:",
        [
            Option("Name", search_weapon_by_name),
            Option("Weapon Type", lambda: push(search_weapon_type_menu(), True)),
            Option("Element", lambda: push(search_weapon_element_menu(), True)),
            Option("Go back", lambda: pop_and_clear())
        ]
    )

def search_weapon_type_menu():
    return Menu(
        "Weapon Type:",
        [
            Option("Auto Rifle", search_weapon_by_type, "auto_rifle"),
            Option("Pulse Rifle", search_weapon_by_type, "pulse_rifle"),
            Option("Scout Rifle", search_weapon_by_type, "scout_rifle"),
            Option("SMG", search_weapon_by_type, "smg"),
            Option("Hand Cannon", search_weapon_by_type, "hand_cannon"),
            Option("Sidearm", search_weapon_by_type, "sidearm"),
            Option("Bow", search_weapon_by_type, "bow"),
            Option("Sniper", search_weapon_by_type, "sniper"),
            Option("Shotgun", search_weapon_by_type, "shotgun"),
            Option("Fusion Rifle", search_weapon_by_type, "fusion_rifle"),
            Option("Trace Rifle", search_weapon_by_type, "trace_rifle"),
            Option("Rocket Launcher", search_weapon_by_type, "rocket_launcher"),
            Option("Grenade Launcher", search_weapon_by_type, "grenade_launcher"),
            Option("Machine Gun", search_weapon_by_type, "machine_gun"),
            Option("Linear Fusion Rifle", search_weapon_by_type, "lfr"),
            Option("Sword", search_weapon_by_type, "sword"),
            Option("Go back", lambda: pop_and_clear())
        ]
    )

def search_weapon_element_menu():
    return Menu(
        "Element:",
        [
            Option("Kinetic", search_weapon_by_element, "Kinetic"),
            Option("Solar", search_weapon_by_element, "Solar"),
            Option("Arc", search_weapon_by_element, "Arc"),
            Option("Void", search_weapon_by_element, "Void"),
            Option("Stasis", search_weapon_by_element, "Stasis"),
            Option("Go back", lambda: pop_and_clear())
        ]
    )

def generate_loadout_menu():
    return Menu(
        [
            Option("Generate a random loadout", lambda: push(search_weapon_menu(), True)),
            Option("Generate a custom loadout", lambda: push(search_weapon_menu(), True)),
            Option("Go back", lambda: pop_and_clear()),
        ]
    )

def main_menu():
    return Menu(
        "Welcome to the Destiny 2 Weapon Database!",
        [
            Option("Search for a weapon", lambda: push(search_weapon_menu(), True)),
            Option("Generate a loadout", lambda: push(generate_loadout_menu(), True)),
        ]
    )

def search_weapon_by_name():
    name = input("Enter a weapon name\n> ")
    return_value = dbs.get_weapon_by_name(name)
    if return_value:
        clear()
        for weapon_info in return_value:
            print(f"Weapon: {weapon_info[0]} | Type: {weapon_info[1]} | Archetype: {weapon_info[2]} "
                  f"| RoF: {weapon_info[3]} | Element: {weapon_info[4]} | Rarity: {weapon_info[5]} "
                  f"| Source: {weapon_info[6]}")
    else:
        clear()
        print("An error occurred/no weapons found.")

def search_weapon_by_type(type):
    return_value = dbs.get_weapon_by_type(type)
    if return_value:
        clear()
        for weapon_info in return_value:
            print(f"Weapon: {weapon_info[0]} | Type: {weapon_info[1]} | Archetype: {weapon_info[2]} "
                  f"| RoF: {weapon_info[3]} | Element: {weapon_info[4]} | Rarity: {weapon_info[5]} "
                  f"| Source: {weapon_info[6]}")
    else:
        clear()
        print("An error occurred/no weapons found.")

def search_weapon_by_element(element):
    return_value = dbs.get_weapon_by_element(element)
    if return_value:
        clear()
        for weapon_info in return_value:
            print(f"Weapon: {weapon_info[0]} | Type: {weapon_info[1]} | Archetype: {weapon_info[2]} "
                  f"| RoF: {weapon_info[3]} | Element: {weapon_info[4]} | Rarity: {weapon_info[5]} "
                  f"| Source: {weapon_info[6]}")
    else:
        clear()
        print("An error occurred/no weapons found.")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def push(menu, clear_history):
    if clear_history:
        clear()
    menu_stack.append(menu)

def pop_and_clear():
    menu_stack.pop()
    clear()

def main():
    menu_stack.append(main_menu())
    while True:
        menu_stack[-1].show()


if __name__ == "__main__":
    main()