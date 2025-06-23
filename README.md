# MD5 Hashing and Cracking

**👤 Name:** Sarvesh Joaquim Gopu


This lab explores hashing, brute-force attacks, salting, and cracking MD5 hashes to demonstrate weaknesses and attack strategies.

---

## 📅 Tasks Overview

### ✅ Part 1: MD5 Hashing

We computed MD5 hashes for strings of different lengths using both shell and Python.

#### Python Example:

```python
import hashlib
hashlib.md5("Pancakes".encode()).hexdigest()
```

#### Shell:

```bash
echo -n "foobar" | md5sum
```

#### Questions & Answers:

* **How does the length of the hash correspond to the input string?**
  Always 32 characters, regardless of input size.

* **Are there any visible correlations between the hash and the input string?**
  None visible; all hashes appear as random hex strings (limited to a-f, 0-9).

* **Issues with MD5?**
  It's cryptographically broken: easy to generate collisions, vulnerable to length-extension attacks, fast enough for brute-force/rainbow tables. Should be replaced by SHA-256, bcrypt, etc.

---

### ✅ Part 2: Brute-Force Cracking MD5 Hashes

Cracked 15 unsalted MD5 hashes from `hash5.txt`. All were 5-character strings (lowercase alphanumeric).

**Script Used:** `ex2.py`
**Output File:** `ex2_hash.txt`

#### Summary:

* **Total Time:** 19.25 seconds
* **Average Time per Hash:** \~1.28 seconds

#### Optimization:

* Used a loop to generate all 36^5 combinations.
* Improved performance by computing hashes once and storing in memory for comparison.

#### Sample Output:

```
found aseas in 0.49 seconds
found cance in 1.47 seconds
...
found tthel in 0.11 seconds
```

#### Q\&A:

* **Can brute force be amortized?**
  Yes. By generating all combinations once and storing them (e.g. in a set), future checks are faster.

---

### ✅ Part 3: Salted Hash Cracking

Salt was applied by adding a single lowercase character to each original password. We then hashed and cracked again.

**Salt Used:** `'j'`

**Scripts:**

* `ex3.py` (cracking salted hashes)
* `salted6.txt` (output salted hashes)
* `plain6.txt` (plaintext + salt)
* `recovered6.txt` (cracked results)

#### Summary:

* **Salted Crack Time:** 15.40 seconds
* **Unsalted Crack Time:** 19.25 seconds
* **Speedup:** Preloading hashes into a set for constant-time lookup.

#### Strategy:

* Pre-created all salted variants
* Used fast hash comparison via Python sets
* No need to scan lists per attempt

#### Sample Output:

```
Found: aseasj -> ... in 0.41s
Found: cancej -> ... in 1.19s
...
All cracked in 15.40 seconds
```

#### Q\&A:

* **Ease of salted vs unsalted cracking?**
  Salted was faster in this case due to better data structures.

* **Why the speed difference?**
  Salted hashes were preprocessed and stored in a set, improving lookup speed.

---

## 🚀 How to Run

```bash
python3 part1.py         # Generate example hashes
python3 ex2.py           # Crack unsalted hashes
python3 ex3.py           # Crack salted hashes
```

---

## 📚 Submission Format

```
lab3_sarvesh_1008107.zip
```

**Include:**

* `part1.py`
* `ex2.py`
* `ex2_hash.txt`
* `ex3.py`
* `salted6.txt`
* `plain6.txt`
* `recovered6.txt`
* `report.ipynb`

Deadline: **22 June 2025, 11:59PM**

---

## 📈 Summary Table

| Task                 | Description                | Time Taken |
| -------------------- | -------------------------- | ---------- |
| MD5 Hashing          | Static 32-character output | --         |
| Brute-force Cracking | 15 unsalted hashes         | 19.25s     |
| Salted Hash Cracking | With salt = 'j'            | 15.40s     |

> ✅ **Lesson:** MD5 is insecure alone. Salt helps, but a slow, modern KDF is best.
