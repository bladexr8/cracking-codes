# Caesar Cipher Hacker

# message to descrypt
message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'

# Every possible symbol that can be decrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop through every possible key
for key in range(len(SYMBOLS)):
    # important to set translated to blank string
    # so previous iteration's value is cleared
    translated = ''

    # rest of program is almost same as Caesar Cipher Program

    # Loop through each symbol in message
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle wraparound
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol
            translated = translated + SYMBOLS[translatedIndex]

        else:
            translated = translated + symbol

    # Display every possible decryption
    print('Key #%s: %s' % (key, translated))

