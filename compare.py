#!/bin/env/python
#Will compare two assoc to see if there is different and similar peaks
#argv[1] assoc 1 and name basis of outfile
#argv[2+] other assoc 
import sys

def main():
   outdir="output/sib/"
   amountCHR = 22
   a1 = [[] for _ in range(amountCHR)]
   a2 = [[] for _ in range(amountCHR)]
   a1sum = 0
   peakpoint = 0.15 #Definition of a chromosome peak 
   a1name  = sys.argv[1].split('/')[-1].split('_')[0]
   outfile = open(outdir+a1name, 'w')
   a1chr=[] #Store CHR with peaks
   
   p = 9e-9
   for line in open(sys.argv[1]):
      if(line[1] == 'C'):
         continue 
      sline = line.split()
      if(float(sline[8]) > p):
         continue 
      if(int(sline[0]) > amountCHR):
         continue
      a1[int(sline[0])-1].append(sline)
      a1sum += 1 

   #Print peaks of main
   for i in (range(amountCHR)):
      a1p = what(len(a1[i-1]), a1sum)
      if(a1p > peakpoint):
         print(a1name+" parent_peak CHR: "+str(i)+" %: "+str(a1p))
         outfile.write(a1name+" parent_peak CHR: "+str(i)+" %: "+str(a1p)+'\n')
         a1chr.append(i)

   print("----------------------------------------------------------")
   for each in sys.argv:  
      if(each == sys.argv[0] or each == sys.argv[1]): 
         continue
      a2sum = 0
      a2name = each.split('/')[-1].split('_')[0]
      for line in open(each):
         if(line[1] == 'C'):
            continue 
         sline = line.split()
         if(float(sline[8]) > p):
            continue 
         if(int(sline[0]) > amountCHR):
            continue
         a2[int(sline[0])-1].append(sline)
         a2sum += 1 

      #Print peaks of main
      for i in (range(amountCHR)):
         a2p = what(len(a2[i-1]), a2sum)
         if(a2p > peakpoint):
            newpeak = "newPeak"
            if(i in a1chr):
               newpeak = "samePeak"   
            print(a2name+" child_peak CHR: "+str(i)+" %: "+str(a2p)+" "+newpeak)
            outfile.write(a2name+" child_peak CHR: "+str(i)+" %: "+str(a2p)+" "+newpeak+'\n')




#Will find the persentage of given value is of the tot
def what(dis, tot): 
   if(dis == 0):
      return 0 
   #print(str(dis) + '/'+str(tot)+' = '+ str(float(dis)/tot))
   return float(dis)/tot

if __name__ == "__main__":
  main()
