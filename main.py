# Armstrong Number Checker
print("===== ARMSTRONG NUMBER CHECKER =====")

# TODO 1: Ask for a number with input() and save it in number.
# Keep it as text. Do not use int() here.
number = input("Enter a number: ")

# TODO 2: Count the digits.
# 2a: Save len(number) in digit_count.
digit_count = len(number)
# 2b: Print "Number of digits: " and the count, using an f-string.
print(f"Number of digits: {digit_count}")

total = 0

# TODO 3: Loop through each digit in number.
for digit in number:
    # 3a: Make power = int(digit) ** digit_count
    power = int(digit) ** digit_count
    # 3b: Print "<digit> to the power <digit_count> = <power>"
    print(f"{digit} to the power {digit_count} = {power}")
    # 3c: Add power to total using +=
    total += power

# TODO 4: Show the result.
# 4a: Print "Sum of the powers = <total>"
print(f"Sum of the powers = {total}")

# 4b: If total equals int(number), print "<number> is an Armstrong number."
# Otherwise print "<number> is not an Armstrong number."
if total == int(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
