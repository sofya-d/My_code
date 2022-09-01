from os import listdir
from os.path import join
from sys import argv

# pass the files directory argument
f_dir = sys.argv[1]
# pass the files format
f_name_end = sys.argv[2]
# pass the output directory path argument
out_dir = sys.argv[3]
# pass the output file name with format argument
out_f_name = sys.argv[4]

files = [f_name for f_name in listdir(f_dir) if f_name_end in f_name]

with open(join(out_dir, out_f_name), "w") as out_f:
    #write the header of the file
    out_f.write("file;read_number;mean_read_length\n")
    
    for f_name in files:
        name = f_name.replace(f_name_end, "")
        
        num = 0
        count = 0
        r_num = 0
        r_len_mean = 0
        with open(join(f_dir, f_name), "r") as file:
            
            for line in file:
                num += 1
                count += 1
                if count == 2:
                    r_num += 1
                    r_len_mean += len(line.strip())
                if count == 4:
                    count = 0
            
            num = num / 4
            if num.is_integer() == True:
                r_len_mean = r_len_mean / r_num
                out_f.write(f"{name};{r_num};{r_len_mean}\n")
            
            else:
                out_f.write(f"{name};NA;NA\n")