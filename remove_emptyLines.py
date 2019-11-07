import sys

try:
    def remove_emptylines(input, output):
        with open(input) as infile, open(output, 'w') as outfile:
            for line in infile:
                if not line.strip(): continue
                outfile.write(line)

    remove_emptylines(sys.argv[1], sys.argv[2])

except:
    print("Usage: python remove_emptyLines.py <input_name.txt> <output_name.txt>")