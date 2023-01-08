# Transposition Cipher Decryption

import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plainText = decryptMessage(myKey, myMessage)

    # print with a | ("pipe" character)
    print(plainText + '|')

    pyperclip.copy(plainText)


def decryptMessage(key, message):
    # simulate "columns" and "rows" of grid
    # using list of strings

    # number of columns
    numOfColumns = int(math.ceil(len(message) / float(key)))

    # number of rows
    numOfRows = key

    # number of shaded boxes in last column
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # each string in plainText represents a column in the grid
    plainText = [''] * numOfColumns

    # the column and row variables point to where in the grid
    # the nexr character in the encrypted message will go
    column = 0
    row = 0

    for symbol in message:
        plainText[column] += symbol
        # point to next column
        column += 1

        # if no more columns or we're at a shaded box, go back
        # to first column and the next row
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plainText)

# if transpositionDecrypt.py is tun (instead of imported in a module),
# call the main() function
if __name__ == '__main__':
    main()



