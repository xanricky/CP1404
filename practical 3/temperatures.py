def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = get_fahrenheit()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius1 = get_celsius()
            print("Result: {:.2f} C".format(celsius1)) #.format(celsius1) format the variable
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_celsius():
    #Convert Fahrenheit to Celsius
    fahrenheit1 = float(input("Fahrenheit: "))
    celsius1 = 5 / 9 * (fahrenheit1 - 32)
    return celsius1


def get_fahrenheit():
    # Convert Celsius to Fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

main()