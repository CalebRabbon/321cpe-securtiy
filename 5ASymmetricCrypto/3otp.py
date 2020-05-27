import string
import random

# Converts an integer list to a single string
def convertIntLstToString(lst):
   newlst = []
   for i in lst:
      char = chr(i)
      newlst.append(char)
   return "".join(newlst)

# Takes two strings and XOR's them if they are the same length
# If different length it throws an error
def xor(str1, str2):
   if(len(str1) != len(str2)):
      err = "Error: String length's differ:\n" + "\tstr1:" + str1 + "\n\tstr2:" + str2
      return err
   datalist = [(ord(a) ^ ord(b)) for a,b in zip(str1,str2)]
   return convertIntLstToString(datalist)

# Creates a random string of given length
def createRanString(length):
   lst = []
   for i in range(0, length):
      ran = createRandomByte()
      char = convertByteToChar(ran)
      lst.append(char)
   return "".join(lst)

# Converts a byte to a character
def convertByteToChar(val):
   return chr(val)

# Creates a random byte by creating a random number between 0 and 255
def createRandomByte():
   value = random.randint(0,255)

   return value

def main():
   # Open a file
   ofile = open("./cp-logo.bmp", "r")
   efile = open("encrypt.txt", "w+")
   dfile = open("decrypt.txt", "w+")

   # Read the files originalText
   if ofile.mode == "r":
      originalText = ofile.read()

   print ("Original Text:\n")
   #print originalText

   ranString = createRanString(len(originalText))
   encrypt = xor(originalText,ranString)

   print ("Encrypted Text:\n")
  # print encrypt
   efile.write(encrypt)

   decrypt = xor(encrypt, ranString)
   print ("\nDecrypted Text:\n")
  # print decrypt
   dfile.write(decrypt)

if __name__== "__main__":
   main()
