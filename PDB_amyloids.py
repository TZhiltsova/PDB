waltz_seq = []       # list for short motifs of amyloid
waltz_dict = {}      # dictionary for sequences from WaltzDB
with open('WALTZ_DB_amyloid_seq') as waltz_db:
    for line in waltz_db:
        waltz_seq = [line.strip() for line in waltz_db]
    for number, amiloid_motif in enumerate(waltz_seq):
        if amiloid_motif.strip().isalpha() == False:    # deleting empty lines
            break
        else:
            waltz_dict[number] = amiloid_motif

m = 0
pdb_new_list = {}
with open('pdb_seqres.txt') as pdb:
    for line in pdb:
        line.replace('\n', '')
        if '>' in line:
            if 'protein' in line:
                m += 1
                key = line
                continue
        if m == 1:
            m = 0
            pdb_new_list[key] = line
with open('pdb_short.txt', 'w') as short:
    for key, val in pdb_new_list.items():
        short.write(key)
        short.write(val)

filter_seq = {}  # dict for seq that have amyloid-forming regions
for key, seq in pdb_new_list.items():
    for val in waltz_dict.values():
        if val in str(seq):
            filter_seq[key] = seq

filter_seq2 = {}
for key, seq in filter_seq.items():
    filter_seq2[seq] = key

with open('pdb_amyloid.fasta', 'w') as short:
    for key, val in filter_seq2.items():
        short.write(val)
        short.write(key)
