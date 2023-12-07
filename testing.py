# test= input()
# print(len(test))

# ch= ord('0')
#     # ch=str(bin(ch))
# ch = format(ch, '08b')
# print(ch)


pc1=[57, 49, 41, 33, 25, 17, 9, 1,
     58, 50, 42, 34 ,26, 18, 10, 2,
     59, 51, 43, 35, 27, 19, 11, 3,
     60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4]

# print(pc1[55])
# for i in range(2):
#     print(i)


# testStr = "asdf"
# testStr[2] = "3"
# print(testStr)


keyPerm1 = "thisisemptystringthisisemptysBePatientGoodThingsTakeTime"     # any 56 chars for itiialize string
keyPerm1_list = list(keyPerm1)
keyLeft = keyPerm1[:28]

# print(keyLeft)
# print(len(keyLeft))
# keyRight= keyPerm1[28:]

# print(keyRight)
# print(len(keyRight))binStr = "0110"
# decimal_value = int("0111", 2)
# print(decimal_value)

val = 3
binVal = bin(val)[2:]
binVal = binVal.zfill(4)  #  in 4 bit representation
binStr = str(binVal)            
# print(binStr)



# ok func. but replaced with one. to used in general 
# def permutate_InMangFunc(sBoxesRes):  # take 32 bits , return 32 bits 
#     p_box =  [16, 7, 20, 21, 29, 12, 28, 17,        # 32 len 
#               1, 15, 23, 26, 5, 18, 31, 10,
#               2, 8, 24, 14, 32, 27, 3, 9,
#               19, 13, 30, 6, 22, 11, 4, 25 ]
# #  10010010011010010110010101111111   
#     permRes = "xxxxxBePatientGoodThingsTakeTime"     # any 32 chars for itiialize string
#     permRes = list(permRes)  # convert to list to modify it1
#     for i in range(32): 
#         permRes[i] = str(sBoxesRes[p_box[i]-1])      # -1; 0-based 
#     permRes = ''.join(permRes) # covert to string again

#     return permRes 

# pe=permutate_InMangFunc(sbx)
# print("perm res:          ",pe )

# test = ""
# # test = "23232"
# if (1==1): 
#     test ="aa"
# print(test)




# convert bin as string to ascii char 
# x = "00110010"
# binX = int(x, 2)
# # print(binX)
# asc = chr(binX)
# print(asc)

# with open('testOut.txt', 'w') as file:
#     # Write the ASCII character to the file
#     file.write("ASCII character: " + asc)

# ascii_value = 11

# # Convert integer to ASCII character
# ascii_character = chr(ascii_value)

# st = "asdfgkljle"

# # Open a file in write mode
# with open('output.txt', 'w') as file:
#     # Loop through each character in the string
#     for char in st:
#         # Process the character and write it to the file
#         ascii_value = ord(char)  # Get ASCII value
#         file.write(chr(ascii_value))  # Write the character directly to the file



# with open('inputEnc.txt', 'r') as file:
#     # Read the entire contents of the file
#     file_contents = file.read()
#     print(file_contents)  # Print or use the file contents as needed

with open('inputEnc.txt', 'r') as file:
    lines = file.readlines()
    output =""
    for line in lines:
        output+= line.strip()
    # output = ''.join(lines[i].strip()[-1] + lines[i + 1].strip()[0] for i in range(len(lines) - 1))

# print(output)




    # for i in range(0,len(plaintext),8):   
    #     block8Chars = plaintext[i:i+8]  # access data // specific 8 chars
        
    #     block_in_bits = ""
    #     for j in block8Chars:    # convert 8 chars to 64 bits 
    #         ch = ord(j) 
    #         ch = format(ch, '08b')
    #         block_in_bits+= ch
        
    #     encryptedData = enc64Block(block_in_bits,generatedKeys,initP,finalP)  #  call encBlock64 func.// return 64 bits
    #     # data as 01011101.  convert to ascci 
    #     # open file to write 
    #     with open('output.txt', 'w') as file:
    #         for j in range(0,64,8): # for each 8 convert to one ascii char 
    #             cut = encryptedData[i:i+8]   # access data 
    #             binCut = int(cut,2)    # convert to bin
    #             asciiCut = chr(binCut)  # ascii char 
    #             file.write(asciiCut)  # write to file 

# test = 22
# def update():
#     # global test
#     s = test +3
#     print(s)
# update()
# print(test)    
# print(6%5)


# old expand func. 
# def expand(Ri):       # take Ri(32 bits) return 48 bits    
#     ### take Ri as string convert to list 
#     # Ri_list = list(Ri)
#     ret= [] 
#     for i in range(0,32,4): 
        
#         if i==0: 
#             ret.append( Ri[31]+Ri[0:5])
#         elif i==28: 
#             ret.append(Ri[i-1:]+ Ri[0])
#         else: 
#             ret.append(Ri[i-1:i+5])
        
#     ret = ''.join(ret) # convert to string 
#     return ret 
test = "12345678"
shiftRight1 = test[-1]+test[:-1]
print(shiftRight1)

shiftRight2 = test[-2:] + test[:-2]
print(shiftRight2)