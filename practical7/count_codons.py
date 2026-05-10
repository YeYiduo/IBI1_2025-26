import re
import matplotlib.pyplot as plt

def read_fasta(filename):
    genes = {}
    current_header = None
    current_seq = []

    with open(filename, 'r', encoding='latin-1') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                if current_header is not None:
                    genes[current_header] = '\n'.join(current_seq)
                current_header = line
                current_seq = []
            else:
                current_seq.append(line)
        if current_header is not None:
            genes[current_header] = '\n'.join(current_seq)
    return genes

#  find the longest ORF stop codon position
def find_longest_orf_stop(seq, target_stop):
    max_len = 0
    best_pos = -1
    seq = seq.replace('\n', '')  

    for frame in range(3):
        for i in range(frame, len(seq)-2, 3):
            codon = seq[i:i+3]
            if codon == "ATG":
                for j in range(i, len(seq)-2, 3):
                    c = seq[j:j+3]
                    if c == target_stop:
                        length = j - i + 3
                        if length > max_len:
                            max_len = length
                            best_pos = j
                        break
    return best_pos

# Caculate all in-frame codons upstream of the stop codon
def get_upstream_codons(seq, stop_pos):
    codons = []
    seq = seq.replace('\n', '')
    for i in range(stop_pos - 3, -1, -3):
        codons.append(seq[i:i+3])
    return codons

# main
filename = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
genes = read_fasta(filename)

#  input stop codon
target = input("Enter stop codon (TAA/TAG/TGA): ").strip().upper()

all_codons = []

# For each gene, find the longest ORF stop codon position and get all in-frame codons upstream of it. Then count the occurrences of each codon and plot a pie chart.
for header, seq in genes.items():
    pos = find_longest_orf_stop(seq, target)
    if pos == -1:
        continue
    codons = get_upstream_codons(seq, pos)
    all_codons.extend(codons)

# Caculate the frequency of each codon
count = {}
for c in all_codons:
    count[c] = count.get(c, 0) + 1

# Output the results
print("\nCodon counts upstream of", target)
for codon, num in sorted(count.items()):
    print(f"{codon}: {num}")

# 3. Plot a pie chart of the codon distribution
labels = list(count.keys())
sizes = list(count.values())

plt.figure(figsize=(10, 10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title(f"Codon Distribution upstream of {target}")
plt.savefig("codon_pie.png")
plt.close()

print("\nPie chart saved as codon_pie.png")
