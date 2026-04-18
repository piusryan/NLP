# -*- coding: utf-8 -*-


from nltk.stem import PorterStemmer

# Initialize the stemmer
stemmer = PorterStemmer()

# Example words
words = ["running", "runner", "runs", "easily", "happier", "better"]

# Apply stemming
stemmed_words = [stemmer.stem(word) for word in words]

print(stemmed_words)

import nltk
nltk.download('wordnet')

"""Lemmatization"""

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Example words
words = ["running", "runner", "runs", "easily", "happier", "better"]

# Apply lemmatization (using verb as default)
lemmatized_words = [lemmatizer.lemmatize(word, pos=wordnet.VERB) for word in words]

print(lemmatized_words)

import nltk
nltk.download('punkt_tab')

"""Morphological Analysis Using NLTK's"""

from nltk.tag import RegexpTagger
from nltk.tokenize import word_tokenize

# Example sentence
sentence = "The cats were running quickly."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Define a simple regular expression pattern for morphological tagging
patterns = [
    (r'.*ing$', 'VB'),    # Verbs ending in 'ing'
    (r'.*ly$', 'RB'),     # Adverbs ending in 'ly'
    (r'.*es$', 'NNS'),    # Nouns ending in 'es'
]

# Create a tagger
tagger = RegexpTagger(patterns)

# Apply the tagger to the tokens
tagged_tokens = tagger.tag(tokens)

print(tagged_tokens)

"""WordNet for Morphological Analysis"""

from nltk.corpus import wordnet

# Ensure WordNet data is downloaded
nltk.download('wordnet')

# Get synsets for the word "running"
synsets = wordnet.synsets('running')

# Print the first synset and its lemma names
print(synsets[0].lemmas())

""" Identifying Prefixes and Suffixes"""

import re

def extract_suffixes(word):
    suffixes = ['ing', 'ed', 'ly', 's']
    for suffix in suffixes:
        if word.endswith(suffix):
            return suffix
    return None

# Sample words
words = ["running", "played", "unhappy", "cats", "jump"]

# Apply function to extract suffixes
suffixes = [extract_suffixes(word) for word in words]

print(suffixes)

import re

def extract_prefixes(word):
    prefixes = ['un', 're', 'pre', 'dis']
    for prefix in prefixes:
        if word.startswith(prefix):
            return prefix
    return None

# Sample words
words = ["running", "redo", "unhappy", "dislike", "prepaid", "happy"]

# Apply function to extract prefixes
prefixes = [extract_prefixes(word) for word in words]

print(prefixes)

"""Using Regular Expressions for Compound Word Segmentation
Splitting Compound Words
"""

import re

# Sample compound words
compound_words = ['sunflower', 'basketball', 'football', 'notebook', 'toothbrush']

# A simple list of possible word components (a more comprehensive list would be much larger)
common_words = ['sun', 'flower', 'basket', 'ball', 'foot', 'book', 'tooth', 'brush']

# Function to break down compound words into known components
def split_compound_word(word, components):
    for component in components:
        if word.startswith(component):
            remaining = word[len(component):]
            if remaining in components:
                return component, remaining
    return word  # If no match, return the word itself

# Split compound words
split_results = {word: split_compound_word(word, common_words) for word in compound_words}

print(split_results)

"""Using Spacy for Compound Word Detection"""

import spacy

# Load a pre-trained SpaCy model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "The football players were practicing on the basketball court."

# Process the text with SpaCy
doc = nlp(text)

# Detect and print compound words
for token in doc:
    if token.dep_ == "compound":
        print(f"Compound word found: {token.text} -> Head: {token.head.text}")



''''
!pip install morfessor

!pip install pycld2

!pip install pyicu

!pip install polyglot

!polyglot download morph2.en
'''
from polyglot.downloader import downloader
print(downloader.supported_languages_table("morph2"))
'''
!pip install polyglot pyicu pycld2 morfessor
'''
from polyglot.downloader import downloader
downloader.download("morph2.en")  # example

# Commented out IPython magic to ensure Python compatibility.
# %%shell
# polyglot download morph2.en morph2.ar

from polyglot.text import Text, Word

words = ["preprocessing", "processor", "invaluable", "thankful", "crossed"]
for w in words:
  w = Word(w, language="en")
  print("{:<20}{}".format(w, w.morphemes))

''' Splitting string by morphological analysis'''
blob = "Wewillmeettoday."
text = Text(blob)
text.language = "en"
text.morphemes

from polyglot.downloader import downloader
print(downloader.supported_languages_table("pos2"))

# Commented out IPython magic to ensure Python compatibility.
# %%shell
# polyglot download embeddings2.en pos2.en

from polyglot.text import Text

blob = """We will meet at eight o'clock on Thursday morning."""
text = Text(blob)
text.pos_tags

