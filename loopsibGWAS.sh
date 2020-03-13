#!/bin/sh
#Loops through all GWASs that was made with HPOscase/HPOsiblingcontrol
#argv[1] directory of Normal GWAS
#argv[2] directory to Sibling made GWAS



mkdir -p output output/sib/
for each in $(ls ${2}):
do
   x="${each}/${each}_--geno_0.1_--maf_0.01/${each}_--geno_0.1_--maf_0.01.assoc"
   if [ ! -f "${2}${x}" ]; then
      continue 
   fi
   echo "${each}"
   python compare.py ${1}${x} ${2}${x}
   if [ $(wc -l output/sib/${each}| awk '{print $1}') == '0' ]; then 
      rm output/sib/${each}
   fi
done
