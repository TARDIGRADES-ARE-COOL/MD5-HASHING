import hashlib

plaintexts = [
    "Pancakes",
    "hello",
    "potatoe",
    "cybersecurity",
    "singaporeuniversityoftechnologyanddesign"
]

for text in plaintexts:
    # 1) encode the string to bytes
    b = text.encode('utf-8')
    # 2) hash and get hex digest
    digest = hashlib.md5(b).hexdigest()
    x = len(digest)
    # 3) print it
    print(f"{text} → {digest}; length is {x}" )



# Answer the following questions in your report:
# • How does the length of the hash correspond to the input string?
# • Are there any visible correlations between the hash and the input string?
# • What are the issues related to the cryptographic weakness of MD5?