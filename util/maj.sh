#!/bin/bash

 echo "
sudo apt-get update"

 echo "sudo apt-get upgrade
    #
     #
      #
       #
        #"
 echo "            Do you want your pinguin to evolve ?

                               --> * or N"

 read -s a
 if [[ $a != [nN] ]]
  then
#   echo $a 
   sudo apt-get update && sudo apt-get upgrade -y

# elif [[ $a == [yY] ]] #[ $a != [nN] ] && [ $a != [yY] ]
#  echo " C'est pô bien ! "

 else
  echo " C'est pô bien ! "

 fi
