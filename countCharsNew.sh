#!/bin/bash

# script to count chars in file "$1" and outputs a list of the 10 most frequent
# idea for part 1 from https://stackoverflow.com/questions/7578930/bash-split-string-into-character-array
# idea for part 2 from https://stackoverflow.com/questions/8217049/bash-associative-array-sorting-by-value
# version 1.0 by hr

echo "### running" "$0"

echo "-----------------------------------------------"
echo Most frequent chars in "$1"
echo "-----------------------------------------------"

# part 1: count chars in associative array CC

declare -A CC=(  )

for ch in `cat "$1" | fold -w1`
do
   # from https://askubuntu.com/questions/1127282/convert-a-string-of-characters-to-ascii-values
   # see also https://stackoverflow.com/questions/70130059/how-do-you-convert-characters-to-ascii-without-use-of-the-printf-in-bash
   # convert char to its ascii value
   dez=`echo -n "$ch" | od -An -t u1`
   ((CC[$dez]++))    # uninitialized elements take value 0
done

# echo "${CC[@]}"
# echo "${!CC[@]}"

# part 2: prepare output and sort by number

for k in "${!CC[@]}"
do
    # https://stackoverflow.com/questions/890262/integer-ascii-value-to-character-in-bash-using-printf
    # convert ascii value back to char
    ch=`echo $k | awk '{printf("%c",$1)}'`
    echo  $ch ' : ' ${CC["$k"]}
done | sort -rn -k3  | cat -n | head -20    # cat -n adds line numbers
