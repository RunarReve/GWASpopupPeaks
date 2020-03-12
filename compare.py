#!/bin/env/python
#Will compare two assoc to see if there is different and similar peaks
#argv[1] assoc 1
#argv[2] assoc 2
import sys

def main():
   amountCHR = 22
   a1 = [[] for _ in range(amountCHR)]
   a2 = [[] for _ in range(amountCHR)]
   a1sum = 0
   a2sum = 0
 

   p = 9e-9
   for line in open(sys.argv[1]):
      if(line[1] == 'C'):
         continue 
      sline = line.split()
      if(float(sline[8]) > p):
         continue 
#      print(' '.join(sline))
      if(int(sline[0]) > amountCHR):
         continue
      a1[int(sline[0])-1].append(sline)
      a1sum += 1 

   for line in open(sys.argv[2]):
      if(line[1] == 'C'):
         continue 
      sline = line.split()
      if(float(sline[8]) > p):
         continue 
#      print(' '.join(sline))
      if(int(sline[0]) > amountCHR):
         continue
      a2[int(sline[0])-1].append(sline)
      a2sum += 1 

   for each in a1:
      for beach in each:
         print(beach)
   

if __name__ == "__main__":
  main()
