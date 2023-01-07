# Caesar Cipher

import pyperclip

# The string to be encrypted/decrypted
message = 'This is my secret message.'

# The encryption/decryption key
key = 13

# Whether program encrypts or decrypts
# set to 'encrypt' or 'decrypt'
mode = 'encrypt'

# Every possible symbol that can be decrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store encrypted/decrypted form of message
translated = ''

# Perform encryption/decryption
for symbol in message:
    # Note: Only symbols in SYMBOLS string can be encrypted/decrypted
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # encrypt/decrypt the symbol
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle wraparound, if needed
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]

    else:
        # Append symbol without encrypting/decrypting
        translated = translated + symbol

# Output the translated string
print(translated)
pyperclip.copy(translated)