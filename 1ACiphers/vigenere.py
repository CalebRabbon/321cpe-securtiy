import string
import math

def chiVal(E,A):
    return ((E-A)*(E-A)) / E

# Takes a Key and the Actual Array of encrypted frequencies
def chi2(key, A = []):
    # Expected frequencies for normal English
    E = [08.47     # a
        ,01.492    # b
        ,02.202    # c
        ,04.253    # d
        ,11.162    # e
        ,02.228    # f
        ,02.015    # g
        ,06.094    # h
        ,07.546    # i
        ,00.153    # j
        ,01.292    # k
        ,04.025    # l
        ,02.406    # m
        ,06.749    # n
        ,07.507    # o
        ,01.929    # p
        ,00.095    # q
        ,07.587    # r
        ,06.327    # s
        ,09.356    # t
        ,02.758    # u
        ,00.978    # v
        ,02.560    # w
        ,00.150    # x
        ,01.994    # y
        ,00.077]   # z

    chi2 = (chiVal(E[0],A[(0 + key) % 26])
         + chiVal(E[1],A[(1 + key) % 26])
         + chiVal(E[2],A[(2 + key) % 26])
         + chiVal(E[2],A[(2 + key) % 26])
         + chiVal(E[3],A[(3 + key) % 26])
         + chiVal(E[4],A[(4 + key) % 26])
         + chiVal(E[5],A[(5 + key) % 26])
         + chiVal(E[6],A[(6 + key) % 26])
         + chiVal(E[7],A[(7 + key) % 26])
         + chiVal(E[8],A[(8 + key) % 26])
         + chiVal(E[9],A[(9 + key) % 26])
         + chiVal(E[10],A[(10 + key) % 26])
         + chiVal(E[11],A[(11 + key) % 26])
         + chiVal(E[12],A[(12 + key) % 26])
         + chiVal(E[13],A[(13 + key) % 26])
         + chiVal(E[14],A[(14 + key) % 26])
         + chiVal(E[15],A[(15 + key) % 26])
         + chiVal(E[16],A[(16 + key) % 26])
         + chiVal(E[17],A[(17 + key) % 26])
         + chiVal(E[18],A[(18 + key) % 26])
         + chiVal(E[19],A[(19 + key) % 26])
         + chiVal(E[20],A[(20 + key) % 26])
         + chiVal(E[21],A[(21 + key) % 26])
         + chiVal(E[22],A[(22 + key) % 26])
         + chiVal(E[23],A[(23 + key) % 26])
         + chiVal(E[24],A[(24 + key) % 26])
         + chiVal(E[25],A[(25 + key) % 26]))

    return chi2

# Takes in the contents, initial offset, and word length
# Returns a list of frequencies in alphabetical order
def findFreq(contents, num, wordLength):
    # Frequency Dictionary
    freqD = {}

    # Blank Frequency Array
    freqA = [0] * 26

    # CreateDictionary
    for i in contents[num::wordLength]:
        print i,
        if i in freqD:
            freqD[i] += 1
        else:
            freqD[i] = 1

    sortedfreq = (sorted(freqD.items(), key = lambda kv:(kv[0], kv[1])))
    #print sortedfreq

    # create the freqA
    for i in sortedfreq:
        key = i[0]
        value = i[1]
        lower_letter = ord(key) in range (97, 123)
        if lower_letter:
            if key == 'a':
                freqA[0] = value
            elif key == 'b':
                freqA[1] = value
            elif key == 'c':
                freqA[2] = value
            elif key == 'd':
                freqA[3] = value
            elif key == 'e':
                freqA[4] = value
            elif key == 'f':
                freqA[5] = value
            elif key == 'g':
                freqA[6] = value
            elif key == 'h':
                freqA[7] = value
            elif key == 'i':
                freqA[8] = value
            elif key == 'j':
                freqA[9] = value
            elif key == 'k':
                freqA[10] = value
            elif key == 'l':
                freqA[11] = value
            elif key == 'm':
                freqA[12] = value
            elif key == 'n':
                freqA[13] = value
            elif key == 'o':
                freqA[14] = value
            elif key == 'p':
                freqA[15] = value
            elif key == 'q':
                freqA[16] = value
            elif key == 'r':
                freqA[17] = value
            elif key == 's':
                freqA[18] = value
            elif key == 't':
                freqA[19] = value
            elif key == 'u':
                freqA[20] = value
            elif key == 'v':
                freqA[21] = value
            elif key == 'w':
                freqA[22] = value
            elif key == 'x':
                freqA[23] = value
            elif key == 'y':
                freqA[24] = value
            elif key == 'z':
                freqA[25] = value
            #print key, value

