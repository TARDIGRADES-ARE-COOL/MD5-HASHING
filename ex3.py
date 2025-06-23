#!/usr/bin/env python3
import hashlib
import itertools
import string
import time
import os

# ——— Part I: generate salted6.txt and plain6.txt ———

# to store new plaintext 
new_plaintext = []
new_hash      = []

# read your recovered ex2 plaintexts
original = open('ex2_hash.txt','r').read().splitlines()

# append the salt character to each
for i in original:
    new_plaintext.append(i + 'j')

# hash each salted plaintext
for text in new_plaintext:
    b      = text.encode('utf-8')
    digest = hashlib.md5(b).hexdigest()
    new_hash.append(digest)

# write salted hashes
with open('salted6.txt', 'a') as outf:
    outf.write('The salted value is j\n')
    for h in new_hash:
        outf.write(h + '\n')

# write salted plaintexts
with open('plain6.txt', 'a') as outf:
    for pt in new_plaintext:
        outf.write(pt + '\n')


# ——— Part II: brute-force reverse the salted hashes ———

def main():
    here        = os.path.dirname(os.path.realpath(__file__))
    salted_path = os.path.join(here, 'salted6.txt')

    # read salt and target hashes
    with open(salted_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    # extract salt and hashes
    salt    = lines[0].split()[-1]     # 'j'
    targets = set(lines[1:])           # MD5 digests

    print(f"Using salt = '{salt}' to crack {len(targets)} hashes…")
    chars = string.ascii_lowercase + string.digits

    found     = {}                     # digest -> salted plaintext
    start     = time.time()
    last_time = start

    for combo in itertools.product(chars, repeat=5):
        core   = ''.join(combo)            # e.g. "aseas"
        salted = core + salt               # e.g. "aseasj"
        digest = hashlib.md5(salted.encode()).hexdigest()

        if digest in targets and digest not in found:
            found[digest] = salted
            now      = time.time()
            delta    = now - last_time
            total    = now - start
            last_time = now

            print(
                f"Found: {salted} -> {digest} "
                f"in {delta:.2f}s (total {total:.2f}s) "
                f"({len(found)}/{len(targets)})"
            )

            if len(found) == len(targets):
                break

    overall = time.time() - start
    print(f"\nAll cracked in {overall:.2f} seconds")


if __name__ == '__main__':
    main()
