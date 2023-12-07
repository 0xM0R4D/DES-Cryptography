from encryption import *
from decryption import *

# main function 
def main():
    choice = int(input("Welcome to DES Program!!\nIMPORTANT: case encryption, enter plaintext firstly in inputEnc.txt file and the output will be returnted in ouputenc.txt file, while case decryption, enter ciphertext in inputDec.txt file and the ouput will be returned to ouputDec.txt file.\nPlz, enter 1 for encryption and 2 for decryption: "))
    while True:
        if choice==1:
            encryptPlaintext()
            break
        elif choice==2:
            decryptCiphertxt()
            break
        else:
            choice = int(input("Error!!\nchoice must be 1 or 2\nPlz, enter 1 for encryption and 2 for decryption: "))



# derive main 

main()