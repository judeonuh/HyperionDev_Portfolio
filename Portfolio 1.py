"""
PORTFOLIO 1: PAWS AND CARTS

This project creates a shopping cart for a user.
The program allows a user to add, remove and view items in their cart.
The program also offers personalised suggestions to users based on the products in their cart.
On viewing the items in their cart, the users can also see the total cost of their items.
A few error handling techniques have been incorporated to capture invalid entries.
"""
# pylint: disable-msg=C0103

# Available products in the shop and their prices.
shop = {"Chicken Dog Treats" : 2.99, "Dogs Meat Selection" : 8.30, "Dogs Food Tins" : 10.50,
        "Dogs Cottage Pie" : 3.20, "Dogs Sunday Lunch" : 4.20, "Chicken Cat Food" : 6.00, 
        "Cats Mixed Selection" : 15.80, "Cats Country Medley" : 5.50, "Cat Food Pouches" : 5.75,
        "Cat Cake Tuna" : 1.20, "Cat Poultry Selection" : 4.50, "Bird Peanuts" : 6.00,
        "Bird Mealworms" : 2.00, "Bird Seeds" : 1.99, "Birds Insect Pellets" : 5.60, 
        "Peckish Seed Mix" : 5.00, "Orange" : 3.99, "Water Melon" : 4.60, "Pineapple" : 4.50,
        "Apple": 2.70, "Banana" : 1.50, "Guava" : 3.99, "Strawberry": 5.70, "Berry" : 4.99}

# Cartegorize related products
dogs_cart = {"Chicken Dog Treats" : 2.99, "Dogs Meat Selection" : 8.30, "Dogs Food Tins" : 10.50,
        "Dogs Cottage Pie" : 3.20, "Dogs Sunday Lunch" : 4.20}

cats_cart = {"Chicken Cat Food" : 6.00, "Cats Mixed Selection" : 15.80, "Cats Country Medley" : 5.50,
             "Cat Food Pouches" : 5.75, "Cat Cake Tuna" : 1.20, "Cat Poultry Selection" : 4.50}

birds_cart = {"Bird Peanuts" : 6.00, "Bird Mealworms" : 2.00, "Bird Seeds" : 1.99,
              "Bird Insect Pellets" : 5.60, "Peckish Seed Mix" : 5.00}

fruits_cart = {"Orange" : 3.99, "Water Melon" : 4.60, "Pineapple" : 4.50, "Apple": 2.70,
               "Banana" : 1.50, "Guava" : 3.99, "Strawberry": 5.70, "Berry" : 4.99}


mycart = {}
attempt = 0

# Print welcome page
print(f"{"-" * 90}\nWELCOME TO JP's PET SHOP\n{"-" * 90}")
shop_list = list(shop.items())
print("PRODUCTS AVAILABLE IN THE SHOP AND THEIR PRICES:\n")

for i,p, in shop.items():
    print(f"{i}:\t\t £{p}")
print(f"{"-" * 90}")

