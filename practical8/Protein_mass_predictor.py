aa_mass = {
    'G': 57.02,
    'A': 71.04,
    'S': 87.03,
    'P': 97.05,
    'V': 99.07,
    'T': 101.05,
    'C': 103.01,
    'I': 113.08,
    'L': 113.08,
    'N': 114.04,
    'D': 115.03,
    'Q': 128.06,
    'K': 128.09,
    'E': 129.04,
    'M': 131.04,
    'H': 137.06,
    'F': 147.07,
    'R': 156.10,
    'Y': 163.06,
    'W': 186.08}
def calculate_mass(protein_sequence):
    total_mass = 0.0
    for aa in protein_sequence:
        if aa in aa_mass:
            total_mass += aa_mass[aa]
        else:
            print(f"Warning: Amino acid '{aa}' not recognized. Skipping.")
    return total_mass
# Example usage
protein_seq = "ACDEFGHIKLMNPQRSTVWY"
mass = calculate_mass(protein_seq)
print(f"The mass of the example protein sequence '{protein_seq}' is: {mass:.2f} Da")

# Allow user input for protein sequence
input_seq = input("Enter a protein sequence: ")
mass = calculate_mass(input_seq)
print(f"The mass of the protein sequence '{input_seq}' is: {mass:.2f} Da") 
