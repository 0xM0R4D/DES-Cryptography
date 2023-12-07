def permutateAny(goal,perm_table):  #goal is str, perm_table list  // to use in perm. in general 
    res_init = "thisisemptystringthisisetringFREEPALASTINEBePatientGoodThingsTakeTime"     # any 64 chars for itiialize string
    size = len(perm_table)
    permRes = res_init[0:size]
    permRes = list(permRes)  # convert to list to modify it
    for i in range(size): 
        permRes[i] = str(goal[perm_table[i]-1])      # -1; 0-based 
    permRes = ''.join(permRes) # covert to string again

    return permRes

# take input and send keys to encryption/decrytion function
def setKeyRet(): # set and return
    key =""
    key = input("Enter your key: ")
    while True:
        if len(key)==8:
            break
        else:
            key =input("Error!!\nyour key length not equal 8.\nPlz, enter key its length equal 8: ")
    return key 

# convert key from chars to bits    // by converting char to ascci number then convert nuber to bits 
def getInitKey_in_bits(settedKey): 
    key_in_bits = ""
    for i in settedKey:
        ch= ord(i)
        # ch=str(bin(ch))
        ch = format(ch, '08b')
        key_in_bits+=ch
    return key_in_bits 


# divide into 2 subkeys, apply rounds and concatenated res 

def divideApplyRoundsConc(perm1Res):  # 0 for encryption and 1 for decryption
   # divide into 2 subkeys, apply rounds and concatenated res
    keyLeft= perm1Res[:28]    
    keyRight=perm1Res[28:]
    # create list of left subkeys     and  same for right 
    leftSubKeys = []
    rightSubKeys= []
    
    
    # round 1  
    leftSubKeys.append(keyLeft[1:]+keyLeft[0])
    rightSubKeys.append(keyRight[1:]+ keyRight[0])

    for i in range(1,16):  # from round 2 to 16 
        prevLSub = leftSubKeys[i-1]
        prevRSub = rightSubKeys[i-1]
        if i==1 or i==8 or i==15:           # for rounds 2,9,16  shift left one  esle shift 2 
            leftSubKeys.append(prevLSub[1:]+ prevLSub[0])
            rightSubKeys.append(prevRSub[1:]+ prevRSub[0])
        else: 
            leftSubKeys.append(prevLSub[2:]+ prevLSub[:2])
            rightSubKeys.append(prevRSub[2:]+ prevRSub[:2])

    # to here, i have 32 subkeys  // 16 for left and 16 for right
    # apply concatenation step // take 16 of 2 subkeys return 16 keys  * each key is 56 bits
    concatenatedKeys =[]
    # print("printing rounds:\n")
    for i in range(16):
        # print("round",i+1," :", (leftSubKeys[i]+rightSubKeys[i])) 
        concatenatedKeys.append(leftSubKeys[i]+rightSubKeys[i])
    return concatenatedKeys
    

def permutateManyKeys(concatenatedKeys):    # take list of concatenated keys(16) and pc2 table and return perm 16 keys
    permutatedKeys = []
    
    pc2= [14,    17,   11,    24,     1,    5,    3,    28,
     15,     6,    21,   10,      23,  19,   12,     4,
     26,    8,    16,     7,   27,    20,    13,    2,
     41,    52,   31,    37,    47,   55,    30,    40,   
     51,    45,    33,   48,    44,    49,   39,    56, 
     34,   53,      46,    42,   50,    36,    29,   32]
    
    for i in range(16):  # loop on 16 keys 
        permRes= permutateAny(concatenatedKeys[i],pc2)
        permutatedKeys.append(permRes)
    return permutatedKeys  # return 
    

def generateKeys():  # all gen key algo.    and return list of 16 keys
    initKey = setKeyRet()  # get key from user 
    key_inBtis = getInitKey_in_bits(initKey)  # convert key to bits
     # permutate1
    pc1=[57, 49, 41, 33, 25, 17, 9, 1,
     58, 50, 42, 34 ,26, 18, 10, 2,
     59, 51, 43, 35, 27, 19, 11, 3,
     60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4]

    perm1Result = permutateAny(key_inBtis,pc1)
    # divide one key into 2 subkeys, apply rounds and concatenated res 
    concResult = divideApplyRoundsConc(perm1Result)
    perm2Res = permutateManyKeys(concResult)   # apply permutation2 on the 16 keys 
    return perm2Res
