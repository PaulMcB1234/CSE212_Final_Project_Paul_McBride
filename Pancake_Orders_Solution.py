def is_available(order):
    if order == "plain":
        return True
    elif order == "bluberry":
        return True
    elif order == "chocolate":
        return True
    else:
        return False
    
def pancake_orders(orders):
    stack = []
    for order in orders:
        if is_available(order):
            stack.append(order)
            print("Order up!")
        elif is_available(order) == False:
            print("That item is not on the menu.")
    
    return stack

orders = ["plain", "bluberry", "chocolate"]
print(pancake_orders(orders))

orders = ["bluberry", "apple", "plain", "chocolate", "chocolate"]
print(pancake_orders(orders))

orders = ["gluten free", "plain", "plain", "chocolate", "bluberry", "mango", "large", "plain", "large",]
print(pancake_orders(orders))
