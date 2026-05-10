import re

input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"
stops = {"TAA", "TAG", "TGA"}

genes = {}
current_header = None
current_seq = []

# 读取FASTA，拼接完整序列
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

# 函数：找到序列里 所有 框内终止密码子（不去重，全部找）
def find_all_in_frame_stops(seq):
    found = set()
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon in stops:
            found.add(codon)
    return sorted(found) if found else None

# 提取基因名
def extract_gene_name(header):
    return header.lstrip(">").split()[0]

# 输出：完全符合要求
with open(output_file, 'w', encoding='utf-8') as outfile:
    for header, seq in genes.items():
        # 必须以 ATG 开头才是有效ORF
        if not seq.startswith("ATG"):
            continue
            
        stop_list = find_all_in_frame_stops(seq)
        
        # 只有找到终止密码子才输出
        if stop_list:
            gene_name = extract_gene_name(header)
            # 标题：基因名 + 所有终止密码子逗号分隔
            outfile.write(f">{gene_name} {','.join(stop_list)}\n")
            # 序列：完整基因序列
            outfile.write(f"{seq}\n")