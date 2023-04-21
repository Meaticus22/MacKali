#!/usr/bin/env python

from core.categories import *
import sys, os

# colors
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[33m"
cyan = "\033[1;36m"
reset = "\033[0m"

# option menu
menu_list = {
    "1":"show_categories",
    "2":"update",
    "3":"help",
    "4":"exit",
    "show":"show_categories",
    "clear":"clean_screen",
    "update":"update",
    "help":"help",
    "exit":"exit",
}

menu_list_set = {
    "load":"load_category",
    "search":"search_tool"
}

def load(function, param=False):
    """
    If the function exists, it is loaded
    """
    if param == False:
        globals()[function]()
    else:
        globals()[function](param)

def show_categories():
    """
    Displays the categories available in the 'categories' dictionary of the core/categories.py file
    """
    print "\n%s:: Categories:%s\n" %(green, reset)
    for name in categories.items():
        category = name[1][0]
        category = format(category)
        if name[0]%2 != 0:
            print " "+str(name[0]).rjust(2) + ")", category.ljust(23)[:23],
        else:
            print " "+str(name[0]).rjust(2) + ")", category
    print " "

def load_category(key):
    """
    When loading a category you can install one or more tools of that category
    """
    if int(key) in categories.keys():
        os.system('clear')
        category = categories[int(key)][0]
        category = format(category)
        print green + ":: " + category + reset + "\n"
        show_tools(categories[int(key)][1])
        tools = categories[int(key)][1]
        site = categories[int(key)][0]
        action = False
        while action == False:
            try:
                option = raw_input(": MacKali (%s%s%s) > " %(yellow, site, reset))
            except KeyboardInterrupt:
                delete_repository()
                print "..."; break
            try:
                if option == 'back':
                    delete_repository()
                    break
                elif option == 'clear':
                    os.system('clear')
                elif option == 'show':
                    show_tools(categories[int(key)][1])
                elif option == 'help':
                    help(True)
                elif option == '99':
                    add_repository()
                    for tool in tools:
                        install_tool = "apt install -y " + tool
                        os.system(install_tool)
                elif int(option) in range(1,len(tools)+1):
                    add_repository()
                    install_tool = "apt install -y " + tools[int(option)-1]
                    os.system(install_tool)
            except:
                pass
    else:
        print red + "E: The command is invalid!" + reset

def search_tool(tool):
    """
    Shows in which category the tool you are looking for is available
    """
    print ": Find " + yellow + tool + reset
    print ": Available in:"
    for lists in categories.items():
        tools = lists[1][1]
        category = lists[1][0]
        category = format(category)
        if tool in tools:
            print " [%s+%s] %s" %(green, reset, category)

def show_tools(tools):
    """
    Show all tools in the loaded category
    """
    for tool in enumerate(tools):
