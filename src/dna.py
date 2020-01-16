transcription = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}

def dna_to_rna(dna):
    rna = ''
    for letter in dna:
        rna += transcription[letter]
    return rna

def validate_dna(dna):
    return set(dna).issubset('GCTA')

def main():
    while True:
        my_dna = input('Type DNA sequence: ')
        if not validate_dna(my_dna):
            answer = input('Invalid DNA sequence, try again (y/n)? ')
            if answer.lower() != 'y':
                break
            continue
        rna = dna_to_rna(my_dna)
        print(f'Transcribed RNA: {rna}')
        return


if __name__ == '__main__':
    # print(dna_to_rna('GCTA'))
    main()