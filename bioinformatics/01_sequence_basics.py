# Beginner Bioinformatics Practice

# Problem 1 — GC Content Calculator Write a script that calculates the GC content of a DNA sequence.
# Count how many nucleotides are G or C and compute the GC%  Print the result rounded to 2 decimal places.

seq = "ATGCGCGTA"
count = 0
for i in range(0,len(seq)):
    if seq[i] == "G" or seq[i] =="C":
        count = count + 1
print("GC Content: ", round((count / len(seq)) * 100,2), "%")

# Problem 2 — DNA → RNA Transcription
# Write a script that converts a DNA sequence into RNA. Replace every thymine (T) with uracil (U).
seq1="ATGCTTAC"
seq1RNA =""
for i in range(0,len(seq1)):
    if seq1[i] == "T":
        seq1RNA += "U"
    else:
        seq1RNA += seq1[i]
print(seq1RNA)

# Problem 3 — Reverse Complement of DNA
# Write a script that finds the reverse complement of a DNA sequence.
seqComp =""
for i in range(0,len(seq)):
    if seq[i] == "T":
        seqComp += "A"
    elif seq[i] == "A":
         seqComp += "T"
    elif seq[i] == "G":
        seqComp += "C"
    elif seq[i] == "C":
        seqComp += "G"
seqComp= seqComp[::-1]
print(seqComp)

# Problem 4 — Sequence Length Statistics
# Given a list of DNA sequences, compute: The Longest sequence length, Shortest sequence length, and Average sequence length
seqlist = ["ATG","ATGCTAG","AT"]
sumseq = 0
minseq = float("inf")
maxseq = float("-inf")
for i in range(0,len(seqlist)):
    sumseq = sumseq + len(seqlist[i])
    if len(seqlist[i]) < minseq:
        minseq = len(seqlist[i])
    elif len(seqlist[i]) > maxseq:
        maxseq = len(seqlist[i])
print("Max Sequence Lengthis:", maxseq)
print("Min Sequence Lengthis:", minseq)
print("AVG Sequence Lengthis:", sumseq/len(seqlist))