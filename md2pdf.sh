#!/bin/bash
# input 1: source md file
# input 2: output pdf file

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 0
fi

pandoc $1 -s -o $2 --toc --toc-depth 2 --pdf-engine=xelatex -V geometry:margin=1in -V mainfont="Charter" -V toc-title='Table of contents' --template bin/default.latex
