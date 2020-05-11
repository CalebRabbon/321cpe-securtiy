import hashlib
import time

# Takes two input strings and counts the number of identical characters at the same location
def findSame(str1, str2):
   print ("Same chars for " + str1 + " and " + str2)
   lst2 = []
   if(len(str1) != len(str2)):
      err = "Error: String length's differ:\n" + "\tstr1:" + str1 + "\n\tstr2:" + str2
      return err
   for i in range(0,len(str1)/2):
      if str1[i*2] == str2[i*2]:
         if str1[i*2+1] == str2[i*2+1]:
            print ("Bytes in common:" + str1[i*2] + str1[i*2+1])
            lst2.append(str1[i])
   print ("Number of bytes in common:" + str(len(lst2)) + "\n")
   return len(lst2)


def hashString(str1):
   val1 = hashlib.sha256(str1.encode('UTF-8')).hexdigest()
   return val1

# Converts the trun value to an integer to be used as a mask
# The trun value of 8 would return 255 since this is 11111111 in binary
def convertTrun(trun):
   val = 1

   # Gets finds 2^trun
   for i in range(0, trun):
      val *= 2

   # Subtract 1 to get the mask
   val -= 1
   return val

# Truncates the string and takes the last trun bits
# Returns just the last bits as an integer
# The string is 256 bits and the trun can be 8 up to 50 bits
def truncate(str1, trun):
   new = int(str1,  16)
   mask = convertTrun(trun)
   val = new & mask
   return val

# Returns an int representing if the value was found in the dictionary
# 1 = The value was found
# 0 = The value was not found
def addToDict(d, val):
   found = d.get(val,0)

   if found == 1:
      #print "Found the value"
      return 1
   else:
      #print "not found"
      d[val] = 1
      return 0
   return 0

def hamming():
   val1 = hashString("password")
   val2 = hashString("pbssword")
   findSame(val1, val2)

   val1 = hashString("0")
   val2 = hashString("1")
   findSame(val1, val2)

   val1 = hashString("00")
   val2 = hashString("01")
   findSame(val1, val2)

   val1 = hashString("10")
   val2 = hashString("11")
   findSame(val1, val2)

# Finds the collision give a digest size. The lower the digest size the faster a collision will occur
def findCollision(digestSize):
   # Birthday dictionary
   bdd = {}

   val = 1

   hashVal = truncate(hashString(str(val)), digestSize)

   print (hashVal)

   start = time.time()
   while addToDict(bdd, hashVal) != 1:
      #print bdd
      val += 1
      hashVal = truncate(hashString(str(val)), int(digestSize))
      print (hashVal)
   #print "digest Size " + str(digestSize)
   end = time.time()
   duration = end - start
   #print str(duration) # + " seconds"

def main():
   findCollision(18)

#   val = 329
#   digestSize = 18
#   hashVal = truncate(hashString(str(val)), int(digestSize))
#   print hashVal
#
#   digestSize = 20
#   hashVal = truncate(hashString(str(val)), int(digestSize))
#   print hashVal
#
#   digestSize = 22
#   hashVal = truncate(hashString(str(val)), int(digestSize))
#   print hashVal

if __name__== "__main__":
   main()
