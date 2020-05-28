# Encrypts a .bmp file with Cypher block chaining encryption

from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
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

def pad(data):
   data = "12345678901234567"
   length = len(data)

   # Check to see if you don't need to pad
   if(length % 16 == 0):
      return data

   # Each block of data is 16 bytes. To get the remaining pad bytes the below equation is used
   padBytes = 16 - (length % 16)
   for i in range(0, padBytes):
      data = data + chr(padBytes)
   return data

def main():
   # Open a file
   #ofile = open("./cp-logo.bmp", "r")
   ofile = open("./mustang.bmp", "r")
   o2file = open("./cp-logo.bmp", "r")
   cp = open("encryptCP.bmp", "w")
   out = open("out.txt", "w")
   must = open("encryptMust.bmp", "w")
   combine = open("combine.bmp", "w")

   # Read the files originalText
   if ofile.mode == "r":
      originalText = ofile.read()

   originalHeader = originalText[0:54]
   data = originalText[54:]

   # Padding the string
   data = pad(data)
#   print (data)
   #out.write(data)

#   # Encryption of the string
   key = get_random_bytes(16)
   out.write(key)
   cipher = AES.new(key, AES.MODE_CBC)
   encrypt = cipher.encrypt(data)
   cp.write(originalHeader)
   cp.write(encrypt)

#   cp.write(originalHeader)
#   cp.write(encrypt)
#
#   # Read the files originalText2
#   if o2file.mode == "r":
#      originalText2 = o2file.read()
#
#   originalHeader2 = originalText2[0:54]
#   data2 = originalText2[54:]
#
#   encrypt2 = xor(data2,ranString)
#
#   must.write(originalHeader2)
#   must.write(encrypt2)
#
#   # XORING the two encrypted files
#   combine.write(originalHeader)
#   combineEncrypt = xor(encrypt, encrypt2)
#   combine.write(combineEncrypt)
#
if __name__== "__main__":
   main()