
# This project was made to relate to my LED circuit experiment.
# done using the Falstad Circuit Simulator.Have fun :)
# This Python calculator calculates current or resistance.
# for a simple circuit, with or without an LED.

print("Electrical Circuit Calculator")
print("Calculate current or resistance with or without an LED.\n")

try:
    S_V = float(input("Enter supply voltage (V): "))
    led_choice = input("Do you want to include an LED? Enter y or n: ").lower()

    if S_V <= 0:
        print("Supply voltage must be greater than zero.")

    elif led_choice == "y":
        L_V = float(input("Enter LED forward voltage (V): "))

        if L_V < 0 or L_V >= S_V:
            print("LED voltage must be non-negative and less than supply voltage.")

        else:
            find = input("What do you want to find: current or resistance? ").lower()

            if find == "current":
                R = float(input("Enter resistance (ohms): "))

                if R <= 0:
                    print("Resistance must be greater than zero.")
                else:
                    I = (S_V - L_V) / R
                    print(f"Current = {I:.4f} A")
                    print(f"Current = {I * 1000:.2f} mA")

            elif find == "resistance":
                I = float(input("Enter current (A): "))

                if I <= 0:
                    print("Current must be greater than zero.")
                else:
                    R = (S_V - L_V) / I
                    print(f"Resistance = {R:.2f} ohms")

            else:
                print("Please enter current or resistance.")

    elif led_choice == "n":
        find = input("What do you want to find: current or resistance? ").lower()

        if find == "current":
            R = float(input("Enter resistance (ohms): "))

            if R <= 0:
                print("Resistance must be greater than zero.")
            else:
                I = S_V / R
                print(f"Current = {I:.4f} A")
                print(f"Current = {I * 1000:.2f} mA")

        elif find == "resistance":
            I = float(input("Enter current (A): "))

            if I <= 0:
                print("Current must be greater than zero.")
            else:
                R = S_V / I
                print(f"Resistance = {R:.2f} ohms")

        else:
            print("Please enter current or resistance.")

    else:
        print("Invalid choice. Please enter y or n.")

except ValueError:
    print("Invalid input. Please enter numerical values where required.")
