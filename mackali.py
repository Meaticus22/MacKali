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
    print("Welcome to MacKali!\n")

def display_categories():
    """Displays the available categories and tools."""
    print("Select a category to install tools from:\n")
    for i, category in enumerate(categories):
        print(f"{i+1}. {category}")
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
        display_categories()
        choice = input("\nEnter your choice: ")
        if choice == '0':
            sys.exit()
        elif choice.isdigit() and 1 <= int(choice) <= len(categories):
            clear_screen()
            display_banner()
            category = list(categories.keys())[int(choice)-1]
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

if __name__ == '__main__':
    main()
