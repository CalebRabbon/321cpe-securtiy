import string
from collections import OrderedDict

def main():
    # Open a file
    efile = open("./encrypted/found1.txt", "r")
    #efile = open("./test.txt", "r")
    dfile = open("decrypted.txt", "w+")

    # Read the files contents
    if efile.mode == "r":
        contents = efile.read()
        print(contents)

    efile.close()

    freq = {}

    for i in contents:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    sortedfreq = (sorted(freq.items(), key = lambda kv:(kv[1], kv[0])))
#    print(sortedfreq)

    sortedfreq.reverse()
    for i in sortedfreq:
        key = i[0]
        value = i[1]
        upper_letter = ord(key) in range (65, 91)
        if upper_letter:
            print key, value

if __name__== "__main__":
    main()
