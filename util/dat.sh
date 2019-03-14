#!/bin/bash


 echo "
      ----//#****  Today's Date  ****#\\\----
"


 while true; do echo "$(date '+%D %T' | toilet -f term -F border --gay)"; sleep 1; done

