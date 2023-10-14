bitcoin_value = int(input(" enter the value of bitcoin : "))
bitcoin_increase = int(input(" enter the increase value of bitcoin : "))

def calculate_bitcoin(bitcoin_value, bitcoin_increase):
    bitcoin_increase_value = bitcoin_increase *100
    total_bitcoin_value = bitcoin_value + bitcoin_increase_value
    print("bitcoin increase value :",bitcoin_increase_value)

    return total_bitcoin_value

print("bitcoin curent  : ",calculate_bitcoin(bitcoin_value, bitcoin_increase))



