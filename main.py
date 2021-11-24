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
            Option("Generate a loadout", lambda: push(generate_loadout_menu(), True)),
        ]
    )

def generate_loadout_menu():
    return Menu(
        [
            Option("Generate a random loadout", lambda: push(search_weapon_menu(), True)),
            Option("Generate a custom loadout", lambda: push(search_weapon_menu(), True)),
        ]
    )

def main_menu():
    return Menu(
        "Welcome to the Destiny 2 Weapon Database!",
        [
            Option("Search for a weapon", lambda: push(search_weapon_menu(), True)),
            Option("Generate a loadout", lambda: push(search_weapon_menu(), True)),
        ]
    )

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