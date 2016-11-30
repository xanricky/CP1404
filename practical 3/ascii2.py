lower = 10
upper = 50

def main():
    num1 = get_number(lower, upper)

    value = 'Value'
    character = 'Char'
    print("\n{:^8s} {:^8s}".format(value, character))
    print("{:^8d} {:^8s}".format(num1, chr(num1)))


def get_number(lower, upper):
    num1 = int(input("Enter a number (10-50): "))
    while num1 < 10 or num1 > 50:
        print("Please enter a valid number!")
        num1 = int(input("Enter a number (10-50): "))
    else:
        return num1

main()