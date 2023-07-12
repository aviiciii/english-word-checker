# read json

import json
import nltk
from nltk.corpus import words
import ssl

# SSL certificate error fix
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Load the English word corpus from NLTK
nltk.download('words')
word_list = words.words()

def is_valid_word(word):
    # Convert the word to lowercase for case-insensitive matching
    word = word.lower()
    if word in word_list:
        return True
    else:
        return False

# Read the JSON file
with open('data.json') as f:
    data = json.load(f)

words_to_check = data['words']

valid = 0
invalid=[]
total = len(words_to_check)
for word in words_to_check:
    if is_valid_word(word):
        valid += 1
    else:
        invalid.append(word)
    
print("Invalid words: " + str(total - valid))
print("Valid words: " + str(valid))
print("Total words: " + str(total))

with open('invalid.json', 'w') as outfile:
    json.dump(invalid, outfile)
