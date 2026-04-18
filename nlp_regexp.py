# -*- coding: utf-8 -*-




import re

# Sample text
text = "Hello, my name is John Doe! I am learning Python, and it's fun 2 much."

# 1. Regular Expression for detecting words (ignoring punctuation)
# We define a pattern that matches words consisting of letters and numbers.
word_pattern = r'\b\w+\b'

# Use re.findall() to get all the words from the text.
words = re.findall(word_pattern, text)
print("Words:", words)

# 2. Regular Expression for detecting specific word patterns (e.g., words starting with 'P')
# Define a pattern to match words that start with 'P'
pattern_start_with_p = r'\bP\w*\b'

# Find all words that start with 'P'
p_words = re.findall(pattern_start_with_p, text)
print("Words starting with 'P':", p_words)

# 3. Tokenizing text based on spaces and punctuation
# Define a pattern to split the text into tokens (words and punctuation)
tokens = re.split(r'(\W+)', text)
print("Tokens:", [token.strip() for token in tokens if token.strip()])  # Remove empty tokens

# 4. Regular Expression for detecting numbers (optional)
number_pattern = r'\b\d+\b'
numbers = re.findall(number_pattern, text)
print("Numbers:", numbers)

text = """101   COM   Computers
205   MAT   Mathematics
189   ENG    English"""

re.findall('[0-9]+', text)

re.findall('[A-Z]{3}', text)

re.findall('[A-Za-z]{4,}', text)

# define the course text pattern groups and extract
course_pattern = '([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4,})'
re.findall(course_pattern, text)

print(re.findall(r'Co+l', 'So Cooool Coool cool coool col'))

re.findall(r'\btoy\b', 'play toy broke toys')

emails = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""
pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
re.findall(pattern, emails, flags=re.IGNORECASE)

#Cleaning the tweet msg for proper message
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
import re

def clean_tweet(tweet):
    tweet = re.sub('http\S+\s*', '', tweet)  # remove URLs
    tweet = re.sub('RT|cc', '', tweet)  # remove RT and cc
    tweet = re.sub('#\S+', '', tweet)  # remove hashtags
    tweet = re.sub('@\S+', '', tweet)  # remove mentions
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)  # remove punctuations
    tweet = re.sub('\s+', ' ', tweet)  # remove extra whitespace
    return tweet

print(clean_tweet(tweet))