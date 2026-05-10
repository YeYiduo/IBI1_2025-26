import re
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"
stops = {"TAA", "TAG", "TGA"}
genes = {}
current_header = None
current_seq = []
# Read the FASTA file and store gene sequences
with open(input_file, 'r', encoding='latin-1') as infile:
    for line in infile:
        line = line.strip()
        if line.startswith('>'):
            if current_header and current_seq:
                genes[current_header] = ''.join(current_seq)
            current_header = line
            current_seq = []
        else:
            current_seq.append(line)
    if current_header and current_seq:
        genes[current_header] = ''.join(current_seq)

# Function: Find all in-frame stop codons in a sequence (without duplicates, find all)
def find_all_in_frame_stops(seq):
    found = set()
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon in stops:
            found.add(codon)
    return sorted(found) if found else None

# Extract gene name from header (remove '>' and take the first word)
def extract_gene_name(header):
    return header.lstrip(">").split()[0]

# For each gene, find all in-frame stop codons and write to output file    
with open(output_file, 'w', encoding='utf-8') as outfile:
    for header, seq in genes.items():
        # Only process genes that start with ATG
        if not seq.startswith("ATG"):
            continue
            
        stop_list = find_all_in_frame_stops(seq)
        
        # If there are stop codons, write the gene name, stop codons, and sequence to the output file
        if stop_list:
            gene_name = extract_gene_name(header)
            # Header: >gene_name stop1,stop2,...  
            outfile.write(f">{gene_name} {','.join(stop_list)}\n")
            # Sequence: Complete gene sequence
            outfile.write(f"{seq}\n")
