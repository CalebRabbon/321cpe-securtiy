import string

def main():
   # Open a file
   #efile = open("./encrypted/caesar_easy_encrypted.txt", "r")
   efile = open("./test.txt", "r")
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

   print ("Frequency:\n" + str(freq))

   # Read the files contents
   dfile = open("decrypted.txt", "r")
   if dfile.mode == "r":
      contents = dfile.read()
      print(contents)

if __name__== "__main__":
   main()
