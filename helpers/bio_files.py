import os


def read_fasta(path):
    """
    Read fasta file
    """
    seqs = {}
    header = None
    with open(path) as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            if line.startswith(">"):
                header = line
                seqs[header] = ""
            else:
                seqs[header] += line
    return seqs


def write_fasta(path, seqs):
    """
    Write dict to a fasta file
    """
    with open(path, "w") as file:
        for header, seq in seqs.items():
            file.write(header + "\n")
            file.write(seq + "\n")


def make_oneline_name(input_fasta):
    """
    Make output name
    """
    name, ext = os.path.splitext(input_fasta)
    res = name + "_oneline" + ext
    return res


def get_hits(path):
    """
    Read BLAST output and return first description
    """
    hits = []
    in_table = False
    with open(path) as file:
        for line in file:
            if line.startswith("Sequences producing significant alignments"):
                in_table = True
            elif in_table and line.startswith("Description"):
                best = next(file)
                hits.append(best.split("  ")[0].strip())
                in_table = False
    return hits


def write_col(path, items):
    """
    Write unique items to a file
    """
    with open(path, "w") as file:
        for item in sorted(set(items)):
            file.write(item + "\n")
