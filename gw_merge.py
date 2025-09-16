#!/usr/bin/env python3
# aMiscreant

import glob

output_file = "wordlist_clean.txt"
all_lines = set()  # using a set to automatically deduplicate

# Find all .txt files in the current directory
for filename in glob.glob("*.txt"):
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if line:  # skip empty lines
                all_lines.add(line)

# Sort all lines
sorted_lines = sorted(all_lines)

# Write to output
with open(output_file, "w", encoding="utf-8") as f:
    for line in sorted_lines:
        f.write(line + "\n")

print(f"[+] Combined {len(sorted_lines)} unique lines into {output_file}")
