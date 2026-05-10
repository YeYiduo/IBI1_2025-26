import re
seq =  'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
# Store all valid ORFs
orfs = []
# Check 3 reading frames
for frame in range(3):
    # Start from the current frame, split every 3 characters
    for match in re.finditer(r'AUG', seq[frame:]):
        start = match.start() + frame
        # From start, search in steps of 3 until a stop codon is found
        for i in range(start, len(seq), 3):
            codon = seq[i:i+3]
            if codon in {'UAA', 'UAG', 'UGA'}:
                orf = seq[start:i+3]
                orfs.append(orf)
                break
# Find the longest ORF
longest_orf = max(orfs, key=len)
length = len(longest_orf)
print("Longest ORF:", longest_orf)
print("Length:", length)
