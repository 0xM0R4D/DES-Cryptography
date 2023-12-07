from keyGen import permutateAny # get keys
from keyGen import generateKeys 

## after modification
# from helpers import expandFunc,mangularFunc,xoring,initP,finalP
from helpers import *


Ri_test= "01100001011000010111001101100100"
kj_test= "111000010110000101110011011111111010101011110000"


def enc64Block(data_64bits, keys, initPerm,finalPerm): 
    initPermRes = permutateAny(data_64bits,initPerm)  # 64 bits
    lPrev = initPermRes[:32]  # divide
    rPrev = initPermRes[32:]

    currL = ""
    currR = ""
    
    for i in range(16): 
        currL = rPrev 
        mangRes = mangularFunc(rPrev,keys[i])
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


#1234aaaa
# testKeys = ['011000000011110001100100010001010010000011000000', '010000001011010001110100010000001010001001000001', 
#             '110001001100010001110110011100101000010000001000',
#              '111001101100001100100010000010000001010100001010', '101010101001001100100011000011000111000000100000',
#                '101010010001001001011011011000000100100001100000', '001001010101001011011000100000001000100000011010',
#                  '000101100101100111010000100001010001011000010000', '000101100100100101010001100010010001001000000000', 
#                  '000011110110100100010101010100000100001000100100', 
#                  '000011110010010110001101000100000000100010001100', '010110110000010010101001100000000011000010010001',
#                    '110110011000100010101000001000110010001000100001', '100100001010101010001110001100100000100100000010',
#                    '001100000011111000000110000001000000000100010110', '011100000011111000000100100001000000000111000000']


def encryptPlaintext(): 
    plaintext = ""
    
    # read from file    
    with open('inputEnc.txt', 'r') as inputfile:
        lines = inputfile.readlines()
        for line in lines:
            plaintext+= line.strip()

    # handle different sizes of plaintext data as input
    if (len(plaintext) % 8 !=0):  # if len % 8!=0 :  add extra special chars
        rem = len(plaintext)%8 
        end = 8 - rem 
        extra =""
        for i in range (end):
            # extra+= "$"   #®
            extra+= "®"   
        plaintext = plaintext + extra
    
    # get keys 
    generatedKeys = generateKeys()
    # generatedKeys = testKeys
    
    # open file to write 
    with open('outputEnc.txt', 'w') as file:

        # loop on data and access every 8 ascii chars together 
        for i in range(0,len(plaintext),8):   
            block8Chars = plaintext[i:i+8]  # access data // specific 8 chars
        
            block_in_bits = ""
            for j in block8Chars:    # convert 8 chars to 64 bits 
                ch = ord(j) 
                ch = format(ch, '08b')
                block_in_bits+= ch
        
            encryptedData = enc64Block(block_in_bits,generatedKeys,initP,finalP)  #  call encBlock64 func.// return 64 bits
        # data as 01011101.  convert to ascci 
        # open file to write 
            # with open('output.txt', 'w') as file:
            for j in range(0,64,8): # for each 8 convert to one ascii char 
                cut = encryptedData[j:j+8]   # access data 
                binCut = int(cut,2)    # convert to bin
                asciiCut = chr(binCut)  # ascii char                     
                file.write(asciiCut)  # write to file 


