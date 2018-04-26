#!/bin/sh

function createOutputs(){
  if [ ! -e "tests/referenceOutputs" ]; then
    mkdir "tests/referenceOutputs"
  fi

  for testDir in tests/referenceScripts/*; do 
    case=${testDir/tests\//}
    case=${case/referenceScripts\//}
    outputDir=${testDir/Scripts/Outputs}
    echo -e "\n\n\nConsidering test case '${case}'"
    if [ ! -e "${outputDir}" ]; then
      mkdir "${outputDir}"
    fi
    ${testDir}/pythonScript.py ${case} $1
  done
}
