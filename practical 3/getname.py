def main():
    user_name = get_userName()

    while  user_name == "":
        user_name = get_userName()
    print(user_name[1:len(user_name):2])


def get_userName():
    userName = str(input("Enter your name: "))
    return userName

main()