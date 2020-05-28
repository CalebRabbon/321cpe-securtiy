# Encrypts a .bmp file with Cypher block chaining encryption

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import string

def pad(data):
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
   ofile = open("./mustang.bmp", "r")
   cp = open("encryptMust.bmp", "w")

   # Read the files originalText
   if ofile.mode == "r":
      originalText = ofile.read()

   originalHeader = originalText[0:54]
   data = originalText[54:]

   # Padding the string
   data = pad(data)

   # Encryption of the string
   key = get_random_bytes(16)
   cipher = AES.new(key, AES.MODE_CBC)
   encrypt = cipher.encrypt(data)
   cp.write(originalHeader)
   cp.write(encrypt)

if __name__== "__main__":
   main()