#    print freqA
#    print len(freqA)
    print sum(freqA)
    total = sum(freqA) + 1.0
    freqPer = []
    # Create the frequency percentages
    for i in freqA[0:26]:
        freqPer.append(100*i/total)
    print freqPer
    return freqPer

# Takes in the contents (contents), initial offset (num), and word length (word)
# Returns the minimum chi2 valued and the key associated with it
def findMinChi(contents, num, word):
    freq = findFreq(contents, num, word)

    # Creating a chi2Array of all possible chi2 values
    chi2Array = [0] * 26
    for i in range(0, 26):
        chi2Array[i] = chi2(i, freq)
        print ("Key %s:   chi2:  %s" % (i, chi2Array[i]))

    # Find the minimum chi2 value and key
    key = 0
    minimum = chi2Array[0]
    for i in range(1, 26):
        if chi2Array[i] < minimum:
            print ("Key %s:   chi2:  %s" % (i, chi2Array[i]))
            print chi2Array[i]
            minimum = chi2Array[i]
            key = i
    return minimum, key

def decrypt(contents, keys, wordlength):
    print contents
    dfile = open("decrypted.txt", "w+")

#    count = 0
#    for i in range(0, len(contents)):
#        if count == 0:
#            contents[i] = chr(((ord(contents[i]) - 97 - keys[0]) % 26) + 97)
#        elif count == 1:
#            contents[i] = chr(((ord(contents[i]) - 97 - keys[1]) % 26) + 97)
#        elif count == 2:
#            contents[i] = chr(((ord(contents[i]) - 97 - keys[2]) % 26) + 97)
#        elif count == 3:
#            contents[i] = chr(((ord(contents[i]) - 97 - keys[3]) % 26) + 97)
#        elif count == 4:
#            contents[i] = chr(((ord(contents[i]) - 97 - keys[4]) % 26) + 97)
#        print contents[i], i,
#        count += 1
#        if count == 5:
#            count = 0
#
    list(contents)
    for index in range(0,5):
        print keys[index]
        print index
        for char in contents[index::wordlength]:
            char = chr(((ord(char) - 97 - keys[index]) % 26) + 97)
            print char,

    # Read the files contents
    dfile = open("decrypted.txt", "r")
    if dfile.mode == "r":
        contents = dfile.read()
        print(contents)

def main():
    # Open a file
    efile = open("./encrypted/vigerene_easy_encrypted.txt", "r")
    #efile = open("./encrypted/v.txt", "r")
    dfile = open("decrypted.txt", "w+")

    # Read the files contents
    if efile.mode == "r":
        contents = efile.read()
        print(contents)


    keys = [0] * 5

    minimum, index = findMinChi(contents, 0, 5)
    print ("1 Key %s" % index)
    keys[0] = index
    minimum, index = findMinChi(contents, 1, 5)
    print ("2 Key %s" % index)
    keys[1] = index
    minimum, index = findMinChi(contents, 2, 5)
    print ("3 Key %s" % index)
    keys[2] = index
    minimum, index = findMinChi(contents, 3, 5)
    print ("4 Key %s" % index)
    keys[3] = index
    minimum, index = findMinChi(contents, 4, 5)
    print ("5 Key %s" % index)
    keys[4] = index

    decrypt(contents, keys, 5)

    efile.close()

if __name__== "__main__":
    main()
