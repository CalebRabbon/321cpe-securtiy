# Used for Task II to for the oracle functions

import urllib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import string

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

def pad(data):
   length = len(data)
   # Each block of data is 16 bytes. To get the remaining pad bytes the below equation is used
   padBytes = 16 - (length % 16)
   for i in range(0, padBytes):
      data = data + chr(padBytes)
   return data

def encryptData(data, key, iv):
   cipher = AES.new(key, AES.MODE_ECB)

   length = len(data)

   # 16 bytes in a block. And length is given in bytes
   numBlocks = length / 16

   # initializing variables
   totalEncrypt = ""
   message = ""
   xormessage = ""

   # Encrypt with CBC
   for i in range(0, numBlocks):
      message = data[i*16: i*16 + 16]
      xormessage = xor(iv, message)
      encryptMessage = cipher.encrypt(xormessage)
      totalEncrypt += encryptMessage
      iv = encryptMessage
   return totalEncrypt

def decryptData(data, key, iv):
   cipher = AES.new(key, AES.MODE_ECB)

   length = len(data)

   # 16 bytes in a block. And length is given in bytes
   numBlocks = length / 16

   # initializing variables
   totalDecrypt = ""
   message = ""
   xormessage = ""

   # Decrypt with CBC
   for i in range(0, numBlocks):
      message = data[i*16: i*16 + 16]
      decryptMessage = cipher.decrypt(message)
      xormessage = xor(iv, decryptMessage)
      totalDecrypt += xormessage
      iv = message
   return totalDecrypt

def submit(string, key, iv):
   newStr = ""
   for c in string:
      if (c == ";"):
         newStr += "%3B"
      elif (c == "="):
         newStr += "%3D"
      else:
         newStr += c

   newStr = "userid=456;userdata=" + newStr + ";session-id=31337"
   newStr = pad(newStr)
   newStr = encryptData(newStr, key, iv)
   return newStr

# Returns true or false if the input string has the string ";admin=true;"
def findAdmin(decrypt):
   result = decrypt.find(";admin=true;")

   if (result == -1):
      return False
   return True

# Decrypts the input string with CBC
# Returns true or false if the input string has the string ";admin=true;"
def verify(string, key, iv):
   decrypt = ""
   decrypt = decryptData(string, key, iv)
   cp = open("decryptMessage.txt", "w")
   cp.write(decrypt)
   print(decrypt)
   return findAdmin(decrypt)

# Takes in a string which is the ciphertext
# Takes in an int representing the byte to modify
# Takes in a character which will change the byte to that value
# Note: You must enter a byte value 16 or greater becuase to change the byte you must
#       modify the byte that is 16 spaces below it
#       Bytes are 0 indexed so putting a 16 for byteNum will alter the 17th byte in cipher text
def setbyte(ciphertext, char, byteNum, key, iv):
   # decrypt the data to get the correct ending term
   decrypt = ""
   decrypt = decryptData(ciphertext, key, iv)

   binaryChar = ord(char)

   # currentByte is the byte that will ultimately be changed in the decrypting
   currentByte = decrypt[byteNum:byteNum + 1]
   print ("current byte " + currentByte)

   # changeByte is the byte 16 spaces below the currentByte which will be changed such that currentByte can ultimately be changed in the decrypting
   changeByte = ciphertext[byteNum - 16:byteNum - 15]
   print ("changebyte " + changeByte)

   xormask = binaryChar ^ ord(currentByte)
   print ("xormask " + chr(xormask))

   flipbyte = int(xormask) + ord(changeByte)

   # truncate the flipbyte
   flipbyte &= 0b11111111
   print (flipbyte)

   newString = ""
   #print (ciphertext[0:byteNum - 16])
  # print chr(flipbyte)
  # print (ciphertext[byteNum + 1:])
   newString += ciphertext[0:byteNum - 16] + chr(flipbyte) + ciphertext[byteNum - 15:]
   #print newString
   return newString

   #print (binaryChar)
#   newString = chr(int('11011111',2))
#   newString += string[1:]
#   return newString

def main():
   # Open a file
   key = get_random_bytes(16)
   iv = get_random_bytes(16)
   encryData = ""
   newEncry = ""
   string = ""
   decryData = ""
   data = "You're the man now, dog"

   encryData = submit(data, key, iv)
   cp = open("encryptMessage.txt", "w")
   cp.write("XXXXXX")
   cp.write(encryData)
   newEncry = setbyte(encryData, ';', 16, key, iv)
   #encryData = setbyte(encryData, ';', 17)
   cp.write("XXXXXX")
   cp.write(newEncry)
#
   decryData = verify(newEncry, key, iv)
   print(decryData)
#
#   data = ""
#   data = encryptData("00000000000100000", key, iv)
#   print(data)
#   print(decryptData(data, key, iv))
#
#
#   cp = open("hi", "w")
#   cp.write(s)

#   ofile = open("./mustang.bmp", "r")
#   cp = open("cbcencryptMust.bmp", "w")
#
#   # Read the files originalText
#   if ofile.mode == "r":
#      originalText = ofile.read()
#
#   originalHeader = originalText[0:54]
#   data = originalText[54:]
#
#   # Padding the string
#   data = pad(data)
#
#   # Encryption of the string
#   encrypt = encryptData(data)
#   cp.write(originalHeader)
#   cp.write(encrypt)

if __name__== "__main__":
   main()
