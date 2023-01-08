import random, sys, transpositonEncrypt, transpositionDecrypt

def main():
    # set random seed to a static value
    random.seed(42)

    for i in range(20):
        # run 20 tests

        # generate random messsages to test
        
        # message will have a random length
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # convert message string to a list to shuffle it
        message = list(message)
        random.shuffle(message)
        # convert list back to a string
        message = ''.join(message)

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        # Check all possible keys for each message
        for key in range(1, int(len(message)/2)):
            encrypted = transpositonEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            # if decryption doesn't match original, display
            # an error and quit
            if message != decrypted:
                print('Mismatch with key %s and message %s' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('Transposition cipher test passed')

# if not imported as a module, call main() function
if __name__ == '__main__':
    main()

