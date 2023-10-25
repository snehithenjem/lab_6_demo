def main():
    while True:
        menu()
        user_input = int(input('\nPlease enter an option: '))
        if user_input == 1:
            password = input('Please enter your password to encode: ')
            password = encode(password)
            print('Your password has been encoded and stored!')

def menu():
    print('\nMenu')
    print('------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def encode(password):
    encoded = ''
    for i in password:
        i = int(i)
        i += 3
        if i >= 10:
            i -= 10
        encoded += str(i)
    return encoded

if __name__ == '__main__':
    main()
