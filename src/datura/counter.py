import re
import logging
from collections import Counter
from pathlib import Path

logger = logging.getLogger(__name__)


alphanumeric_regex: re.Pattern = re.compile(r'[^\w]')


def read_file(path: Path) -> str:
    """Loads the contents of the file at path, and returns them as a long string.
    Note: this is not very efficient for large files, as all their contents are loaded into memory.

    Args:
        path: the path of the input file.
    """
    try:
        f = path.open('r')
        contents = ' '.join(f.readlines())
        return contents
    except Exception as ex:
        logger.exception(f'Could not open file: {ex}')
        raise


def normalize_word(raw_word: str) -> str:
    '''Converts all uppercase characters into lowercase, and takes only the alphanumeric characters out of the resulting
    string.
    '''
    return alphanumeric_regex.sub('', raw_word.lower())


def raw_word_count(contents: list[str]) -> dict[str, int]:
    '''Counts the words.

    Note: this function does NOT load directly from the file. Use word_count() instead.
    '''
    word_counter = Counter()
    for word in contents:
        word_counter[normalize_word(word)] += 1
    return word_counter


def word_count(path: Path) -> dict[str, int]:
    contents = read_file(path)
    words = contents.split()

    counts = raw_word_count(words)
    return counts
