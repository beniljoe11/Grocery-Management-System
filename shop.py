import jo_shop as js

while True:
    print("1. Add Items")
    print("2. Remove Items")
    print("3. View Items")
    print("4. Total Price")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        js.Add_Item(name, price)

    elif choice == 2 :
        name = input("Enter the product name :")
        js.Remove_Item(name)

    elif choice == 3 :
        
        js.Display_Items()

    elif choice == 4 :
        js.Total_Price()

    elif choice == 5 :
        js.Exit_Program()
        break

    else:
        print("Invalid choice. Please try again.")


