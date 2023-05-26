def calculate_gc_content(dna_sequence):
    total_length = len(dna_sequence)
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    gc_content = (gc_count / total_length) * 100
    return gc_content

def find_sequence_with_highest_gc(file_path):
    sequences = {}
    current_sequence_id = ''
    current_sequence = ''

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_sequence_id != '':
                    sequences[current_sequence_id] = current_sequence
                    current_sequence = ''
                current_sequence_id = line[1:]
            else:
                current_sequence += line

        # Add the last sequence to the dictionary
        sequences[current_sequence_id] = current_sequence

    highest_gc_id = ''
    highest_gc_content = 0.0

    for sequence_id, sequence in sequences.items():
        gc_content = calculate_gc_content(sequence)
        if gc_content > highest_gc_content:
            highest_gc_id = sequence_id
            highest_gc_content = gc_content

    return highest_gc_id, highest_gc_content


file_path = 'rosalind_gc.txt'  
result = find_sequence_with_highest_gc(file_path)
print(result[0])
print( result[1])
