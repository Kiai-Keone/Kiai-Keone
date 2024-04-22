import urllib.request
import re

url = "https://www.gutenberg.org/cache/epub/11/pg11-images.html"
destination_filename = "alice_words.txt"
urllib.request.urlretrieve(url, destination_filename)

count = {}

with open(destination_filename, 'r', encoding='utf-8') as f:
    for line in f:
        cleaned_line = re.sub(r'<[^>]+>', ' ', line)
        words = cleaned_line.strip().split()
        
        for word in words:
            word = re.sub(r'[^A-Za-z]', '', word).lower()
            if word:
                count[word] = count.get(word, 0) + 1

sorted_count = sorted(count.items())

print("Word              Count")
print("=======================")

for word, freq in sorted_count:
    print(f"{word.ljust(18)}{freq}")

print("The word 'alice' appears " + str(count['alice']) + " times in the book.")
