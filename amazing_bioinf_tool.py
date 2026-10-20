from helpers.fastq import (
    bounds,
    length,
    make_output_path,
    quality,
    read_fastq,
    write_read,
)


def filter_fastq(
    input_fastq,
    output_fastq,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold=0,
):
    """
    Filter reads from a FASTQ file
    """
    output_path = make_output_path(output_fastq)
    for read in read_fastq(input_fastq):
        name, seq, plus, qual = read
        if (
            bounds(gc_bounds, seq)
            and length(seq, length_bounds)
            and quality(qual, quality_threshold)
        ):
            write_read(output_path, read)


from helpers.bio_files import (
    make_oneline_name,
    read_fasta,
    write_fasta,
)


def convert_multiline_fasta_to_oneline(input_fasta, output_fasta=None):
    """
    Save fasta file where every sequence is written in one line
    """
    if output_fasta is None:
        output_fasta = make_oneline_name(input_fasta)
    seqs = read_fasta(input_fasta)
    write_fasta(output_fasta, seqs)


from helpers.bio_files import (
    get_hits,
    write_col,
)


def parse_blast_output(input_file, output_file):
    """
    Take hits from BLAST and save them into a file
    """
    hits = get_hits(input_file)
    write_col(output_file, hits)
