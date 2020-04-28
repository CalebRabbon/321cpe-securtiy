import string

# Converts a list of integer to hex values and returns a single string representing thos hex values
def convertStrListHex(lst):
   # Removes the leading convertes the integers to hex values without the leading 0x
   # 0 means to add 0 if empty space
   # >2 Means to right align
   # x means to make in hex format
   # Citation for the below line of code: https://stackoverflow.com/questions/58114383/how-to-remove-0x-in-hex-and-get-2-digits
   lst2 = ["{:0>2x}".format(i) for i in lst]
   return "".join(lst2)

# Takes two strings and XOR's them if they are the same length
# If different length it throws an error
def xor(str1, str2):
   if(len(str1) != len(str2)):
      err = "Error: String length's differ:\n" + "\tstr1:" + str1 + "\n\tstr2:" + str2
      return err
   datalist = [(ord(a) ^ ord(b)) for a,b in zip(str1,str2)]
   return convertStrListHex(datalist)

def main():
   print xor("Darlin dont you go","and cut your hair!")
   print xor("aDarlin dont you go","and cut your hair!")

if __name__== "__main__":
   main()
