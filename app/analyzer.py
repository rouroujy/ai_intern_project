import string
from collections import Counter
from typing import Dict


def analyze_text(file_path: str,
                 ignore_case: bool = False,
                 remove_punctuation: bool = False) -> Dict:

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    if ignore_case:
        text = text.lower()

    if remove_punctuation:
        text = text.translate(str.maketrans("", "", string.punctuation))

    lines = text.splitlines()
    words = text.split()
    characters = len(text)

    word_counts = Counter(words)
    top_5 = word_counts.most_common(5)

    return {
        "lines": len(lines),
        "words": len(words),
        "characters": characters,
        "top_5_words": top_5
    }

