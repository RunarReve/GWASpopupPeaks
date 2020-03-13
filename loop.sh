#!/bin/sh
#Loops through all GWASs that was made with HPOscase/HPOsiblingcontrol

rm -f combined

for each in $(wc -l output/sib/* | awk '{if($1 > 1){print $2}}' )
do
   echo "${each}"
   string=$(echo "${each}" | sed -e 's/\// /g' | awk '{print $NF}')
   same="x"
   diff="x"

   #Get all peaks
   for i in $(grep parent_peak ${each}| awk '{print $4}');do
      string="${string},${i}"
   done
   for i in $(grep samePeak ${each} | awk '{print $1","$4}'); do
      same="${same}_${i}"
   done
   for i in $(grep newPeak  ${each} | awk '{print $1","$4}'); do
      diff="${diff}_${i}"
   done
   #Remove default value if anything else is added 
   same=$(echo "${same}" |sed -e 's/x_//g')
   diff=$(echo "${diff}" |sed -e 's/x_//g')

   string="${string}	${same}	${diff}"
   
   echo "${string}" >> combined
done
