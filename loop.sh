#!/bin/sh
#Loops through all GWASs that was made with HPOscase/HPOsiblingcontrol


for each in $(ls output/sib):
do
   #echo "${each}"

   cat output/sib/${each} | sed -e 's/newPeak/newPeak\n/g' | sed -e 's/samePeak/samePeak\n/g' > output/sib/${each}T
   mv output/sib/${each}T output/sib/${each} 

   #if [ $(wc -l output/sib/${each}| awk '{print $1}') == '0' ]; then 
   #   rm output/sib/${each}
   #fi
done
