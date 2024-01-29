#!/usr/bin/python3
grocery_list = []

while True:
    action = input("what would you like to do(add/view/remove/quit)")
    if action == "add":
        item = input("Enter item: ")
        grocery_list.append(item)
        print(f"'{item}' has been added to the list")
    elif action == "view":
        print("Grocery list: ")
        for item in grocery_list:
            print("-" + item)
    elif action == "remove":
        "input"
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"'{item}' has been removed")
    elif action == "quit":
        print('Goodbye')
        break
    else:
        print('Error: Invalid Option, please choose from list')