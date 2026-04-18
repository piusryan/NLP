# -*- coding: utf-8 -*-
"""
Morphological Analysis Module: Stemming, Lemmatization, and Compound Word Analysis.
"""

import re
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tag import RegexpTagger
from nltk.tokenize import word_tokenize

# Optional imports that might not be installed
try:
    import spacy
except ImportError:
    spacy = None

try:
    from polyglot.text import Text, Word
    from polyglot.downloader import downloader
except ImportError:
    Text = Word = downloader = None

def download_resources():
    """Download necessary NLTK and Polyglot resources."""
    nltk.download('wordnet', quiet=True)
    nltk.download('punkt_tab', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    if downloader:
        try:
            downloader.download("morph2.en", quiet=True)
        except Exception:
            pass

def apply_stemming(words):
    """Apply Porter Stemming to a list of words."""
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in words]

def apply_lemmatization(words, pos=wordnet.VERB):
    """Apply WordNet Lemmatization to a list of words."""
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word, pos=pos) for word in words]

def tag_morphology(sentence):
    """Apply basic morphological tagging using regex."""
    tokens = word_tokenize(sentence)
    patterns = [
        (r'.*ing$', 'VB'),    # Verbs ending in 'ing'
        (r'.*ly$', 'RB'),     # Adverbs ending in 'ly'
        (r'.*es$', 'NNS'),    # Nouns ending in 'es'
    ]
    tagger = RegexpTagger(patterns)
    return tagger.tag(tokens)

def extract_suffixes(word):
    """Extract common suffixes from a word."""
    suffixes = ['ing', 'ed', 'ly', 's']
    for suffix in suffixes:
        if word.endswith(suffix):
            return suffix
    return None

def extract_prefixes(word):
    """Extract common prefixes from a word."""
    prefixes = ['un', 're', 'pre', 'dis']
    for prefix in prefixes:
        if word.startswith(prefix):
            return prefix
    return None

def split_compound_word(word, components):
    """Break down compound words into known components."""
    for component in components:
        if word.startswith(component):
            remaining = word[len(component):]
            if remaining in components:
                return component, remaining
    return word

def get_spacy_compounds(text, model="en_core_web_sm"):
    """Detect compound words using SpaCy."""
    if not spacy:
        return "SpaCy not installed."
    try:
        nlp = spacy.load(model)
        doc = nlp(text)
        return [(token.text, token.head.text) for token in doc if token.dep_ == "compound"]
    except Exception as e:
        return str(e)

def get_morphemes_polyglot(words, lang="en"):
    """Get morphemes using Polyglot."""
    if not Word:
        return "Polyglot not installed."
    results = {}
    for w in words:
        try:
            poly_word = Word(w, language=lang)
            results[w] = poly_word.morphemes
        except Exception:
            results[w] = None
    return results

if __name__ == "__main__":
    download_resources()
    test_words = ["running", "runner", "runs", "easily", "happier", "better"]
    print("Stemmed:", apply_stemming(test_words))
    print("Lemmatized:", apply_lemmatization(test_words))
    
    sentence = "The cats were running quickly."
    print("Tagged:", tag_morphology(sentence))
    
    print("Suffix of 'running':", extract_suffixes("running"))
    print("Prefix of 'unhappy':", extract_prefixes("unhappy"))
    
    common_components = ['sun', 'flower', 'basket', 'ball', 'foot', 'book', 'tooth', 'brush']
    print("Split compound 'sunflower':", split_compound_word("sunflower", common_components))
