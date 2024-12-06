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



def test_one_long_word():
    example_input = ('a' * 100).split()
    assert raw_word_count(example_input) == {
        'a' * 100: 1
    }


def test_uppercase():
    example_input = """
    HELLO WORLD!
    THIS IS A SAMPLE TEXT FILE
    HELLO PYTHON WORLD
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


def test_special_chracters():
    example_input = '''
    Hello!!!! Wor#$%#$%ld
    AAAAA H#ello
    '''.split()
    assert raw_word_count(example_input) == {
        'hello': 2,
        'world': 1,
        'aaaaa': 1,
    }

def test_file_word_count():
    pass