working_hours = int(input("Enter youre hourd of work : "))
income_hours = int(input("Enter youre hourly income : "))
income = income_hours * working_hours
def what_i_can_buy():
    PS4_costs = 200
    Samsung_phone = 900
    TV = 500
    game_skin = 9.99
    return f"I can buy {int(income / PS4_costs)} PS4, {int(income / Samsung_phone)} Samsung, {int(income / TV)} TV, 80 game skin"
print(what_i_can_buy())
