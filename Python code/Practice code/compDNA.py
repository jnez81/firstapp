def DNA_strand(dna):
    if dna in 'A':
        return 'T'
    elif dna in 'T':
        return 'A'
    
    if dna in 'C':
        return 'G'
    elif dna in 'G':
        return 'C'