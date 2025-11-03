# Module Lab: Caesar Cipher Program Bug #2
#
# In a previous lab, you created a Caesar cipher program. This version of
# the program is buggy. Use a debugger to find the bug and fix it.

# Double the given alphabet
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Get a message to encrypt
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Get a cipher key
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

# Encrypt message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# Decrypt message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Main program logic
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')

# Main logic
runCaesarCipherProgram

'''
that is after removing the $ in line 56
voclabs:~/environment $ python3 -m pdb debug-caesar-2.py
Traceback (most recent call last):
  File "/usr/lib64/python3.8/pdb.py", line 1705, in main
    pdb._runscript(mainpyfile)
  File "/usr/lib64/python3.8/pdb.py", line 1573, in _runscript
    self.run(statement)
  File "/usr/lib64/python3.8/bdb.py", line 580, in run
    exec(cmd, globals, locals)
  File "<string>", line 1, in <module>
  File "/home/ec2-user/environment/debug-caesar-2.py", line 56
    runCaesarCipherProgram$
                          ^
SyntaxError: invalid syntax
voclabs:~/environment $ python3 -m pdb debug-caesar-2.py
> /home/ec2-user/environment/debug-caesar-2.py(7)<module>()
-> def getDoubleAlphabet(alphabet):
(Pdb) a
(Pdb) a
(Pdb) l
  2     #
  3     # In a previous lab, you created a Caesar cipher program. This version of
  4     # the program is buggy. Use a debugger to find the bug and fix it.
  5  
  6     # Double the given alphabet
  7  -> def getDoubleAlphabet(alphabet):
  8         doubleAlphabet = alphabet + alphabet
  9         return doubleAlphabet
 10  
 11     # Get a message to encrypt
 12     def getMessage():
(Pdb) n
> /home/ec2-user/environment/debug-caesar-2.py(12)<module>()
-> def getMessage():
(Pdb) '''