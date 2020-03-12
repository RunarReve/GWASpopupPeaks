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
   peakpoint = 0.15
   a1name = sys.argv[1].split('/')[-1]
   a2name = sys.argv[2].split('/')[-1]


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

   #How to define a peak easily
   #When one chromosome is <15% of the assoc
   for i, a1l, a2l in zip(range(amountCHR), a1, a2):
      a1p = what(len(a1l), a1sum)
      a2p = what(len(a2l), a2sum)
      if(a1p > peakpoint):
         print(a1name+" parent has peak at CHR: "+str(i)+" it's "+str(a1p)+" of the assoc")
      if(a2p > peakpoint):
         print(a2name+" child  has peak at CHR: "+str(i)+" it's "+str(a2p)+" of the assoc")
      
#      print(str(i+1) +' '+str(len(a1l))+' '+a1p+'\t'+str(len(a2l))+' '+a2p )


#Will find the persentage of given value is of the tot
def what(dis, tot): 
   if(dis == 0):
      return 0 
   #print(str(dis) + '/'+str(tot)+' = '+ str(float(dis)/tot))
   return float(dis)/tot

if __name__ == "__main__":
  main()
