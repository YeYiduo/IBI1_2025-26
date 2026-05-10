import re
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
largest_orf = max(re.findall(r"AUG(?:...)*(?:UAA|UAG|UGA)", seq), key=len)
largest_orf_length = len(largest_orf)
print("Largest ORF: " ,largest_orf)
print("Length: " + str(largest_orf_length))