#!/bin/bash

samtools depth -a $1 | awk '{ sum+=$3 } END { print sum/NR}'
