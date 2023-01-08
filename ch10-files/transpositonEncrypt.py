# Transposition Cipher Encryption

import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    cipherText = encryptMessage(myKey, myMessage)

    # print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message
    print(cipherText + '|')

    # Copy the encrypted string in cipherText to the clipboard
    pyperclip.copy(cipherText)

def encryptMessage(key, message):

    #print(f'key = {key}')
    #print(range(key))

    # Each string in ciphertext represents a column in the grid
    ciphertext = [''] * key

    # Loop through each column in ciphertext
    for column in range(key):
        currentIndex = column

        #print(f'currentIndex = {currentIndex}')

        # Keep looping until currentIndex goes past the
        # message length
        while currentIndex < len(message):
            # Place the character at currentIndex in message
            # at the end of the current column in the
            # ciphertext list
            ciphertext[column] += message[currentIndex]

            # Move the currentIndex over
            currentIndex += key

        #print('-> ciphertext = %s' % (ciphertext))

    # Convert the ciphertext list into a single string value and
    # return it
    return ''.join(ciphertext)

# if transpositionEncrypt.py is run (instead of imported as a module)
# call the main() function
if __name__ == '__main__':
    main()
