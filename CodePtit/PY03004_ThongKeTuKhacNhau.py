from collections import defaultdict
import re

word = defaultdict(int)

for _ in range(int(input())):
    s = input().strip()
    words = re.findall(r'\b\w+\b', s)
    for tu in words:
        tu = tu.lower()
        word[tu] += 1

sorted_word = sorted(word.items(), key=lambda x: (-x[1], x[0]))

for w, c in sorted_word:
    print(f"{w} {c}")
