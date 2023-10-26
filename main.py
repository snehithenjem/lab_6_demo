
def decode(password):
    decoded = ''
    for i in password:
        i = int(i)
        i -= 3
        if i <= 0:
            i += 10
        decoded += str(i)
    return decoded


def main():
    while True:
        menu()
        user_input = int(input('\nPlease enter an option: '))
        if user_input == 1:
            # This allows the user to encode the password if they select option 1 from the menu
            password = input('Please enter your password to encode: ')
            password = encode(password)
            print('Your password has been encoded and stored!')
        elif user_input == 2:
            decoded = decode(password)
            print("The encoded password is " + password + ", and the original password is " + decoded + ".")
        elif user_input == 3:
            break


def menu():
    print('\nMenu')
    print('------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    # This prints out the initial menu that the user can choose from


def encode(password):
    encoded = ''
    for i in password:
        i = int(i)
        i += 3
        if i >= 10:
            i -= 10
        encoded += str(i)
    return encoded
    # This encodes the password by going digit by digit and adding 3


if __name__ == '__main__':
    main()