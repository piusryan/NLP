from .preprocessing import (
    download_resources as download_preprocessing_resources,
    tokenize_sentences,
    tokenize_words,
    get_word_frequency,
    plot_word_frequency,
    remove_stopwords
)
from .morphology import (
    download_resources as download_morphology_resources,
    apply_stemming,
    apply_lemmatization,
    tag_morphology,
    extract_suffixes,
    extract_prefixes,
    split_compound_word
)
from .regex_utils import (
    extract_words,
    find_words_starting_with,
    tokenize_with_punctuation,
    extract_numbers,
    extract_course_info,
    extract_emails,
    clean_tweet
)

def download_all_resources():
    """Download all necessary resources for the package."""
    download_preprocessing_resources()
    download_morphology_resources()