# Constantly prompt user for an input. Convert to lower case and remove trailing spaces
while True:
    user_prompt = input("MENU\n"
                        "Select:\n"
                        "A: To add item to cart from the product lists above\n"
                        "B: To remove item from cart\n"
                        "C: To view cart\n" 
                        "D: Proceed to checkout\n"
                        ">>> Please enter an option: ").strip().lower()
    print("")

    if user_prompt == "a" and not user_prompt.isdigit():

        # Validate user input and catch potential errors raised.
        try:
            user_item = input("Please enter the item you wish to add to cart: ").strip().title()
            item_price = float(input("How much is this item?: £"))
            while item_price != shop[user_item]:
                print(f"\n{"-" * 90}\nSorry! You have entered a wrong price!\n{"-" * 90}\n")
                item_price = float(input("How much is this item?: £"))
        except (ValueError, IndexError, KeyError, TypeError) as err_mess:
            print(f"\n{"-" * 90}\nYou have either entered a wrong price or typed in item wrongly!")
            print(f"\nError Message: {err_mess}\n{"-" * 90}\n")

        # Add validated item to user's cart and offer personalised product suggestions to user.
        if user_item in shop.keys():
            mycart.update({user_item : item_price})
            print(f"\n{"-" * 90}\n{user_item} has been added to your cart!\n{"-" * 90}\n")
            if user_item in dogs_cart:
                print("OTHER SUGGESTED DOG FOODS YOU CAN PICK FROM:\n")
                for a,b, in dogs_cart.items():
                    print(f"{a}:\t\t £{b}")
                print(f"\n{"-" * 90}\n")
            elif user_item in cats_cart:
                print("OTHER SUGGESTED CAT FOODS YOU CAN PICK FROM:\n")
                for a,b, in cats_cart.items():
                    print(f"{a}:\t\t £{b}")
                print(f"\n{"-" * 90}\n")
            elif user_item in birds_cart:
                print("OTHER SUGGESTED BIRD FOODS YOU CAN PICK FROM:\n")
                for a,b, in birds_cart.items():
                    print(f"{a}:\t\t £{b}")
                print(f"\n{"-" * 90}\n")
            elif user_item in fruits_cart:
                print("OTHER SUGGESTED FRUITS YOU CAN PICK FROM:\n")
                for a,b, in fruits_cart.items():
                    print(f"{a}:\t\t £{b}")
                print(f"\n{"-" * 90}\n")
        else:
            print(f"\nSorry! {user_item} is not available in the shop.\n")

    # Validate user input and remove the selected product from cart
    elif user_prompt.lower() == "b" and not user_prompt.isdigit():
        user_item = input("Please enter the item you wish to remove from cart: ").strip().title()
        if user_item in shop.keys():
            del mycart[user_item]
            print(f"\n{"-" * 90}\n{user_item} has been removed from your cart!\n{"-" * 90}\n")
        else:
            print(f"\nSorry! {user_item} is not in your cart.\n")

    # Return the contents of user's cart and the total price of the items in the cart
    elif user_prompt.lower() == "c" and not user_prompt.isdigit():
        if not mycart:
            print(f"{"-" * 90}\nYour cart is empty!\n{"-" * 90}")
        else:
            total_price = sum(mycart.values())
            print(f"{"-" * 90}\nThe items in  your cart are:\n{"-" * 90}")
            for x,y in mycart.items():
                print(f"{x}:\t\t £ {y}")
            print(f"{"-" * 90}\nTOTAL:\t\t £ {total_price:.2f}\n{"-" * 90}")   # Add discount option
            print("")

    # Direct user to checkout and apply any discount user is eligible for
    elif user_prompt.lower() == "d" and not user_prompt.isdigit():
        print(f"{"-" * 90}\nITEMS TO CHECKOUT:\n")
        for x,y in mycart.items():
            print(f"{x}:\t\t £ {y}")
        total_price = sum(mycart.values())
        print(f"{"-" * 90}\nTOTAL:\t\t £ {total_price:.2f}\n")
        discount = input("Please enter your discount voucher number: ").strip().lower()
        disc_vouch = ["dc50", "dc20",]
        if discount in disc_vouch and discount == "dc50":
            new_total_price = total_price - (0.5 * total_price)
            print(f"\n50% discount approved!\nPlease proceed to pay £{new_total_price:.2f} at the Checkout.\n{"-" * 90}")
            print("Thank you for shopping at JP's PET SHOP. Goodbye!\n")
            break
        elif discount in disc_vouch and discount == "dc20":
            new_total_price = total_price - (0.2 * total_price)
            print(f"\n20% discount approved!\nPlease proceed to pay £{new_total_price:.2f} at the Checkout.\n{"-" * 90}")
            print("Thank you for shopping at JP's PET SHOP. Goodbye!\n")
            break
        else:
            print("\nNo valid discount code has been entered!\n")
            print(f"Please proceed to pay £{total_price:.2f} at the Checkout.\n{"-" * 90}")
            print("Thank you for shopping at JP's PET SHOP. Goodbye!\n")
            break

    else:
        print("Sorry, that was an invalid entry!\n")
        attempt += 1
        if attempt == 3:
            print("Please hold. A shop assistant will be with you shortly. Thank you!\n")
            break
