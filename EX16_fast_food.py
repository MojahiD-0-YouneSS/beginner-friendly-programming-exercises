print(" _________________________\n"
      "|    Meal   |    Price    |\n"
      "|-----------|-------------|\n"
      "|   Burger  |    5$       |\n"
      "|   Pizza   |   3$        |\n"
      "|   Hot Dog |   1,5$      |\n"
      "|___________|_____________|")
order = input("Enter your meal : ")
Burger = 5
Pizza = 3
Hot_Dog = 1.5
def meal_cost(order):
    if order == 'Burger':
        return f"{order} costs {Burger}$"
    elif order == 'Pizza':
        return f"{order} costs {Pizza}$"
    elif order == 'Hot Dog':
        return f"{order} costs {Hot_Dog}$"
    else:
        return "ivalid order!"

print(meal_cost(order))