staying_hours = int(input("Enter your staying hours : "))
mebership_validation = input(" are you a meber , Y(for yes), N for (for no):")
def cafe_charges(mebership_validation):
    def mebers_harges(staying_hours):
            Tax = 10
            cost_hours = staying_hours * 2
            total_cost = cost_hours + (cost_hours * Tax) / 100
            return total_cost
    def not_mebers_harges(staying_hours):
            Tax = 20
            cost_hours = staying_hours * 5
            total_cost = cost_hours + (cost_hours * Tax) / 100
            return total_cost

    if mebership_validation == "Y":
        return mebers_harges(staying_hours)
    elif mebership_validation == "N":
         return not_mebers_harges(staying_hours)
    else:
        return "invalid input please identify your mebership"

print(cafe_charges(mebership_validation))
