#!/bin/bash

# 1st argument is path to gz fastq file

gunzip -c $1 | sed -n '2~4p' | tr -d "\n" | wc -c
