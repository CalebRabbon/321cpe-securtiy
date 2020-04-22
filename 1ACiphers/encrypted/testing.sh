#!/bin/bash

cat mono_medium_encrypt.txt
printf "\n\n1.) Translation\n\n"
#                                  1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
cat mono_medium_encrypt.txt | tr "[X,A,V,H,C,Y,S,J,E,D,I,G,F,O,R,P,A,M,B,T,W,N,L,Z]" "[E,T,A,O,I,N,S,R,H,L,D,C,U,M,F,P,G,W,Y,B,V,K,X,J]"

# Trying to switch T and A
printf "\n\n2.) Translation\n\n"
cat mono_medium_encrypt.txt | tr "[X,A,V,H,C,Y,S,J,E,D,I,G,F,O,R,P,A,M,B,T,W,N,L,Z]" "[E,A,T,O,I,N,S,R,A,H,L,D,C,U,M,F,P,G,W,Y,B,V,K,X,J]"


# Trying to switch X->A, A->T, V->E
printf "\n\n3.) Translation\n\n"
#                                  1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
cat mono_medium_encrypt.txt | tr "[X,A,V,H,C,Y,S,J,E,D,I,G,F,O,R,P,A,M,B,T,W,N,L,Z]" "[A,T,R,I,O,T,N,S,R,H,L,D,C,U,M,F,P,G,W,Y,B,V,K,J]"


printf "\n\n4.) Translation\n\n"
#                                  1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
cat mono_medium_encrypt.txt | tr "[X,A,V,H,C,Y,S,J,E,D,I,G,F,O,R,P,A,M,B,T,W,N,L,Z]" "[E,T,A,H,I,S,S,R,Y,L,D,C,U,W,F,P,T,C,Y,B,V,K,X,J]"

#Encryption Key
#[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
#[Z,Y,O,R,B,U,N,X,L,P,M,J,T,I,S,Q,V,G,F,K,W,C,A,H,D,E]
#Letter that gets mapped to
