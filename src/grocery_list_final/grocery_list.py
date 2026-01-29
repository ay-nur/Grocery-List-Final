"""
Grocery list
by. Ayca Erdogan
Description: Program that helps user create a grocery list for their next errand/grocery run by using functions, indexing, lists, user input, output, and decisions.
""" 

def always_items(get):
    get = get.split()
    return tuple(get)

def add_items(add):
    return add.split()

def remove_items(delete):
    return delete.split()

def grocery_list():
    """
    This is the main function that uses all functions to make the grocery list.
    """
    always_list = always_items(input("What items do you always buy when headed to the grocery store? "))
    ans = input("Add items to list? (Y/N): ")
    ans = ans.lower()
    if ans == "y":
        add_list = add_items(input("What items do you want to add to your list? "))
    else: 
        add_list = ""
    ans = input("Remove items from list?: ")
    ans = ans.lower()
    if ans == "y":
        remove_list = remove_items(input("What items do you want to remove from your list? "))
    else:
        remove_list = ""
    glist = [always_list] + add_list

    for item in remove_list:
        if item in glist:
            glist.remove(item)
    print("--------------")
    print("Here is your grocery list:")
    return glist

def show_list():
    print("--------------")
    for item in grocery_list():
        print(item)
    
print(show_list())