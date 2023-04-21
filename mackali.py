#!/usr/bin/env python3

import os
import sys
from categories import categories
from gear import gear

def clear_screen():
    """Clears the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

def display_banner():
    """Displays the banner for MacKali."""
    print(gear)
    print(""" 
___  ___           _   __      _ _ 
|  \/  |          | | / /     | (_)
| .  . | __ _  ___| |/ /  __ _| |_ 
| |\/| |/ _` |/ __|    \ / _` | | |
| |  | | (_| | (__| |\  \ (_| | | |
\_|  |_/\__,_|\___\_| \_/\__,_|_|_|                                                                                                                                  
    """)
    print("Welcome to MacKali!\n")
    print("Categories:")
    print("1. Information Gathering")
    print("2. Vulnerability Analysis")
    print("3. Wireless Attacks")
    print("4. Web Application Analysis")
    print("5. Exploitation Tools")
    print("6. Password Attacks")
    print("7. Sniffing & Spoofing")
    print("8. Maintaining Access")
    print("9. Reverse Engineering")
    print("10. Forensics Tools")
    print("0. Exit")

def display_tools(category):
    """Displays the tools for the selected category."""
    print(f"\nTools for {category}:\n")
    tools = categories[category]
    for i, tool in enumerate(tools):
        print(f"{i+1}. {tool} - {tools[tool]}")
    print("0. Back")

def install_tool(tool):
    """Installs the selected tool using Homebrew."""
    os.system(f"brew install {tool}")

def main():
    clear_screen()
    display_banner()
    while True:
        choice = input("\nEnter your choice: ")
        if choice == '0':
            sys.exit()
        elif choice.isdigit() and 1 <= int(choice) <= 10:
            clear_screen()
            display_banner()
            category = {
                '1': 'Information Gathering',
                '2': 'Vulnerability Analysis',
                '3': 'Wireless Attacks',
                '4': 'Web Application Analysis',
                '5': 'Exploitation Tools',
                '6': 'Password Attacks',
                '7': 'Sniffing & Spoofing',
                '8': 'Maintaining Access',
                '9': 'Reverse Engineering',
                '10': 'Forensics Tools'
            }[choice]
            display_tools(category)
            while True:
                choice = input("\nEnter your choice: ")
                if choice == '0':
                    clear_screen()
                    display_banner()
                    break
                elif choice.isdigit() and 1 <= int(choice) <= len(categories[category]):
                    tool = list(categories[category].keys())[int(choice)-1]
                    install_tool(tool)
                    input(f"\n{tool} has been installed. Press Enter to continue...")
                    clear_screen()
                    display_banner()
                else:
                    print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
