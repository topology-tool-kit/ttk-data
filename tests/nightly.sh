#!/bin/sh
# Copyright (C) Julien Tierny <julien.tierny@sorbonne-universite.fr>

function create_sample_configuration(){

  echo "TTK_SOURCE_DIR='path to TTK source dir'" > "$1"
  echo "TTK_DATA_DIR='path to TTK data dir'" >> "$1"
}

function print_usage(){

  echo "Usage:"
  echo "  $0"
  echo "  -c <absolute path to configuration file>"
  exit
}

function update_source(){
  
  currentDir=`pwd`
  echo "Updating source repository..." | tee -a $2
  cd $1
  git pull | tee -a $2
  rm -R build 2> /dev/null | tee -a $2
  mkdir build | tee -a $2
  cd $currentDir
}

function update_build(){

  currentDir=`pwd`
  cd $1
  echo "Building sources..." | tee -a $2
  cmake ../ -G Ninja | tee -a $2
  ninja install | tee -a $2
  cd $currentDir 
}

function update_data(){
  
  currentDir=`pwd`
  echo "Updating data repository..." | tee -a $2
  cd $1 | tee -a $2
  git pull | tee -a $2
  cd $currentDir
}

function run_tests(){

  currentDir=`pwd`
  echo "Running tests..." | tee -a $2
  cd $1 | tee -a $2
  tests/run.sh  | tee -a $2
  cd $currentDir | tee -a $2
}

configFile=""
while getopts "c:h" option
do
  case $option in
    c)
      configFile=$OPTARG
      ;;
    h)
      print_usage
      ;;
  esac
done

if [ -z "$configFile" ]; then
  echo "No configuration file provided!"
  sampleFile="sample.conf"
  create_sample_configuration $sampleFile
  echo "A sample configuration file has been created in '$sampleFile'"
  print_usage
fi

source $configFile
currentDate=`date`
logFile="`pwd`/ttk-nightly-check-${currentDate// /_}.log"

update_source $TTK_SOURCE_DIR $logFile
update_build $TTK_SOURCE_DIR/build $logFile
update_data $TTK_DATA_DIR $logFile
run_tests $TTK_DATA_DIR $logFile
