#!/bin/bash 

# bash script to replace given char-patterns by others
# special solution for substdigits.sh in https://github.com/pmarf/bashBootcamp/blob/main/README.md 
# author : hr
# vers 2026-0331

echo "### running " $0

while IFS='=' read -r digit text; do # fill dictionary with text
   if [[ -z $digit ]]; then
      continue # skip empty lines
   fi
   TT["$digit"]="$text"
done << 'EOF'
0=zero
1=one
2=two
3=three
4=four
5=five
6=six
7=seven
8=eight
9=nine
EOF

echo ### pattern read:

for k in "${!TT[@]}"; do
    echo $k ' : ' ${TT["$k"]}
done 

echo ### generating script to run

# header + start of sed
echo "#!/bin/bash " > "$0".run
echo "# =================================" >> "$0".run
echo "# starting $0 with input $1" >> "$0".run
echo "# =================================" >> "$0".run
echo 'sed -E "{' >> "$0".run

# sed substitutions
for k in "${!TT[@]}"; do
    echo "         s|"$k"|${TT["$k"]}|g;" >> "$0".run
done 

# end of sed command with input output file
echo '}" ' "$1" '>' "$1".rep3 >> "$0".run

# make script executable
chmod +x "$0".run

# show generated file
echo '-------------------------------'
echo "### this script was generated as" "$0".run
echo '-------------------------------'
cat "$0".run
echo '-------------------------------'

read -rp "run scrip now (y/n) " ans

if [[ "$ans" == y ]]; then
   echo running script "$0".run 
   source "$0".run
else
   echo you can run generated scrip by typing '"'"$0".run'"' in the shell
fi


