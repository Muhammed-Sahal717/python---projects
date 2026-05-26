class ItemNotFoundError(Exception):
    pass

class OutOfStockError(Exception):
    pass

class InvalidQuantityError(Exception):
    pass

menu = {
    1: {"name": "Burger", "price": 120, "stock": 10},
    2: {"name": "Pizza", "price": 250, "stock": 5},
    3: {"name": "Shawarma", "price": 150, "stock": 8}
}

orders = []

def view_menu():

    print("\n------ MENU ------")

    for item_id, item in menu.items():

        print(
            item_id,
            item["name"],
            "- Rs", item["price"],
            "- Stock:", item["stock"]
        )

def add_item():

    try:
        item_id = int(input("Enter item ID: "))
        name = input("Enter item name: ")
        price = int(input("Enter item price: "))
        stock = int(input("Enter stock quantity: "))

        menu[item_id] = {
            "name": name,
            "price": price,
            "stock": stock
        }

        print("Item added successfully!")

    except ValueError:
        print("Enter numbers only!")

def place_order():

    try:
        view_menu()

        item_id = int(input("\nEnter item ID: "))
        quantity = int(input("Enter quantity: "))

        if item_id not in menu:
            raise ItemNotFoundError("Item not found!")

        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than 0")

        if quantity > menu[item_id]["stock"]:
            raise OutOfStockError("Not enough stock!")

        total = quantity * menu[item_id]["price"]

        menu[item_id]["stock"] -= quantity

        orders.append(
            f"{menu[item_id]['name']} x {quantity} = Rs {total}"
        )

        print("Order placed successfully!")
        print("Total Bill: Rs", total)

    except ItemNotFoundError as e:
        print("Order Error:", e)

    except InvalidQuantityError as e:
        print("Quantity Error:", e)

    except OutOfStockError as e:
        print("Stock Error:", e)

    except ValueError:
        print("Enter valid numbers only!")

def view_orders():

    print("\n------ ORDER HISTORY ------")

    if len(orders) == 0:
        print("No orders yet")

    else:
        for order in orders:
            print(order)

    print("----------------------------")




while True:

    print("\n===== RESTAURANT MANAGEMENT =====")

    print("1. View Menu")
    print("2. Add Item")
    print("3. Place Order")
    print("4. View Orders")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_menu()

    elif choice == "2":
        add_item()

    elif choice == "3":
        place_order()

    elif choice == "4":
        view_orders()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")