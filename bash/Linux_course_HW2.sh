gunzip rsid.tsv.gz
gunzip hail.tsv.gz

# join hail.tsv and rsid.tsv
# delete column names
sed -i '1d' hail.tsv
sed -i '1d' rsid.tsv
# sort table with the first column with locus coordinates
sort -k 1b,1 hail.tsv > hail_sorted.tsv
sort -k 1b,1 rsid.tsv > rsid_sorted.tsv
# join
join hail_sorted.tsv rsid_sorted.tsv > joined.tsv

# create file with "SNP" column
awk '{print $13}' joined.tsv > SNP.txt
sed -i '1s/^/SNP\n/' SNP.txt # 13372796 lines

# create files with "tA1" and "tA2" columns
# isolate column with nucleotide variants written in a form ["A","T"]
awk '{print $2}' joined.tsv > A.txt
# delete brackets from lines (first and last character of a string)
sed -i "s/^.//;s/.$//g" A.txt
# "s/" - substitution "." - "match any character"; "^" - matches the null string at beginning of the pattern space; "$" - matches the null string at end of the pattern space
# now we have csv file with 2 columns that can be split
cut -d"," -f 1 A.txt > tA2.txt
cut -d"," -f 2 A.txt > tA1.txt
# delete quotes
sed -i "s/^.//;s/.$//g" tA1.txt
sed -i "s/^.//;s/.$//g" tA2.txt
# create file with "tA2" column
sed -i '1s/^/tA1\n/' tA1.txt
sed -i '1s/^/tA2\n/' tA2.txt

# create file with "tN" column
touch tN.txt
echo tN > tN.txt
counter=0; while [ $counter -lt 13372795 ]; do counter=$(($counter+1)); echo 499956 >> tN.txt; done

# create file with "tP" column
awk '{print $11}' joined.tsv > tP.txt
sed -i '1s/^/tP\n/' tP.txt

# create file with "tZ" column
awk '{print $8/$9}' joined.tsv > tZ.txt
sed -i '1s/^/tZ\n/' tZ.txt

# merge new columns to create new table
paste SNP.txt tA1.txt tA2.txt tN.txt tP.txt tZ.txt > result.txt