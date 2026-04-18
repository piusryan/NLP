# -*- coding: utf-8 -*-
"""
Text Preprocessing Module: Tokenization, Filtration, word frequency, and Stop Word Removal.
"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Ensure necessary NLTK data is downloaded
def download_resources():
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)
    nltk.download('stopwords', quiet=True)

def tokenize_sentences(text):
    """Tokenize text into sentences."""
    return sent_tokenize(text)

def tokenize_words(text):
    """Tokenize text into words."""
    return word_tokenize(text)

def get_word_frequency(tokens):
    """Calculate frequency distribution of tokens."""
    return FreqDist(tokens)

def plot_word_frequency(fdist, top_n=30):
    """Plot the frequency distribution."""
    fdist.plot(top_n, cumulative=False)
    plt.show()

def remove_stopwords(tokens, language="english"):
    """Remove stop words from a list of tokens."""
    stop_words = set(stopwords.words(language))
    return [w for w in tokens if w.lower() not in stop_words]

if __name__ == "__main__":
    # Example usage
    download_resources()
    text = """Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
    The sky is pinkish-blue. You shouldn't eat cardboard"""
    
    tokenized_text = tokenize_sentences(text)
    print("Sentences:", tokenized_text)
    
    tokenized_word = tokenize_words(text)
    print("Words:", tokenized_word)
    
    fdist = get_word_frequency(tokenized_word)
    print("Most common words:", fdist.most_common(4))
    
    filtered_sent = remove_stopwords(tokenized_word)
    print("Filtered Word:", filtered_sent)
