"""
PAWS AND CARTS

"""

shop = {"tomato", "apple", "mango", "fish", "orange", "beef", "turkey", "chicken", "milk", "egg",
        "pepper", "biscuit", "chocolate", "bread", "potato", "pizza", "crisp", "sausage"}

mycart = []
attempt = 0
while True:
    user_prompt = input("MENU\n"
                        "Please enter:\n"
                        "A: To add item to cart\n"
                        "B: To remove item from cart\n"
                        "C: To view cart\n" 
                        "D: To cancel\n"
                        "Enter: ").lower()
    print("")

# ERROR TO CHECK: What happens if user capitalizes the first letter of the item?
    if user_prompt.lower() == "a" and not user_prompt.isdigit():
        user_item = input("Please enter the item you wish to add to cart: ").lower()
        if user_item in shop:
            mycart.append(user_item)
            print(f"{user_item} has been added to your cart!\n")
        else:
            print(f"Sorry! {user_item} is not available in the shop.\n")

    elif user_prompt.lower() == "b" and not user_prompt.isdigit():
        user_item = input("Please enter the item you wish to remove from cart: ").lower()
        if user_item in mycart:
            mycart.remove(user_item)
            print(f"{user_item} has been removed from your cart!\n")
        else:
            print(f"Sorry! {user_item} is not in your cart.\n")

    elif user_prompt.lower() == "c" and not user_prompt.isdigit():
        if mycart == []:
            print("Your cart is empty!\n")
        else:
            print("The items in  your cart are:")
            [print(x) for x in (mycart)]
            print("")

    elif user_prompt.lower() == "d" and not user_prompt.isdigit():
        print("Thank you for shopping with us. Goodbye!")
        break
    else:
        print("Sorry, that was an invalid entry!\n")
        attempt += 1
        if attempt == 3:
            print("Please call a shop assistant for help. Thank you!\n")
            break
