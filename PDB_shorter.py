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
