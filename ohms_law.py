# CTE 123 Python Mini Project
# Project: Ohm's Law and Power Calculator
# Author: Okparaku Mitchell
# Course: ND1 Mechatronics Engineering

# This function checks that a number is positive.
def get_positive_number(message):
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value
            else:
                print("Error: Please enter a number greater than zero.")

        except ValueError:
            print("Error: Please enter a valid number.")


# This function calculates voltage, current, resistance and power.
def calculate_electricity():
    print("\nWhat would you like to calculate?")
    print("1. Voltage")
    print("2. Current")
    print("3. Resistance")
    print("4. Power")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # Voltage = Current x Resistance
        current = get_positive_number("Enter current in amperes (A): ")
        resistance = get_positive_number("Enter resistance in ohms: ")

        voltage = current * resistance
        power = current ** 2 * resistance

        print(f"\nVoltage = {voltage:.2f} V")
        print(f"Power = {power:.2f} W")

    elif choice == "2":
        # Current = Voltage / Resistance
        voltage = get_positive_number("Enter voltage in volts (V): ")
        resistance = get_positive_number("Enter resistance in ohms: ")

        current = voltage / resistance
        power = voltage * current

        print(f"\nCurrent = {current:.2f} A")
        print(f"Power = {power:.2f} W")

    elif choice == "3":
        # Resistance = Voltage / Current
        voltage = get_positive_number("Enter voltage in volts (V): ")
        current = get_positive_number("Enter current in amperes (A): ")

        resistance = voltage / current
        power = voltage * current

        print(f"\nResistance = {resistance:.2f} ohms")
        print(f"Power = {power:.2f} W")

    elif choice == "4":
        # Power = Voltage x Current
        voltage = get_positive_number("Enter voltage in volts (V): ")
        current = get_positive_number("Enter current in amperes (A): ")

        power = voltage * current

        print(f"\nElectrical Power = {power:.2f} W")

    else:
        print("Invalid choice. Please select a number from 1 to 4.")
        return

    # Extra feature: Check whether power exceeds the user's chosen limit.
    print("\n--- Circuit Power Status Checker ---")

    power_limit = get_positive_number(
        "Enter the power limit in watts (W): "
    )

    if power > power_limit:
        print("WARNING: Power exceeds your specified limit!")
    elif power == power_limit:
        print("NOTICE: Power is exactly at your specified limit.")
    else:
        print("STATUS: Power is within your specified limit.")


# Main program: repeat calculations until the user quits.
def main():
    print("====================================")
    print(" OHM'S LAW AND POWER CALCULATOR")
    print("====================================")

    while True:
        calculate_electricity()

        print("\nWould you like to perform another calculation?")
        answer = input("Enter yes or no: ").strip().lower()

        if answer == "no":
            print("Thank you for using the calculator!")
            break

        elif answer == "yes":
            continue

        else:
            print("Invalid response. The program will end.")
            break


# Start the program.
if __name__ == "__main__":
    main()
