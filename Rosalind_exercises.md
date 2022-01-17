# 1. Installing Python.

```python
"The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"
```

# 2. Variables and Some Arithmetic.

```python
a = int(input())
b = int(input())
square_c = a ** 2 + b ** 2
print(square_c)
```

# 3. Strings and Lists.

```python
s = raw_input()
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
d = int(raw_input())
asb = s[a:(b + 1)]
csd = s[c:(d + 1)]
ans = f"{asb} {csd}"
print(ans)
```

# 4. Conditions and Loops.

```python
a = int(raw_input())
b = int(raw_input())
sum = 0
for num in range(a, b + 1):
    if num % 2 == 1:
        sum += num
print(sum)
```

# 5. Working with Files.

```python
with open('rosalind_ini.txt', 'r') as input_file, open('answer.txt', 'w') as output_file:
    count = -1
    for line in input_file:
        count += 1
        if count % 2 == 1:
            output_file.write(line)
```

# 6. Dictionaries.

```python
data = input().split()
from collections import Counter
data = dict(Counter(data))
for key in data:
    print(key, data[key])
```
# 7. Let's Be Practical.

```python
seq = input()
counts = collections.Counter(seq)
print( counts['A'], counts['C'], counts['G'], counts['T'], end = " ")

```
# 8. GenBank Introduction.

```python
from Bio import Entrez

def genbank(genus, dtstart, dtend):
    Entrez.email = "sumepremos@gmail.ru"
    term = F"{genus}[Organism] AND {dtstart}[Publication Date] : {dtend}[Publication Date]"
    handle = Entrez.esearch(db = "nucleotide", term = term)
    record = Entrez.read(handle)
    return record["Count"]

print(genbank("Sulfurospirillum", "2007/10/25", "2009/02/03"))
```

# 9. Data Formats.

```python
from Bio import Entrez
from Bio import SeqIO

IDs = input().split()

Entrez.email = "sumepremos@gmail.ru"
handle = Entrez.efetch(db = "nucleotide", id = IDs, rettype = "fasta")
records = list(SeqIO.parse(handle, "fasta"))

ans_i = 0
record_len = len(records[0].seq)

for i in range(len(records)):
    if len(records[i].seq) < record_len:
        record_len = len(records[i].seq)
        ans_i = i

ans_handle = Entrez.efetch(db = "nucleotide", id = IDs[ans_i], rettype = "fasta")
ans_record = ans_handle.read()

print(ans_record)
```

# 10. FASTQ format introduction.

```python
from Bio import SeqIO

count = SeqIO.convert("rosalind_tfsq.txt", "fastq", "seq.fasta", "fasta")
print(f"{count} records converted")

# 7. Read Quality Distribution.

from Bio import SeqIO

with open('fastq_threshold.txt', 'r') as fastq_threshold, open('fastq.txt', 'w') as fastq:
    lines = fastq_threshold.readlines()
    threshold = int(lines[0])
    del lines[0]
    for line in lines:
        fastq.write(line)

count = 0
for record in SeqIO.parse("fastq.txt", "fastq"):
    phred = record.letter_annotations["phred_quality"]
    if sum(phred) / len(phred) < threshold:
        count += 1

print(count)
```
# 11. Read Quality Distribution.

```python
from Bio import SeqIO

with open('fastq_threshold.txt', 'r') as fastq_threshold, open('fastq.txt', 'w') as fastq:
    lines = fastq_threshold.readlines()
    threshold = int(lines[0])
    del lines[0]
    for line in lines:
        fastq.write(line)

count = 0
for record in SeqIO.parse("fastq.txt", "fastq"):
    phred = record.letter_annotations["phred_quality"]
    if sum(phred) / len(phred) < threshold:
        count += 1

print(count)
```

# 12. Read Filtration by Quality.

```python
from Bio import SeqIO

with open('fastq_threshold.txt', 'r') as fastq_threshold, open('fastq.txt', 'w') as fastq:
    lines = fastq_threshold.readlines()
    values = lines[0].split()
    threshold = int(values[0])
    percentage = int(values[1])
    del lines[0]
    for line in lines:
        fastq.write(line)

count = 0
for record in SeqIO.parse("fastq.txt", "fastq"):
    phred = record.letter_annotations["phred_quality"]
    ok_scores = 0
    for score in phred:
        if score >= threshold:
            ok_scores += 1
    if ok_scores / len(phred) * 100 >= percentage:
        count += 1

print(count)
```

# 13. Base Quality Distribution.

```python
from Bio import SeqIO

with open('fastq_threshold.txt', 'r') as fastq_threshold, open('fastq.txt', 'w') as fastq:
    lines = fastq_threshold.readlines()
    threshold = int(lines[0])
    del lines[0]
    for line in lines:
        fastq.write(line)

cyc_count = 0
all_phred = []
for record in SeqIO.parse("fastq.txt", "fastq"):
    phred = record.letter_annotations["phred_quality"]
    cyc_count += 1
    if all_phred == []:
        all_phred = phred
    for i in range(len(phred)):
        if cyc_count != 1:
            all_phred[i] += phred[i]

for i in range(len(all_phred)):
    all_phred[i] = all_phred[i] / cyc_count

pos_count = 0
for score in all_phred:
    if score < threshold:
        pos_count += 1

print(pos_count)
```
