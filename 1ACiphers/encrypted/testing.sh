#!/bin/bash

cat mono_easy_encrypt.txt
printf "\n\n1.) Translation\n\n"
#                                1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
cat mono_easy_encrypt.txt | tr "[B,K,Z,S,F,I,L,G,X,J,N,R,T,W,U,D,A,O,Q,C,Y,M,H,P,E,V]" "[E,T,A,O,I,N,S,R,H,L,D,C,U,M,F,P,G,W,Y,B,V,K,X,J,Q,Z]"

# Noticed from the word AVOMT should be ABOUT Mapping V->B M->U
# Noticed JEFFERION -> JEFFERSON. I->S
printf "\n\n2.) Translation\n\n"
cat mono_easy_encrypt.txt | tr "[B,K,Z,S,F,I,L,G,X,J,N,R,T,W,U,D,A,O,Q,C,Y,M,H,P,E,V]" "[E,T,A,O,S,N,S,R,H,L,D,C,U,U,F,P,G,W,Y,B,B,K,X,J,Q,Z]"

#THOUAS -> THOMAS. U->M, ANC -> AND C->D, SS -> IS, AMERIWA -> AMERICA W->C, LIBE-> LIVE B->V, THOUDH->THOUDH D->G GEST COAST->WEST COAST G->W
printf "\n\n3.) Translation\n\n"
#                                1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
cat mono_easy_encrypt.txt | tr "[B,K,Z,S,F,I,L,G,X,J,N,R,T,W,U,D,A,O,Q,C,Y,M,H,P,E,V]" "[E,T,A,O,S,N,I,R,H,L,G,D,M,U,F,P,W,C,Y,V,B,K,X,J,Q,Z]"

#SIGNIFICANTLP->SIGNIFICANTLY P->Y ROYE->ROPE Y->P, From googling QIEGLER->ZIEGLER
printf "\n\n3.) Translation\n\n"
#                                1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
cat mono_easy_encrypt.txt | tr "[B,K,Z,S,F,I,L,G,X,J,N,R,T,W,U,D,A,O,Q,C,Y,M,H,P,E,V]" "[E,T,A,O,S,N,I,R,H,L,G,D,M,U,F,Y,W,C,P,V,B,K,X,J,Z,Q]"
