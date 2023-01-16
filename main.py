import cryptoFunc

choice = input('Please type 1 for encrypt or 2 for decrypt: ')
file = input('Please give me a file name: ')

if choice == '1':
    cryptoFunc.encrypt_file(file)
elif choice == '2':
    cryptoFunc.decrypt_file(file)

print('Successfull')