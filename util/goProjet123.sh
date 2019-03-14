#!/bin/bash


 echo "
      ----//#****  Which project launch ?  ****#\\\----"
 read a

 echo "Vous avez choisi le projet $a"
 cd /home/cases/Documents/Master1/ProgWeb/projet$a/
 #echo `code .`

 echo " cd .."
 echo " ./mongodb-linux-x86_64-4.0.3/bin/mongod --dbpath=data
"
 echo "  cd /Documents/Master1/ProgWeb/mongodb-linux-x86_64-4.0.3/bin
  ./mongo
"
 echo " use restaurant
"
 echo " --------------------------
"


 echo " show bds"
 echo " show collections"
 echo " db.dishes.findOne()"
 echo " db.Dish.drop()"
 echo " db.deserts.insertOne({name:\"Flant\", type:\"deserts\", desc:\"Flantflantflantder\", price:\"66€\"})
"



"name" : "Nouilles de la Cour de Corail",
        "type" : "plat",
        "desc" : "110g de Spaghetti, Huile d’olive, Bacon, Piment de Cayenne sec, Parmesan",
        "price" : "7"




# b="$( pwd )"
