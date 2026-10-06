"""
screen.py

A simple k-mer based screening baseline.

This is a transparent, local stand-in for provider screening systems.
It is intended for methodological evaluation, not as a measurement of
any commercial tool.
"""

KMER_SIZE = 20
MIN_MATCHES = 1


def build_kmer_index(reference_sequences, kmer_size: int = KMER_SIZE) -> set:
    """Build a set of k-mers from all reference sequences."""
    kmers = set()
    for seq in reference_sequences:
        seq = seq.upper()
        for i in range(len(seq) - kmer_size + 1):
            kmers.add(seq[i:i + kmer_size])
    return kmers


def screen(sequence: str, kmer_index: set,
           kmer_size: int = KMER_SIZE,
           min_matches: int = MIN_MATCHES) -> bool:
    """
    Return True if the sequence shares at least min_matches k-mers
    with the reference index.
    """
    seq = sequence.upper().replace("N", "")
    matches = 0
    for i in range(len(seq) - kmer_size + 1):
        if seq[i:i + kmer_size] in kmer_index:
            matches += 1
            if matches >= min_matches:
                return True
    return False


def screen_many(sequences, kmer_index) -> list:
    """Return a list of (sequence, detected) tuples."""
    return [(seq, screen(seq, kmer_index)) for seq in sequences]
