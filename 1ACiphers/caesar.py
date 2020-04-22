import string

def main():
   # Open a file
   efile = open("./encrypted/vigerene_easy_encrypted.txt", "r")
   dfile = open("decrypted.txt", "w+")

   # Read the files contents
   if efile.mode == "r":
      contents = efile.read()
      print(contents)

   efile.close()

   # Loops through each possible cipher
   for i in range(0, 26):
      dfile.write("\nUsing the key %s\n" % i)
      # Attempting a single Caesar Cipher key
      for c in contents:
         # Checking to make sure I am only shifting the ASCII characters
         lower_letter = ord(c) in range (97, 123)
         upper_letter = ord(c) in range (65, 91)
         if lower_letter:
            # Shift letter by i, 97 is the ASCII value for a
            #    We subtract out 97 then add it back in to get the ASCII value
            # Using 0 index: a = 0, b = 1... z = 25
            # Mod by 26 so a value greater than 25 will revert back to 0
            # Subtracting out i to decrypt the message
            dfile.write(chr(((ord(c) - 97 - i) % 26) + 97))
         elif upper_letter:
            # Shift letter by i, 65 is the ASCII value for a
            dfile.write(chr(((ord(c) - 65 - i) % 26) + 65))
         else:
            dfile.write(c)

   # Read the files contents
   dfile = open("decrypted.txt", "r")
   if dfile.mode == "r":
      contents = dfile.read()
      print(contents)

if __name__== "__main__":
   main()
