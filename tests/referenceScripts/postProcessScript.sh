#!/bin/sh
# Copyright (C) Julien Tierny <julien.tierny@sorbonne-universite.fr>

function print_usage(){

  echo "Usage:"
  echo "  $0"
  echo "  <path to python script>"
  exit
}

function insert_header(){
  echo "from paraview.simple import *"

  echo "if len(sys.argv) >= 2:"
  echo -e "\toutputDirectory = sys.argv[1] + "/""
  echo -e "\tif len(sys.argv) == 3:"
  echo -e "\t\tdebugLevel = sys.argv[2]"
  echo -e "\telse:"
  echo -e "\t\tdebugLevel = 0"
  echo "else:"
  echo -e "\tprint("Missing output directory")"
  echo -e "\tsys.exit()"

  echo "if debugLevel != 0:"
  echo -e "\tprint("  Debug level: " + debugLevel)"
}

function write_out(){
  echo "$1.DebugLevel = int(debugLevel)"
  echo "if $1.GetNumberOfOutputPorts() != 1:"
  echo -e "\tfor i in range(0, $1.GetNumberOfOutputPorts()):"
  echo -e "\t\tSaveData(outputDirectory + '$1_' + str(i) + ".vtu","
  echo -e "\t\t\tCleantoGrid(OutputPort($1, i)))"
  echo "else:"
  echo -e "\tSaveData(outputDirectory + '$1.vtu',"
  echo -e "\t\tCleantoGrid(OutputPort($1)))"
}

if [ -z "${1}" ]; then
  print_usage
fi

insert_header >> tmp.py

for object in `cat ${1} | grep "= TTK"`; do
  object=`echo ${object} | grep "^tTK"`
  if [ ! -z "${object}" ]; then
    echo "Considering TTK object '${object}'..."
    write_out $object >> tmp.py
  fi
done

mv tmp.py $1
