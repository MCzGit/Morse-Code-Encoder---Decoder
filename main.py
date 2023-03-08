import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

#Function created to encode message.
def encode(message):
    encoding = ''
    for letter in message:
        if letter != ' ':
            #Searches the dictionary and adds the corresponding characters
            #Adds a space to separate morse codes different characters
            encoding += MORSE_CODE_DICT[letter] + ' '
        else:
            #One space indicates different characters, two spaces indicates different words
            encoding += ' '
    return encoding


#Function created to decode message.
def decode(message):
    #Added an extra space to access last morse code
    message += ' '

    decoding = ''
    encoded_text = ''

    for letter in message:
            #check for space
            if (letter != ' '):
                #counter to track space
                i = 0

                #tracking morse code of a single character
                encoded_text += letter

            #If there is space
            else:
                #if i=1 that indicates a new character
                i += 1

                #if i=2 that indicates a new word
                if i == 2:
                    #adding space to separate words
                    decoding += ' '
                else:
                    #retreiving the keys using their values (reversing encoding)
                    decoding += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(encoded_text)]
                    encoded_text = ''

    return decoding


#Main function created to provide menu for user to navigate through the various functions.
def main():

    while(True):
        print("\nWelcome to the Morse Code Translator\n")
        print("Please choose one of the available options\n")
        print("Enter '1'. To enter the message you wish to encode with Morse Code.\n")
        print("Enter '2'. To enter the Morse Code message you wish to decode.\n")
        print("Enter '3'. To exit the application.\n")

        menu = input()
        menu = int(menu)
        if menu == 1:
            print("\nEnter the message that you wish to encode with Morse Code: \n")
            data = input("")
            morse_code = encode(data.upper())
            print(f"\nYou're encoded message is: {morse_code}")
        elif menu == 2:
            print("\nEnter the message that you wish to decode to plain English: \n")
            data = input("")
            morse_to_english = decode(data)
            print(f"\nYou're decoded message is: {morse_to_english}")
        elif menu == 3:
            sys.exit("\nThank you for using the Morse Code Translator! Goodbye.\n")
        else:
            print("\nThe key you have entered is invalid.\n")
            print("Please try again.\n")
            print("Enter '1'. To enter the message you wish to encode with Morse Code.\n")
            print("Enter '2'. To enter the Morse Code message you wish to decode.\n")
            print("Enter '3'. To exit the application.\n")

            menu = input()
            menu = int(menu)
            if menu == 1:
                print("\nEnter the message that you wish to encode with Morse Code: \n")
                data = input("")
                morse_code = encode(data.upper())
                print(f"\nYou're encoded message is: {morse_code}")
            elif menu == 2:
                print("\nEnter the message that you wish to decode to plain English: \n")
                data = input("")
                morse_to_english = decode(data)
                print(f"\nYou're decoded message is: {morse_to_english}")
            elif menu == 3:
                sys.exit("\nThank you for using the Morse Code Translator! Goodbye.\n")


        print("\nTo run the Morse Code Convertor again enter 'Y'; to exit enter 'N': \n")
        run_again = input()

        if run_again == 'y' or run_again == 'Y':
            print("\nPlease choose one of the available options\n")
            print("Enter '1'. To enter the message you wish to encode with Morse Code.\n")
            print("Enter '2'. To enter the Morse Code message you wish to decode.\n")
            print("Enter '3'. To exit the application.\n")

            menu = input()
            menu = int(menu)
            if menu == 1:
                print("\nEnter the message that you wish to encode with Morse Code: \n")
                data = input("")
                morse_code = encode(data.upper())
                print(f"\nYou're encoded message is: {morse_code}")
            elif menu == 2:
                print("\nEnter the message that you wish to decode to plain English: \n")
                data = input("")
                morse_to_english = decode(data)
                print(f"\nYou're decoded message is: {morse_to_english}")
            elif menu == 3:
                sys.exit("\nThank you for using the Morse Code Translator! Goodbye.\n")
        
        print("\nTo run the Morse Code Convertor again enter 'Y'; to exit enter 'N': \n")
        run_again = input()

        if run_again == 'y' or run_again == 'Y':
            print("\nPlease choose one of the available options\n")
            print("Enter '1'. To enter the message you wish to encode with Morse Code.\n")
            print("Enter '2'. To enter the Morse Code message you wish to decode.\n")
            print("Enter '3'. To exit the application.\n")

            menu = input()
            menu = int(menu)
            if menu == 1:
                print("\nEnter the message that you wish to encode with Morse Code: \n")
                data = input("")
                morse_code = encode(data.upper())
                print(f"\nYou're encoded message is: {morse_code}")
            elif menu == 2:
                print("\nEnter the message that you wish to decode to plain English: \n")
                data = input("")
                morse_to_english = decode(data)
                print(f"\nYou're decoded message is: {morse_to_english}")
            elif menu == 3:
                sys.exit("\nThank you for using the Morse Code Translator! Goodbye.\n")

        elif run_again == 'n' or run_again == 'N':
            sys.exit("\nThank you for using the Morse Code Translator! Goodbye.\n")  

if __name__ == '__main__':
    main()

