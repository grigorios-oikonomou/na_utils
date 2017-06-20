"""
Convert DNA sequences to RNA.
"""

def rna(seq):
    """ Convert DNA to RNA."""
    # Determine if original is in uppercase
    seq_upper = seq.isupper()

    # Make all to lowercase
    seq = seq.lower()

    # Swap out t for u:
    seq = seq.replace('t', 'u')

    # Return upper or lower, depending on input

    if seq_upper:
        return seq.upper()
    else:
        return seq


def reverse_rna_complement(seq):
    """
    DNA into rc RNA
    """

    # Determine if original is in uppercase
    seq_upper = seq.isupper()

    # Reverse seq
    seq = seq[::-1]

    # Convert to uppercase
    seq = seq.upper()

    # Compute complement
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')

    # Return
    if seq_upper:
        return seq.upper()
    else:
        return seq 
