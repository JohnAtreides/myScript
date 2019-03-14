#!/bin/bash

cd /media/cases/Toshiba\ Mopìssau/tOto/HIMYM


for ele in $( ls )
 do
  
  cd /media/cases/Toshiba\ Mopìssau/tOto/HIMYM/$ele
  # read a
  echo "
 ELE = $ele
 "
  for nfo in $( ls | grep nfo )
   do
    rm $nfo
   done
 done

