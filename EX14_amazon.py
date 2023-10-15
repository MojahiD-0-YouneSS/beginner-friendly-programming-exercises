produt_cost = int(input("enter product cost : "))
location = input("Enter youre current location (USA or Europe or Canada or Other ): ")
def calculation_of_the_cost(produt_cost, location):
    def location_fees(location):
        if location == "USA":
            fee = 5
            return fee
        elif location == "Europe":
            fee = 7
            return fee
        elif location == "Canada":
            fee = 3
            return fee
        else:
            fee = 9
            return fee
        
    total_cost = location_fees(location) + produt_cost
    return f"You have to pay {total_cost}$, {produt_cost}$ for the product and {location_fees(location)}$ for shipping cost"

print(calculation_of_the_cost(produt_cost, location))