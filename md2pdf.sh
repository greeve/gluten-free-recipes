#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 0
fi

pandoc $1 -s -o $2 --toc --toc-depth 2 --pdf-engine=xelatex -V geometry:margin=1in -V toc-title='Table of contents'
