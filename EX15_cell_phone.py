
the_calls_duration = int(input("Enter youre call duration : "))
def the_monthly_bill(the_calls_duration):
    def call_fees(the_calls_duration):
        if the_calls_duration in range(1, 501):
            call_fee = the_calls_duration * 0.01
            return int(call_fee)
        elif the_calls_duration in range(501, 801):
            call_fee = the_calls_duration * 0.008
            return int(call_fee)
        else:
            call_fee = the_calls_duration * 0.005
            return int(call_fee)
    total_amount = call_fees(the_calls_duration)
    return f"total amount: {total_amount}$"

print(the_monthly_bill(the_calls_duration))
print("the following our billing policy : ")
print(" _______________________________________________\n"
      "|                    Fixed cost 25$             |\n"
      "|-----------------------------------------------|\n"
      "|Call duration(in seconds)| Charge($/per second)|\n"
      "|-------------------------|---------------------|\n"
      "|      001-500            |        0,01         |\n"
      "|      501-800            |        0,008        |\n"
      "|      801-802+           |        0,005        |\n"
      "|_________________________|_____________________|")