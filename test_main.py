import pytest
from main import generate_sentence


def test_generate_sentence():

    sentence = generate_sentence()

    # check if the sentence has exactly 6 words
    words = sentence[:-1].split()  # Remove the period and split into words
    assert len(words) == 6, f"Expected 6 words, got {len(words)}"
    # Check if capitalized
    assert sentence[0].isupper(), "The first letter should be capitalized"
    # Check if there is a period
    assert sentence.endswith("."), "The sentence should end with a period"
