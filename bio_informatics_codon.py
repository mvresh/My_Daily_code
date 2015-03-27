dic = {'A':'T','T':'A','G':'C','C':'G'}
string = raw_input('give sequence')
new = ''
for char in string:
    if char in dic.keys():
        new += dic[char]
    else: new += ' ERROR '



codon = {'TTT':'PHE', 'TTC':'PHE', 'TTA':'LEU','TTG':'LEU','CTT':'LEU','CTC':'LEU',
         'CTA':'LEU','CTG':'LEU','ATT':'LLE','ATC':'LLE','ATA':'LLE','ATG':'MET',
         'GTT':'VAL','GTC':'VAL','GTA':'VAL','GTG':'VAL','TCT':'SER','TCC':'SER',
         'TCA':'SER','TCG':'SER','CCT':'PRO','CCC':'PRO','CCA':'PRO','CCG':'PRO',
         'ACT':'THR','ACC':'THR','ACA':'THR','ACG':'THR','GCT':'ALA','GCC':'ALA',
         'GCA':'ALA','GCG':'ALA','TAT':'TYR','TAC':'TYR','TAA':'STOP','TAG':'STOP',
         'CAT':'HIS','CAC':'HIS','CAA':'GLN','CAG':'GLN','AAT':'ASN','AAC':'ASN',
         'AAA':'LYS','AAG':'LYS','GAT':'ASP','GAC':'ASP','GAA':'GLU','GAG':'GLU',
         'TGT':'CYS','TGC':'CYS','TGA':'STOP','TGG':'TRP','CGT':'ARG','CGC':'ARG',
         'CGA':'ARG','CGG':'ARG','AGT':'SER','AGC':'SER','AGA':'ARG','AGG':'ARG',
         'GGT':'GLY','GGC':'GLY','GGA':'GLY','GGG':'GLY'}


bonus, result =[], ''
for char in range(0,len(string),3):
    bonus.append(string[char:char+3])

for item in bonus:
    if item in codon:
        result += codon[item]
        result += ' '



print string
print new
print result
