""" Generate a synthetic FASTQ file for parsing and sequence analysis """

import random

def main(n_reads=10000, min_len=100, max_len=150, out="sample.fastq"):
    with open(out, "w") as fh:
        for i in range(n_reads):
            length = random.randint(min_len, max_len)
            seq = "".join(random.choice("ACGT") for _ in range(length))
            qual = "".join(chr(random.randint(35, 73)) for _ in range(length))
            fh.write(f"@read_{i}\n{seq}\n+\n{qual}\n")
    print(f"Wrote {n_reads} reads to {out}")

if __name__ == "__main__":
 main()
