from typing import List, Tuple
def custom_zip(*sequences, full=False, default=None) -> List[Tuple]:
    # Find the length of the shortest or longest iterable based on the 'full' parameter
    if full:
        max_length = max(len(seq) for seq in sequences)
        zipped_sequences = [
            tuple(seq[i] if i < len(seq) else default for seq in sequences)
            for i in range(max_length)
        ]
    else:
        min_length = min(len(seq) for seq in sequences)
        zipped_sequences = [tuple(seq[i] for seq in sequences) for i in range(min_length)]
    return zipped_sequences
seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
print(custom_zip(seq1, seq2))
print(custom_zip(seq1, seq2, full=True, default="Q"))