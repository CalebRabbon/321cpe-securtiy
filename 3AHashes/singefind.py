import bcrypt
import time
from nltk.corpus import words

# Run this with a designateed hash name to find the time it takes to find the original plain text word
# This is slow it took an hour to find the hBilbo password which is welcome

def checkpw(str1, hashval):
   if bcrypt.checkpw(str1, hashval):
      print(" Found password:")
      print (str1)

def main():

   hBilbo = "$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq"
   hGandalf = "$2b$08$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC"
   hThorin = "2b$08$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q"
   hFili = "2b$09$M9xNRFBDn0pUkPKIVCSBzuwNDDNTMWlvn7lezPr8IwVUsJbys3YZm"
   hKili = "2b$09$M9xNRFBDn0pUkPKIVCSBzuPD2bsU1q8yZPlgSdQXIBILSMCbdE4Im"
   hBalin = "2b$10$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom"
   hDwalin = "2b$10$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be"
   hOin = "2b$10$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK"
   hGloin = "2b$11$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q"
   hDori = "2b$11$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq"
   hNori = "2b$11$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12"
   hOri = "2b$12$rMeWZtAVcGHLEiDNeKCz8OiERmh0dh8AiNcf7ON3O3P0GWTABKh0O"
   hBifur = "2b$12$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK"
   hBofur = "2b$12$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O"
   hDurin = "2b$13$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay"

   str1 = b"Secrity"
   hashed8 = "$2b$08$qks9sFC3VR/KKNo0qpHxsOezEbuqk5mS40LW7P0Q5PoRm1gc6VnNe"
   #hashed8 = bcrypt.hashpw(str1, bcrypt.gensalt(rounds=8))
   hashed9 = bcrypt.hashpw(str1, bcrypt.gensalt(rounds=9))
   print (hashed8)

   start = time.time()
   checkpw(str1,hashed8)
   end = time.time()
   elapsed = end - start
   print ("Round 8 Time")
   print (elapsed)

   start = time.time()
   checkpw(str1,hashed9)
   end = time.time()
   elapsed = end - start
   print ("Round 9 Time")
   print (elapsed)

   wlist = words.words()
   print (len(wlist))
   some = 0

   start = time.time()
   for word in wlist:
      if(len(word) < 11):
         if(len(word) > 5):
            some += 1
            #checkpw(word.encode('utf-8'),hBilbo)

   print (" some " + str(some))
   end = time.time()
   elapsed = end - start
   print ("Total Time to Crack Password")
   print (elapsed)


if __name__== "__main__":
   main()
