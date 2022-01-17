# Writes number of lines of txt-like files with exact length and length of those lines in .txt file.
```console
for i in *.fq; do echo $i; echo $i >> reads_length.txt; awk '{++a[length()]} END{for (i in a) print i, a[i]}' $i >> reads_length.txt; done
```
# Writes number of lines and number of reads of .fastq file in .txt file.
```console
for i in *.fq; do echo $i; echo $i >> lines_reads.txt; echo "number of lines" >> lines_reads.txt; wc -l < $i >> lines_reads.txt; echo "number of lines divided by 4" >> lines_reads.txt; printf %.2f\\n "$((100 * $(wc -l < $i) / 4))e-2" >> lines_reads.txt; echo "number of reads" >> lines_reads.txt; grep '^@HISEQ' $i | wc -l >> lines_reads.txt; done
```
