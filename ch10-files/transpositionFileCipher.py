# Transposiion Cipher Encrypt/Decrypt File
import time, os, sys, transpositonEncrypt, transpositionDecrypt

def main():
    inputFilename = './ch10-files/frankenstein.txt'
    # if a file with outputFilename already exists,
    # it will be overwritten
    outputFileName = './ch10-files/frankenstein_encrypted.txt'
    myKey = 10
    # set to 'encrypt' or 'decrypt'
    myMode = 'encrypt'

    # if input file doesn't exist, terminate early
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    # if output file already exists, give user a chance to quit
    if os.path.exists(outputFileName):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFileName))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in message from input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # Measure how long encryption/decryption takes
    startTime = time.time()

    if myMode == 'encrypt':
        translated = transpositonEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds...' % (myMode.title(), totalTime))

    # write out translated message to output file
    outputFileObj = open(outputFileName, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFileName))


# run main() if not imported as a module
if __name__ == '__main__':
    main()
