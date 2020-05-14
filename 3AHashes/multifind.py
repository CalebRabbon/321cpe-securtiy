import bcrypt
import time
import sys
from nltk.corpus import words

# Takes an input User to solve the password for, then a range for which parts of the nltk word list to search
# Example python multifind.py Bilbo 0 1000

arg = sys.argv

def checkpw(str1, hashval):
   if bcrypt.checkpw(str1, hashval):
      print(" Found password:" + (str1))
      return 1
   return 0

def crackpw(hashval, indStart, indEnd):
   wlist = words.words()
   val = 0

   start = time.time()
   for word in wlist[int(indStart):int(indEnd)]:
      if(len(word) < 11):
         if(len(word) > 5):
            val = checkpw(word.encode('utf-8'),hashval)
      if val == 1:
         break

   end = time.time()
   elapsed = end - start

   if val == 0:
      print ("Didn't find Password:")
   print ("Result " + str(arg[2]) + " - " + str(arg[3]) + " Total time elapsed:")
   print (elapsed)


def findHash(user):
   if user == "Bilbo":
      print ("This is Bilbo")
      return "$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq"
   elif user == "Gandalf":
      print ("This is Gandalf")
      return "$2b$08$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC"
   elif user == "Thorin":
      print ("This is Thorin")
      return "2b$08$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q"
   elif user == "Fili":
      print ("This is Fili")
      return "2b$09$M9xNRFBDn0pUkPKIVCSBzuwNDDNTMWlvn7lezPr8IwVUsJbys3YZm"
   elif user == "Kili":
      print ("This is Kili")
      return "2b$09$M9xNRFBDn0pUkPKIVCSBzuPD2bsU1q8yZPlgSdQXIBILSMCbdE4Im"
   elif user == "Balin":
      print ("This is Balin")
      return "2b$10$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom"
   elif user == "Dwalin":
      print ("This is Dwalin")
      return "2b$10$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be"
   elif user == "Oin":
      print ("This is Oin")
      return "2b$10$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK"
   elif user == "Gloin":
      print ("This is Gloin")
      return "2b$11$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q"
   elif user == "Dori":
      print ("This is Dori")
      return "2b$11$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq"
   elif user == "Nori":
      print ("This is Nori")
      return "2b$11$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12"
   elif user == "Ori":
      print ("This is Ori")
      return "2b$12$rMeWZtAVcGHLEiDNeKCz8OiERmh0dh8AiNcf7ON3O3P0GWTABKh0O"
   elif user == "Bifur":
      print ("This is Bifur")
      return "2b$12$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK"
   elif user == "Bofur":
      print ("This is Bofur")
      return "2b$12$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O"
   elif user == "Durin":
      print ("This is Durin")
      return "2b$13$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay"
   else:
      sys.exit()

def main():

   hashval = findHash(arg[1])
   print ("Starting from " + str(arg[2]) + " to " + str(arg[3]))
   crackpw(hashval, arg[2], arg[3])

if __name__== "__main__":
   main()
