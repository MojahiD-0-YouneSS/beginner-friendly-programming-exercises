head_count = 0
tails_count = 0

while True:
    result = input("Enter 'head', 'tails', or 'stop': ")
    if result == "stop":
        break
    elif result == "head":
        head_count += 1
    elif result == "tails":
        tails_count += 1
    else:
        print("Invalid input. Please enter 'head', 'tails', or 'stop'.")

total_flips = head_count + tails_count

print(f"Head won {head_count} times and tails won {tails_count} times")
if total_flips > 0:
    head_percentage = (head_count / total_flips) * 100
    tails_percentage = (tails_count / total_flips) * 100
    print(f"{head_percentage:.0f}% Head, {tails_percentage:.0f}% Tails")
else:
    print("No flips recorded.")