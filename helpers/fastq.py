import os


def read_fastq(path):
    """
    Take a path of fastq-file and return list of all reads as a list
    """
    reads = []
    with open(path) as file:
        while True:
            name = file.readline().strip()
            if name == "":
                break
            seq = file.readline().strip()
            plus = file.readline().strip()
            qual = file.readline().strip()
            reads.append((name, seq, plus, qual))
    return reads


def make_output_path(output_fastq, folder="filtered"):
    """
    Create folder and return path to output file
    """
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, output_fastq)
    open(path, "w").close()
    return path


def gc_cont(reads):
    """
    Calculate the GC content of each read
    """
    n = 0
    for i in reads:
        if i.upper() == "G" or i.upper() == "C":
            n += 1
    return n / len(reads) * 100


def bounds(bounds, seq):
    """
    Filter based on GC-content
    """
    if isinstance(bounds, tuple):
        low_bound = bounds[0]
        high_bound = bounds[1]
    else:
        low_bound = 0
        high_bound = bounds
    return low_bound <= gc_cont(seq) <= high_bound


def length(seq, length_bounds):
    """
    Check if length is okay
    """
    if isinstance(length_bounds, tuple):
        low_bound = length_bounds[0]
        high_bound = length_bounds[1]
    else:
        low_bound = 0
        high_bound = length_bounds
    return low_bound <= len(seq) <= high_bound


def quality(qual, quality_threshold):
    """
    Check if quality is okay
    """
    mean_qual = 0
    total = 0
    for i in qual:
        total += ord(i) - 33
    mean_qual = total / len(qual)
    return mean_qual >= quality_threshold


def write_read(path, read):
    """
    Append one read to the file
    """
    with open(path, "a") as file:
        file.write("\n".join(read) + "\n")
