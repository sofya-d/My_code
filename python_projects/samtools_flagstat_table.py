import sys

in_file_path = sys.argv[1]
out_file_path = sys.argv[2]

with open(in_file_path) as in_file:
    lines = in_file.readlines()

block_num = int(len(lines) / 12)
last_percent_str_i = int(3 + 12 * (block_num - 1))

percent_str = []
for i in range(3, last_percent_str_i + 1, 12):
    percent_str.append(lines[i])

mapped_percent = []
for string in percent_str:
    percent_wrd = string.split()
    brackets = percent_wrd[4]
    percent = float(brackets[1:-8])
    mapped_percent.append(percent)

with open(out_file_path, "w") as out_file:
    out_file.write("sample\tmapped\tunmapped\n")
    for i in range(len(mapped_percent)):
        sample = lines[i * 12].split()[0]
        mapped = mapped_percent[i]
        unmapped = float("{:6.2f}".format(100 - mapped))
        out_file.write(f"{sample}\t{mapped}\t{unmapped}\n")