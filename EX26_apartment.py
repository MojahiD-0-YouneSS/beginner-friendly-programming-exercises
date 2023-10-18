def check_input():
    prices = []
    counter = 0
    while True:
        user_input = int(input("Enter apartment price: "))
        if user_input <= 0:
            break
        prices.append(user_input)
        counter += 1
    return prices, counter

prices, apartment_count = check_input()

def calculate_average(prices):
    total = sum(prices)
    return total / len(prices) if len(prices) > 0 else 0

average_price = calculate_average(prices)

print(f"{apartment_count} apartments have registered. The average price for rent is {average_price:.2f}$")

def compare_prices(prices, average_price):
    names = []
    for price in prices:
        if price > average_price:
            names.append("\"Above average price\",")
        elif price < average_price:
            names.append(",\"Below average price\"")
        else:
            names.append(",\"Equal to the average price\"")
    return names
print(*compare_prices(prices, average_price))

   
