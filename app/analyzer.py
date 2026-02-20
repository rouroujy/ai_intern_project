import string
from collections import Counter
from typing import Dict
import logging
import aiofiles

logger = logging.getLogger(__name__)


#io错误
class TextAnalysisError(Exception):
    """Custom exception for text analysis errors"""
    pass


async def analyze_text(file_path: str,
                 ignore_case: bool = False,
                 remove_punctuation: bool = False) -> Dict:
    
    logger.info(f"Start analyzing file: {file_path}")

    try:
        async with aiofiles.open(file_path, "r", encoding="utf-8") as f:
            text = await f.read()
            logger.debug("Raw text length: %s", len(text))
    except FileNotFoundError:
        logger.exception("File not found")
        raise TextAnalysisError("File does not exist")
    except Exception:
        logger.exception("Unexpected error while reading file")
        raise

    if ignore_case:
        text = text.lower()

    if remove_punctuation:
        text = text.translate(str.maketrans("", "", string.punctuation))

    lines = text.splitlines()
    words = text.split()
    characters = len(text)

    word_counts = Counter(words)
    top_5 = word_counts.most_common(5)

    logger.info("Analysis completed successfully!")

    return {
        "lines": len(lines),
        "words": len(words),
        "characters": characters,
        "top_5_words": top_5
    }

