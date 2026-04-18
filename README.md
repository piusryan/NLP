# NLP Utils Package

A collection of Natural Language Processing (NLP) tools for text preprocessing, morphological analysis, and regex-based extraction.

## Installation

You can install this package directly from GitHub using pip:

```bash
pip install git+https://github.com/your-username/NLP.git
```

## Features

- **Preprocessing**: Tokenization, stop word removal, and word frequency analysis.
- **Morphology**: Stemming, lemmatization, suffix/prefix extraction, and compound word splitting.
- **Regex Utilities**: Email extraction, tweet cleaning, and structured data parsing.

## Quick Start

```python
from nlp_utils import download_all_resources, clean_tweet, tokenize_words

# Download required NLTK data
download_all_resources()

# Clean a tweet
tweet = "Good advice! RT @TheNextWeb: Learning to code today http://t.co/lbwej0pxOd #rstats"
cleaned = clean_tweet(tweet)
print(cleaned)

# Tokenize words
tokens = tokenize_words(cleaned)
print(tokens)
```

## Modules

- `nlp_utils.preprocessing`: Functions for basic text cleaning and tokenization.
- `nlp_utils.morphology`: Tools for structural word analysis.
- `nlp_utils.regex_utils`: Advanced regex patterns for specific NLP tasks.

## License

MIT
