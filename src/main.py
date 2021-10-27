from Bio import SeqIO
import re


def calculateGaps(record):
    matches = re.findall(r'[N]+', str(record.seq))
    N_repetitions = str(record.seq).count('N')
    print(f'\tGaps in total: {len(matches)}')
    print(f'\tGap symbols in total: {N_repetitions}')
    print(f'\tCheck: {sum(len(c) for c in matches)} == {N_repetitions}')


def getRecords(records):
    total = sum(len(record) for record in records)
    longest = len(records[0])
    score = 0
    n_50 = 0
    ind = 0
    while(score < total/2):
        n_50 = len(records[ind])
        ind += 1
        score += n_50
    print(f'\tTotal length: {total}')
    print(f'\tThe longest contig size: {longest}')
    print(f'\tN50: {n_50}')


contigs = list(SeqIO.parse("Poil_contig.fa", "fasta"))
scaffolds = list(SeqIO.parse("out_scaffold.fa", "fasta"))
gaps = list(SeqIO.parse("out_gapClosed.fa", "fasta"))
contigs.sort(key=lambda r: -len(r))
scaffolds.sort(key=lambda r: -len(r))
gaps.sort(key=lambda r: -len(r))

SeqIO.write([scaffolds[0]], 'longest.fa', "fasta")

print(f'============ contigs: {len(contigs)} ===============')
getRecords(contigs)

print(f'\n============ scaffold: {len(scaffolds)} ===============')
getRecords(scaffolds)

print(f'\n============ scaffold longest  ===============')
calculateGaps(scaffolds[0])

print(f'\n============ gap closed ===============')
calculateGaps(gaps[0])
