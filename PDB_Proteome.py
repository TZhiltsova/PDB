from pyfaidx import Fasta

proteome_seq = {}
with Fasta('Amyloid_Proteome.fasta') as genes:
    n = 0
    for record in genes:
        line = '>' + record.long_name
        proteome_seq[line] = genes[n][:]
        n += 1

pdb_seq = {}
with Fasta('pdb_amyloid.fasta') as genes:
    n = 0
    for record in genes:
        line = '>' + record.long_name
        pdb_seq[line] = genes[n][:]
        n += 1

proteome_seq_filter = {}
pdb_seq_filter = {}
for key, val in proteome_seq.items():
    for key_pdb, val_pdb in pdb_seq.items():
        if len(val) >= len(val_pdb):
            if str(val_pdb) in str(val):
                proteome_seq_filter[key] = val
                pdb_seq_filter[key_pdb] = val_pdb

with open('pdb_proteome.fasta', 'w') as short:
    for key, val in proteome_seq_filter.items():
        short.write(key + '\n')
        short.write(str(val) + '\n')


with open('pdb_proteome2.fasta', 'w') as short:
    for key, val in pdb_seq_filter.items():
        short.write(key + '\n')
        short.write(str(val) + '\n')

