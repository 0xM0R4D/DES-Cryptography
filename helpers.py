from keyGen import permutateAny

#### this file contains functions used for encryption and decryption *without permutateAny


def expandFunc(Ri): # ri is 32 bits and expandbox table of 48 elements
    EBox_table = [
            32,1,2,3,4,5,
            4,5,6,7,8,9,
            8,9,10,11,12,13,
            12,13,14,15,16,17,
            16,17,18,19,20,21,
            20,21,22,23,24,25,
            24,25,26,27,28,29,
            28,29,30,31,32,1]
    expandRes = ""
    
    for i in range( len(EBox_table)):
        expandRes += str(Ri[EBox_table[i]-1])
    
    return expandRes




# print("before e
# xpanding: ", Ri_test)
# print("after: ", expand(Ri_test))

def xoring(Ri,kj):    #  j = i+1    // take any length and used in general 
    ret = [] 
    itrLen = len(Ri)
    for i in range(itrLen):
        if (Ri[i]=='0' and kj[i] == '0') or (Ri[i]=='1' and kj[i] == '1'): 
            ret.append('0')
        else: 
            ret.append('1')
    ret = ''.join(ret)
    return ret 


# print("after expanding: ", expand(Ri_test))
# print("key:             ", kj_test)
# exp=expand(Ri_test)
# print("after xoring:    ",xoring(exp, kj_test))

def applySBoxes(xoringRes): #   take xoring res(48 bits) return 32 bits
    s1 = [ [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
		   [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
		   [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		   [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13] ]
    
    s2= [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
		 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
		 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9] ]

    s3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], 
		  [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		  [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		  [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]  ]

    s4 = [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		   [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		   [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		   [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

    s5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

    s6 =[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ]

    s7 =[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

    s8 =[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
		 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
	
    # get part, get row, col in s box*as00,1111 then convert this str to bin then to desimal
    sboxesRes = []
    for i in range(0,48,6): 
        cut= xoringRes[i:i+6]        # ex: 110111  *str
        row=cut[0]+cut[5] # 11
        col=cut[1:5]  # 1011
        colIdx = int(col,2)
        rowIdx = int(row,2)

        val = 0 
        if i ==0: # s1 
            val = s1[rowIdx][colIdx]  # get val // ex: 4 
        elif i ==6: 
            val = s2[rowIdx][colIdx]
        elif i ==12: 
            val = s3[rowIdx][colIdx]
        elif i ==18: 
            val = s4[rowIdx][colIdx]
        elif i ==24: 
            val = s5[rowIdx][colIdx]
        elif i ==30: 
            val = s6[rowIdx][colIdx]
        elif i ==36: 
            val = s7[rowIdx][colIdx]

        elif i ==42: 
            val = s8[rowIdx][colIdx]
        else: 
            break


        binVal = bin(val)[2:]
        binVal = binVal.zfill(4)  #  in 4 bit representation
        binStr = str(binVal)
        sboxesRes.append(binStr)
    sboxesRes = ''.join(sboxesRes)    # convert to string 

    return sboxesRes
            
# xoringRes =xoring(exp, kj_test)            
# sbx = applySBoxes(xoringRes)
# print("after sboixing  :  ",  sbx)

p_mang =  [16, 7, 20, 21, 29, 12, 28, 17,        # 32 len 
              1, 15, 23, 26, 5, 18, 31, 10,
              2, 8, 24, 14, 32, 27, 3, 9,
              19, 13, 30, 6, 22, 11, 4, 25 ]



# pe=permutateAny(sbx, p_box)
# print("perm res:          ",pe )

# print("test permFun.:     ", permutateAny(sbx,testP))   # ok , use it in next

initP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

finalP = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

def mangularFunc(ri,kj):
    expRes = expandFunc(ri)
    xorRes = xoring(expRes,kj)
    sboxsRes = applySBoxes(xorRes)
    permRes  = permutateAny(sboxsRes,p_mang)
    return permRes


#### functions used