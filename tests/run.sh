#!/bin/sh
# Copyright (C) Julien Tierny <julien.tierny@sorbonne-universite.fr>

function print_usage(){

  echo "Usage:"
  echo "  $0"
  echo "  -d <debug level>"
  echo "  -g [generate the reference outputs]"
  exit
}

function createOutputs(){
  baseName="$1"
  if [ ! -e "tests/${1}Outputs" ]; then
    mkdir "tests/${1}Outputs"
  fi

  for testDir in tests/referenceScripts/*; do 
    if [ -d $testDir ]; then
      case=${testDir/tests\//}
      case=${case/referenceScripts\//}
      outputDir=tests/${1}Outputs/${case}
      echo -e "\n\n\nConsidering test case '${case}'"
      if [ ! -e "${outputDir}" ]; then
        mkdir "${outputDir}"
      fi
      pvpython ${testDir}/pythonScript.py ${outputDir} $2
    fi
  done
}

function compareOutputs(){
  for testDir in tests/$1Outputs/*; do
    case=${testDir/tests\//}
    case=${case/${1}Outputs\//}
    echo "Comparing case '${case}'..."
    for file in tests/$1Outputs/${case}/*; do
      file=${file/tests\//}
      file=${file/${1}Outputs\//}
      diff tests/$1Outputs/$file tests/$2Outputs/$file 
    done
  done
}

debugLevel="0"
generateRef="0"

while getopts "d:gh" option
do
  case $option in
    d)
      debugLevel=$OPTARG
      ;;
    g)
      generateRef="1"
      ;;
    h)
      print_usage
      ;;
  esac
done

if [ $generateRef -eq "1" ]; then
  echo "Generating reference outputs..."
  createOutputs "reference" $debugLevel 
else
  if [ ! -e tests/referenceOutputs ]; then
    echo "Error!"
    echo "Could not find directory 'tests/referenceOutputs/'..."
    echo "Please make sure that reference outputs have been generated first."
    print_usage
  fi
  echo "Generating test outputs..."
  rm -R tests/testOutputs 2> /dev/null
  createOutputs "test" $debugLevel
  echo -e "\n\n\nComparing outputs..."
  compareOutputs "reference" "test"
fi
