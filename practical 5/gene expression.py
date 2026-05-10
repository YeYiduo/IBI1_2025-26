dictionary = {"TP53":12.4, "EGFR":15.1, "BRCA1":8.2, "PTEN":5.3, "ESR1":10.7}
for gene, expression in dictionary.items():
    print(f"{gene}: {expression}")  
dictionary["MYC"] = 11.6
import numpy as np
import matplotlib.pyplot as plt
N=6
x = np.arange(N)
y = list(dictionary.values()) 
plt.bar(x, y)
plt.xticks(x, list(dictionary.keys()))    
plt.xlabel('Genes')
plt.ylabel('Expression Levels')     
plt.title('Gene Expression Levels')
plt.show()      

# --------------------------
# ↓↓↓ Target gene (modify as needed) ↓↓↓
gene_of_interest = "BRCA1"  # Update this to the gene you want to query
# ↑↑↑ Target gene (modify as needed) ↑↑↑
# --------------------------
if gene_of_interest in dictionary:
    print(f"The expression level of {gene_of_interest} is: {dictionary[gene_of_interest]}")
else:    print(f"{gene_of_interest} is not found in the dictionary.")   

avg_expression = sum(dictionary.values()) / len(dictionary)
print(f"The average expression level across all genes is: {avg_expression:.2f}")