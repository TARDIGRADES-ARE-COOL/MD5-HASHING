#!/usr/bin/env python3
import hashlib
import itertools
import string
import time
import os

final = []
avgtime = []
here = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(here, 'hash5.txt')

with open(path, 'r') as f:
    hashes = [line.strip() for line in f if line.strip()]

# all the possible characters of length 5
chars = string.ascii_lowercase + string.digits 

# start timing
start = time.time()
last_time = start

for combo in itertools.product(chars, repeat=5):
    plaintext = ''.join(combo)
    digest = hashlib.md5(plaintext.encode()).hexdigest()
    if digest in hashes and plaintext not in final:
        final.append(plaintext)
        now = time.time()
        interval = now - last_time
        avgtime.append(interval)
        total_elapsed = now - start
        print(f"found {plaintext} in {interval:.2f} seconds (total {total_elapsed:.2f}s)")
        last_time = now
        if len(final) == len(hashes):
            print("found all i think please check")
            break

def avgt(avgtime):
 return sum(avgtime) / len(avgtime) 

# stop timing & report overall
end = time.time()
print(f"Time taken overall: {end - start:.2f} seconds")
print(avgt(avgtime))


# write all recovered plaintexts in sequence to ex2_hash.txt
output_path = os.path.join(here, 'ex2_hash.txt')
with open(output_path, 'w') as outfile:
    for pt in final:
        outfile.write(pt + '\n')

