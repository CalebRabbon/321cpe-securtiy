#! /bin/bash

if [$1 == ""];then
   printf "Please enter a name for which password to solve\n"
   printf "   Example: .\solve Bilbo\n"
   printf "   Example: .\solve Gandalf\n"
   printf "   Example: .\solve Thorin\n"
   printf "   Example: .\solve Fili\n"
   printf "   Example: .\solve Kili\n"
   printf "   Example: .\solve Balin\n"
   printf "   Example: .\solve Dwalin\n"
   printf "   Example: .\solve Oin\n"
   printf "   Example: .\solve Gloin\n"
   printf "   Example: .\solve Dori\n"
   printf "   Example: .\solve Nori\n"
   printf "   Example: .\solve Ori\n"
   printf "   Example: .\solve Bifur\n"
   printf "   Example: .\solve Bofur\n"
   printf "   Example: .\solve Durin\n"
   exit
fi



python multifind.py $1 0 23674 &
python multifind.py $1 23674 47347 &
python multifind.py $1 47347 71021 &
python multifind.py $1 71021 94694 &
python multifind.py $1 94694 118368 &
python multifind.py $1 118368   142042 &
python multifind.py $1 142042   165715 &
python multifind.py $1 165715   189389 &
python multifind.py $1 189389   213062 &
python multifind.py $1 213062   236736 &

jobs
