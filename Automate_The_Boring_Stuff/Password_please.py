import os
passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
while True:
    typedPassword = input('Enter your password\n')
    if typedPassword == secretPassword:
        print('Access granted')
        break
    elif typedPassword == '12345':
        print('That password is one that an idiot puts on their luggage.\n')
    else:
        print('Access denied\n')

os.startfile('chest.jpg')
