
grocery_list = {}


def Add_Item(name,price):

    grocery_list[name] = price

    print(f"{name} added to the grocery list with price {price}")



def Remove_Item(name):    

    if name in grocery_list:
        
        del grocery_list[name]

        print(f"{name} removed from the grocery list.")
    else:

        print(f"{name} not found in the grocery list.")

def Display_Items():

    print("grocery_List:")

    for items,price in grocery_list.items():
       
        print(f"{items} {price}")

def Total_Price():

    total = sum(grocery_list.values())

    print(f"Total price of all items: ${total}")

def Exit_Program():
    print("Exiting the program...")