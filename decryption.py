from helpers import *
from keyGen import *

####   decryption part 
def dec64Block(data_64bits, keys, initPerm,finalPerm): 
    initPermRes = permutateAny(data_64bits,initPerm)  # 64 bits
    lPrev = initPermRes[:32]  # divide
    rPrev = initPermRes[32:]

    currL = ""
    currR = ""
    
    for i in range(16): 
        currL = rPrev
        # start from k16 ; decryption 
        # mangRes = mangularFunc(rPrev,keys[i])
        mangRes = mangularFunc(rPrev,keys[16-1-i])
        currR = xoring(lPrev, mangRes)
        lPrev = currL 
        rPrev = currR

    # now, i have l16, r16 
    tmp = currL         # swaping 
    currL= currR
    currR = tmp 
    # inverse perm. here 
    res = currL+currR
    inversePerm = permutateAny(res,finalPerm)
    return inversePerm


def decryptCiphertxt(): 
    ciphertxt = ""
    
    # read from file    
    with open('inputDec.txt', 'r') as inputfile:
        lines = inputfile.readlines()
        for line in lines:
            ciphertxt+= line.strip()

    # handle different sizes of ciphertxt data as input
    if (len(ciphertxt) % 8 !=0):  # if len % 8!=0 :  add extra special chars
        rem = len(ciphertxt)%8 
        end = 8 - rem 
        extra =""
        for i in range (end):
            # extra+= "$"
            extra+= "®"
        ciphertxt= ciphertxt + extra
    
    # get keys 
    generatedKeys = generateKeys()
    # generatedKeys = testKeys
    
    # open file to write 
    with open('outputDec.txt', 'w') as file:

        # loop on cipher data and access every 8 ascii chars together 
        for i in range(0,len(ciphertxt),8):   
            block8Chars = ciphertxt[i:i+8]  # access data // specific 8 chars
        
            block_in_bits = ""
            for j in block8Chars:    # convert 8 chars to 64 bits 
                ch = ord(j) 
                ch = format(ch, '08b')
                block_in_bits+= ch
        
            # encryptedData = enc64Block(block_in_bits,generatedKeys,initP,finalP)  #  call encBlock64 func.// return 64 bits
            # replace with dec64Block func. 
            decryptedData = dec64Block(block_in_bits,generatedKeys,initP,finalP)
        # data as 01011101.  convert to ascci 
        # open file to write 
            # with open('output.txt', 'w') as file:
            for j in range(0,64,8): # for each 8 convert to one ascii char 
                cut = decryptedData[j:j+8]   # access data 
                binCut = int(cut,2)    # convert to bin
                asciiCut = chr(binCut)  # ascii char 
                if asciiCut=="®":
                    continue

                file.write(asciiCut)  # write to file 