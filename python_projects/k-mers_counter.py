# K-mers Counter
def k_mer_counter(dna_seqs, k):
# counts a quantity of original and repetitive k-mers (substrings of length k contained within a biological sequence)
# input:
# dna_seqs - dictionary with keys as names of sequences and values as sequences
# k - length of k-mer (substring)
# output:
# a character string with quantity of original and repetitive k-mers
    k_mers = {}
    for heading in dna_seqs.keys():
        sequence = dna_seqs[heading]
        stop = k
        for start in range(len(sequence)):
            if stop <= len(sequence):
                k_mer = sequence[start:stop]
                stop += 1
                if k_mer not in k_mers.keys():
                    k_mers[k_mer] = 1
                else:
                    k_mers[k_mer] += 1

    original_count = 0
    repetitive_count = 0
    for count in k_mers.values():
        if count == 1:
            original_count += 1
        else:
            repetitive_count += 1

    return f"Sequences contain {original_count} original {k_input}-mer(s) and {repetitive_count} repetitive {k_input}-mer(s)"

dna_seqs = {1:"atatacta", 2:"tgcacaca"}
k_mer_counter(dna_seqs, 8)
