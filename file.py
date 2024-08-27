import re
from collections import defaultdict
import os

def count_word_occurrences(file_path):
    if not os.path.isfile(file_path):
        print(f"No file exists with the name: {file_path}")
        return

    word_count = defaultdict(int)

    # Open and read the file
    with open(file_path, 'r') as file:
        text = file.read()

        # Convert to lowercase and remove punctuation
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)

        # Split the text into words
        words = text.split()

        # Count the occurrences of each word
        for word in words:
            word_count[word] += 1

    # Sort the word count dictionary alphabetically by word
    sorted_word_count = dict(sorted(word_count.items()))

    # Display the results
    print("Word Occurrences:")
    for word, count in sorted_word_count.items():
        print(f"{word}: {count}")

# Example usage:
file_path = input("Enter the name of the file to analyze: ")
count_word_occurrences(file_path)
