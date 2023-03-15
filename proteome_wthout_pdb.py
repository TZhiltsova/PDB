from pyfaidx import Fasta

proteome_seq = {}
with Fasta('Amyloid_Proteome.fasta') as genes:
    n = 0
    for record in genes:
        line = '>' + record.long_name
        proteome_seq[line] = genes[n][:]
        n += 1

pdb_seq = []
with Fasta('pdb_proteome.fasta') as genes:
    n = 0
    for record in genes:
        line = '>' + record.long_name
        pdb_seq.append(line)

proteome_seq_filter = {}
for key, val in proteome_seq.items():
    if key not in pdb_seq:
        proteome_seq_filter[key] = val

with open('proteome_without_pdb.fasta', 'w') as short:
    for key, val in proteome_seq_filter.items():
        short.write(key + '\n')
        short.write(str(val) + '\n')
