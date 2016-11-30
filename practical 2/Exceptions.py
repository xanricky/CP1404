valid_input = False
while not valid_input:
    try:
        age = int(input("Age: "))
        valid_input = True
    except ValueError:
        print("Invalid (Not an integer.)")
print("Next year you will be", age+1)