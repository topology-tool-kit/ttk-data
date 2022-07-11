#!/bin/bash

# Prepare a module white list based on the test examples
# July 2022, Julien Tierny <julien.tierny@sorbonne-universite.fr>

outputFile="whiteList.csv"

whiteList=()
exampleList=()

isInWhiteList (){
  pos=0
  for entry in ${whiteList[@]}; do
    if [ $entry == $1 ]; then
      return $pos
    fi
    pos=`echo $pos + 1 | bc`
  done
  return 255
}

add2whiteList () {
  isInWhiteList $1 
  pos=$?
  if [ $pos == 255 ]; then
      echo "Adding $1 to white list..."
      whiteList+=( $1 )
      exampleList+=( $2 )
  else
      if [[ ! "${exampleList[$pos]}" == *"$2" ]]; then
        exampleList[$pos]="${exampleList[$pos]} $2"
      fi
  fi
}

for example in *.pvsm; do
  list=`grep TTK $example`
  for word in $list; do
    if [ ! -z `echo $word | grep name` ]; then
      module=`echo "$word" | cut -d'"' -f 2`
      module=`echo "$module" | cut -d'(' -f 1`
      module=${module//[[:digit:]]/}
      if [[ "$module" == "TTK"* ]]; then
        add2whiteList ${module} $example
      fi
    fi
  done
done

for example in *.py; do
  list=`grep "= TTK" $example`
  for word in $list; do
    if [ ! -z `echo $word | grep TTK` ]; then
      module=`echo "$word" | cut -d'(' -f 1`
      add2whiteList ${module} $example
    fi
  done
done

echo "Saving white list to '$outputFile'..."
rm $outputFile 2> /dev/null
pos=0
for entry in ${whiteList[@]}; do
  echo "$entry, ${exampleList[$pos]}" >> whiteList.csv
  pos=`echo $pos + 1 | bc`
done
