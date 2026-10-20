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
