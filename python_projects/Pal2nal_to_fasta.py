# .pal2nal to .fasta converter
def pal2nal_2_fasta(lines):
# converts .pal2nal format to .fasta format
# input:
# lines - a list with lines of .pal2nal file as values
# output:
# a list with lines of .fasta format as values
    # delete first line in list
    lines = lines[1:len(lines)]

    # delete "\n" in the and of every string
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()

    # find number of parts that make up a sequence line (it might be the same for all sequences in file because they are aligned)
    seq_parts_num = 0
    for i in range(1, len(lines)):
        line = lines[i]
        marker = "sequence"
        seq_parts_num += 1
        for symbol in line.lower():
            if symbol not in "atgc":
                marker = "header"
                break
        if marker == "header":
            seq_parts_num -= 1
            break

    # compute the quantity of lines between headers, number of headers
    header_gap = seq_parts_num + 1
    header_num = int(len(lines) / header_gap)

    # make list of header indexes in "lines" list
    header_indexes = []
    for i in range(header_num):
        header_indexes.append(i * header_gap)

    # add ">" to the start of header, "\n" to the end of header, "\n" to the end of sequence
    for i in header_indexes:
        lines[i] = f">{lines[i]}\n"
        lines[i + seq_parts_num] = f"{lines[i + seq_parts_num]}\n"
    return(lines)
