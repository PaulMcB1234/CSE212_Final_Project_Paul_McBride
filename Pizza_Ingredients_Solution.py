def recipes(set1, set2):
    set3 = set()
    for i in set1:
        for j in set2:
            if i == j:
                set3.add(i)
    
    set4 = set()
    for i in set1:
        if i not in set2:
            set4.add(i)
    for j in set2:
        if j not in set1:
            set4.add(j)
    
    print(set3, set4)
    
pizza_1 = {"dough", "marinara sauce", "cheese"}
pizza_2 = {"dough", "marinara sauce", "cheese", "peperoni"}
recipes(pizza_1, pizza_2)

pizza_1 = {"dough", "barbaque sauce", "cheese", "chicken", "bacon"}
pizza_2 = {"dough", "marinara sauce", "cheese", "sausage", "bacon", "ham"}
recipes(pizza_1, pizza_2)

pizza_1 = {"dough", "spicy sauce", "jalapeno", "peperoni"}
pizza_2 = {"dough", "ranch sauce", "peperoni"}
recipes(pizza_1, pizza_2)
