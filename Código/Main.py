import random
import string


#this loop will maintain as long as the user don't write a number bigger than 6
while True:
    password = int(input('How long do you want your password to be? '))
    if password < 6:
        print('The password has to be longer than this')
    else:
        break
lettersv = int(input('How many letters do you want(they will be in uppercase and lowercase)'))
numbers = int(input('And how many numbers do you want?'))
#this loop will maintain as long as the user don't get satisfied with de password generated
while True:
    letters = []
    numberl = []
    passwordl = []
    #this repetition structure will add random ascii letters to the list letters
    for c in range(0, lettersv):
        letters.append(random.choice(string.ascii_letters))
    #this repetition structure will add random numbers to the list numbers
    for c in range(0, numbers):
        numberl.append(random.randint(0, 10))
    #we add the list letters to the list numeros in the list senhaa
    passwordl = numberl + letters
    #here, we do a subtraction of the size of the password required with de sum of the lists letters and numbers, to discover the number of blank spaces, and fill them with symbols
    symbol = password - (lettersv + numbers)
    #verification if there are any blank spaces, and if so, fill them with symbols in the repetition structure down below
    if symbol > 0:
         for c in range(0, symbol):
             passwordl.append(random.choice(string.punctuation))
    #randomizing all the elements in the lista passwordl,
    random.shuffle(passwordl)
    #printing one by one the characters of the password
    for c in range(0, len(passwordl)):
        print(passwordl[c], end='')
    print("\n\nDoes this password satisfies you??\n[Y] yes\n[N] no")
    verify = input()
    if verify == 'Y' or verify == 'y':
        break

