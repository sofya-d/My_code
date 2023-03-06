#!/bin/bash

for input in *.tsv
do
	# get rid of heading
	tail -n +2 "$input" > file

	# calculating mean number of mutations per patient
	line_num=$(wc -l < file)
	uniq_tsb_num=$(awk '{print $16}' file | sort | uniq -c | wc -l)
	mean_mut_num=$(($line_num / $uniq_tsb_num))

	cancer_type=$(awk -v file_name="$input" 'BEGIN {str = file_name; sub("_mutations.tsv", "", str); print str}')

	cat file | awk 'BEGIN {FS = "\t"; OFS = FS}; {print $5 "_" $6 "_" $7 "_" $11 "_" $12 " " $1, $16}' | sort -t $'\t' -k 1 | uniq | awk 'BEGIN {FS = "\t"; OFS = FS}; {print $1}' | uniq -c | sed -e 's/^ *//' | awk -v mean_mut_num=$mean_mut_num -v cancer_type=$cancer_type 'BEGIN {print "ID", "gene_" cancer_type, "rec_" cancer_type "_" mean_mut_num}; {print $2, $3, $1}' | sed -e 's/ /\t/g' > ./recurrency/${cancer_type}_recurrency.tsv
done

for i in *.tsv; do (head -n 1 $i && tail -n +2 $i | sort -t $'\t' -k 1b,1) > ./sorted/$i; done

join -t $'\t' -e 0 -a1 -a2 -o auto BLCA_recurrency.tsv BRCA_recurrency.tsv > 1
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 1 && tail -n +2 1 | sort -t $'\t' -k 1b,1) CESC_recurrency.tsv > 2
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 2 && tail -n +2 2 | sort -t $'\t' -k 1b,1) CHOL_recurrency.tsv > 3
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 3 && tail -n +2 3 | sort -t $'\t' -k 1b,1) GBM_recurrency.tsv > 4
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 4 && tail -n +2 4 | sort -t $'\t' -k 1b,1) HNSC_recurrency.tsv > 5
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 5 && tail -n +2 5 | sort -t $'\t' -k 1b,1) KICH_recurrency.tsv > 6
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 6 && tail -n +2 6 | sort -t $'\t' -k 1b,1) KIRC_recurrency.tsv > 7
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 7 && tail -n +2 7 | sort -t $'\t' -k 1b,1) KIRP_recurrency.tsv > 8
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 8 && tail -n +2 8 | sort -t $'\t' -k 1b,1) LGG_recurrency.tsv > 9
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 9 && tail -n +2 9 | sort -t $'\t' -k 1b,1) LIHC_recurrency.tsv > 10
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 10 && tail -n +2 10 | sort -t $'\t' -k 1b,1) LUAD_recurrency.tsv > 11
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 11 && tail -n +2 11 | sort -t $'\t' -k 1b,1) LUSC_recurrency.tsv > 12
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 12 && tail -n +2 12 | sort -t $'\t' -k 1b,1) PAAD_recurrency.tsv > 13
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 13 && tail -n +2 13 | sort -t $'\t' -k 1b,1) PCPG_recurrency.tsv > 14
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 14 && tail -n +2 14 | sort -t $'\t' -k 1b,1) PRAD_recurrency.tsv > 15
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 15 && tail -n +2 15 | sort -t $'\t' -k 1b,1) SKCM_recurrency.tsv > 16
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 16 && tail -n +2 16 | sort -t $'\t' -k 1b,1) THCA_recurrency.tsv > 17
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 17 && tail -n +2 17 | sort -t $'\t' -k 1b,1) UCEC_recurrency.tsv > 18
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 18 && tail -n +2 18 | sort -t $'\t' -k 1b,1) UCS_recurrency.tsv > 19
join -t $'\t' -e 0 -a1 -a2 -o auto <(head -n 1 19 && tail -n +2 19 | sort -t $'\t' -k 1b,1) UVM_recurrency.tsv > cancer_recurrency.tsv

tail -n +2 cancer_recurrency.tsv | awk 'BEGIN {print "SUMS"}; {print $3+$5+$7+$9+$11+$13+$15+$17+$19+$21+$23+$25+$27+$29+$31+$33+$35+$37+$39+$41+$43}' > SUMS.txt

paste cancer_recurrency.tsv SUMS.txt > cancer_recurrency_sums.tsv

(head -n 1 cancer_recurrency_sums.tsv && tail -n +2 cancer_recurrency_sums.tsv | sort -r -n -t $'\t' -k 44) > cancer_recurrency_sums_sorted.tsv

scp -P 22160 user6@ctddev.ifmo.ru:/home/user6/linux/hw4/recurrency/sorted/cancer_recurrency_sums_sorted.tsv.gz /mnt/c/users/User/Downloads