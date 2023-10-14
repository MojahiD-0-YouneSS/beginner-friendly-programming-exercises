
def prise(money, btcoin_price, Ethereum_price, Litecoin3_price):
   bit_amount = int(money / btcoin_price)
   ethereum_amount = int(money / Ethereum_price)
   Litecoin3_amount = int(money / Litecoin3_price)
   return f"With {money}$ you can buy: {bit_amount} Bitcoins,  {ethereum_amount} Ethereum, and {Litecoin3_amount} Litecoins"

money = int(input("Enter your money amount : "))
btcoin_price = int(input("Enter your money amount : "))
Ethereum_price = int(input("Enter your money amount : "))
Litecoin3_price = int(input("Enter your money amount : "))
total = prise(money, btcoin_price, Ethereum_price, Litecoin3_price)
print(total)