import string
from collections import OrderedDict

def main():
    # Open a file
    efile = open("./encrypted/mono_easy_encrypt.txt", "r")
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

 #   print ("Frequency:\n" + str(freq))

 #   sorted(freq)

 #   print(sorted(freq.values()))
    sortedfreq = (sorted(freq.items(), key = lambda kv:(kv[1], kv[0])))
    print(sortedfreq)

    d = OrderedDict()
    d = {'E':'', 'T':'', 'A':'', 'O':'', 'I':'', 'N':'', 'S':'', 'R':'', 'H':'',
        'L':'', 'D':'', 'C':'', 'U':'', 'M':'', 'F':'', 'P':'', 'G':'',
        'W':'', 'Y':'', 'B':'', 'V':'', 'K':'', 'X':'', 'J':'', 'Q':'', 'Z':''}

    commonletterfreq = {'E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D',
        'C', 'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'J',
        'Q', 'Z'}

#    print "trying"
#    for i,j in zip(d, commonletterfreq):
#        d[i] = j
#        print i, d[i], j
    print commonletterfreq
    print "take"
    for i in commonletterfreq:
        print i

    d['E'] = 'B'
    print d['E']


    sortedfreq.reverse()
    for i in sortedfreq:
        key = i[0]
        value = i[1]
        upper_letter = ord(key) in range (65, 91)
        if upper_letter:
            print key, value, upper_letter, ord(key)


    #for i in freq.reveerse():
    #    print i

 #   for i in sorted(freq.items()):
 #       print (i)


    # Read the files contents
    dfile = open("decrypted.txt", "r")
    if dfile.mode == "r":
        contents = dfile.read()
        print(contents)

if __name__== "__main__":
    main()
