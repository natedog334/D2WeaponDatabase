import os
import random
import re
from MenuModule import Menu, Option
from DatabaseService import DatabaseService

menu_stack = []
dbs = DatabaseService()
weapon_types = {
    "rocket_launcher" : "Rocket Launcher",
    "grenade_launcher" : "Grenade Launcher",
    "hand_cannon" : "Hand Cannon",
    "sniper" : "Sniper",
    "shotgun" : "Shotgun",
    "smg" : "SMG",
    "scout_rifle" : "Scout Rifle",
    "sidearm" : "Sidearm",
    "auto_rifle" : "Auto Rifle",
    "bow" : "Bow",
    "pulse_rifle" : "Pulse Rifle",
    "lfr" : "Linear Fusion Rifle",
    "fusion_rifle" : "Fusion Rifle",
    "trace_rifle" : "Trace Rifle",
    "machine_gun" : "Machine Gun",
    "sword" : "Sword"
}

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
        "Loadout Generator",
        [
            Option("Generate a random loadout", make_random_loadout),
            Option("Generate a custom loadout", make_random_loadout),
            Option("Go back", lambda: pop_and_clear())
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
            print_weapon(weapon_info)
    else:
        clear()
        print("An error occurred/no weapons found.")

def search_weapon_by_type(type):
    return_value = dbs.get_weapon_by_type(type)
    if return_value:
        clear()
        for weapon_info in return_value:
            print_weapon(weapon_info)
    else:
        clear()
        print("An error occurred/no weapons found.")

def search_weapon_by_element(element):
    return_value = dbs.get_weapon_by_element(element)
    if return_value:
        clear()
        for weapon_info in return_value:
            print_weapon(weapon_info)
    else:
        clear()
        print("An error occurred/no weapons found.")

def make_random_loadout():
    primaries = dbs.get_all_primaries()
    maxIdx = len(primaries)
    idx = random.randint(0, maxIdx)
    primary = primaries[idx]
    exotic_flag = check_exotic_status(primary)

    secondaries = dbs.get_all_secondaries()
    maxIdx = len(secondaries)
    idx = random.randint(0, maxIdx)
    secondary = secondaries[idx]
    if exotic_flag:
        while check_exotic_status(secondary):
            idx = random.randint(0, maxIdx)
            secondary = secondaries[idx]
    else:
        exotic_flag = check_exotic_status(secondary)

    heavies = dbs.get_all_heavies()
    maxIdx = len(heavies)
    idx = random.randint(0, maxIdx)
    heavy = heavies[idx]
    if exotic_flag:
        while check_exotic_status(heavy):
            idx = random.randint(0, maxIdx)
            heavy = heavies[idx]

    clear()
    print_loadout(primary, secondary, heavy)

def check_exotic_status(weapon_info):
    if weapon_info[5] is "Exotic":
        return True
    else:
        return False

def print_loadout(p, s, h):
    print("Primary:")
    print_weapon(p)
    print("Secondary:")
    print_weapon(s)
    print("Heavy:")
    print_weapon(h)

def print_weapon(weapon_info):
    print(f"Weapon: {weapon_info[0]} | Type: {weapon_types.get(weapon_info[1])} | Archetype: {weapon_info[2]} "
          f"| RoF: {weapon_info[3]} | Element: {weapon_info[4]} | Rarity: {weapon_info[5]} "
          f"| Source: {weapon_info[6]}")

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