"""
FASTQ Quality Analysis

Reads a FASTQ file and calculates:
- Per-read GC content
- Per-base Phred quality scores
- Mean Phred quality score for each read
- Minimum, maximum and average read length
- Overall GC content
"""

def read_fastq(path):
    """
    Reads a FASTQ file one record at a time
    Yields: header, sequence, quality string
    
    """
    with open(path) as fh:
        while True:
            header = fh.readline().strip()
            if not header:
                break 
            seq = fh.readline().strip()
           # Skip the separator line present in FASTQ records
            fh.readline() 
            qual = fh.readline().strip()
            yield header, seq, qual

min_read_length = float("inf")
max_read_length = 0
num_reads = 0
total_read_length = 0
gc_total = 0

quality_scores = {}
average_quality  = {}

for header, seq, qual in read_fastq("sample.fastq"):
    
    # Calculate statistics for the current read.
    read_length = len(seq)
    gc_count = seq.count("G") + seq.count("C")
    gc_percent = gc_count / read_length * 100
    
    print(
    f"Sequence : {seq}\n"
    f"Quality  : {qual}\n"
    f"GC (%)   : {gc_percent:.2f}\n"
    )
    
    # Update cumulative statistics    
    total_read_length += read_length
    num_reads += 1
    gc_total += gc_count
    
    min_read_length = min(min_read_length, read_length)
    max_read_length = max(max_read_length, read_length)
    
    quality = [ord(char) - 33 for char in qual]

    quality_scores[header] = quality
    average_quality[header] = round(sum(quality) / len(quality) ,2)
    
print(quality_scores)
print(average_quality)

print(f"Minimum read length: {min_read_length}")
print(f"Maximum read length: {max_read_length}")
print(f"Average read length: {total_read_length/num_reads:.2f}")
print(f"Overall GC content: {gc_total / total_read_length * 100:.2f}%")





