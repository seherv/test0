import pytest

from datura.counter import raw_word_count

def test_basic_word_count():
    example_input = """
    Hello world!
    This is a sample text file.
    Hello Python world.
    """.split()

    assert raw_word_count(example_input) == {
        'hello': 2,
        'world': 2,
        'this': 1,
        'is': 1,
        'a': 1,
        'sample': 1,
        'text': 1,
        'file': 1,
        'python': 1
    }

def test_no_words():
    example_input = ''.split()

    assert raw_word_count(example_input) == {}

