import hashlib
import time

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
   print ("Initial string " + str1)
   new = int(str1,  16)
   print ("Int String " + str(new))
   mask = convertTrun(trun)
   print ("mask " + str(mask) + " " + str(trun))
   val = new & mask
   print ("And'ed val: " + str(val))
   return val

# Takes two input strings and counts the number of identical characters at the same location
def findSame(str1, str2):
   print (str1)
   print (str2)
   lst2 = []
   if(len(str1) != len(str2)):
      err = "Error: String length's differ:\n" + "\tstr1:" + str1 + "\n\tstr2:" + str2
      return err
   for i in range(0,int(len(str1)/2)):
      if str1[i*2] == str2[i*2]:
         if str1[i*2+1] == str2[i*2+1]:
            print ("Bytes in common:" + str1[i*2] + str1[i*2+1])
            lst2.append(str1[i])
   print ("Number of bytes in common:" + str(len(lst2)) + "\n")
   return len(lst2)


def hashString(str1):
   val1 = hashlib.sha256(str1.encode('UTF-8')).hexdigest()
   return val1

def hamming():
   print ("Same chars for password and pbssword")
   val1 = hashString("password")
   val2 = hashString("pbssword")
   findSame(val1, val2)

   print ("Same chars for 0 and 1")
   val1 = hashString("0")
   val2 = hashString("1")
   findSame(val1, val2)

   print ("Same chars for 00 and 01")
   val1 = hashString("00")
   val2 = hashString("01")
   findSame(val1, val2)

   print ("Same chars for 10 and 11")
   val1 = hashString("10")
   val2 = hashString("11")
   findSame(val1, val2)

   print ("Same chars for 329 and 292")
   in1 = 329
   in2 = 292
   val1 = hashString(str(in1))
   val2 = hashString(str(in2))
   findSame(val1, val2)
   digestSize = 18
   hashVal1 = truncate(hashString(str(in1)), int(digestSize))
   hashVal2 = truncate(hashString(str(in2)), int(digestSize))
   print (hashVal1, hashVal2)


def main():
   hamming()

if __name__== "__main__":
   main()
