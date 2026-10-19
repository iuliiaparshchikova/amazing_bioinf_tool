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
    return path
