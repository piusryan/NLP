# -*- coding: utf-8 -*-
"""
Regex Utilities Module: Text cleaning, pattern matching, and extraction.
"""

import re

def extract_words(text):
    """Extract all words from text ignoring punctuation."""
    word_pattern = r'\b\w+\b'
    return re.findall(word_pattern, text)

def find_words_starting_with(text, char):
    """Find all words that start with a specific character (case-sensitive)."""
    pattern = rf'\b{char}\w*\b'
    return re.findall(pattern, text)

def tokenize_with_punctuation(text):
    """Tokenize text into words and punctuation."""
    tokens = re.split(r'(\W+)', text)
    return [token.strip() for token in tokens if token.strip()]

def extract_numbers(text):
    """Extract all numbers from text."""
    number_pattern = r'\b\d+\b'
    return re.findall(number_pattern, text)

def extract_course_info(text):
    """Extract course info (ID, Code, Name) from structured text."""
    course_pattern = r'([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4,})'
    return re.findall(course_pattern, text)

def extract_emails(text):
    """Extract all email addresses from text."""
    pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
    return re.findall(pattern, text, flags=re.IGNORECASE)

def clean_tweet(tweet):
    """Clean tweet text by removing URLs, mentions, hashtags, and extra whitespace."""
    tweet = re.sub(r'http\S+\s*', '', tweet)  # remove URLs
    tweet = re.sub(r'\b(RT|cc)\b', '', tweet)  # remove RT and cc
    tweet = re.sub(r'#\S+', '', tweet)  # remove hashtags
    tweet = re.sub(r'@\S+', '', tweet)  # remove mentions
    tweet = re.sub(r'[%s]' % re.escape(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)  # remove punctuations
    tweet = re.sub(r'\s+', ' ', tweet).strip()  # remove extra whitespace
    return tweet

if __name__ == "__main__":
    text = "Hello, my name is John Doe! I am learning Python, and it's fun 2 much."
    print("Words:", extract_words(text))
    print("Words starting with 'P':", find_words_starting_with(text, 'P'))
    print("Numbers:", extract_numbers(text))
    
    emails = "zuck26@facebook.com, page33@google.com"
    print("Emails:", extract_emails(emails))
    
    tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"
    print("Cleaned Tweet:", clean_tweet(tweet))
