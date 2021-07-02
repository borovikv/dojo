import time

import pytest

import find_palindromes as subject


@pytest.mark.parametrize(
    'string,expected', [
        ('popop', 9),
        ('pop' * 3_000, 500000500000),
    ],
    ids=['popop', 'performance']
)
def test_count_palindromes(string, expected):
    start = time.time()
    assert expected == subject.count_palindromes(string)
    end = time.time()
    assert end - start <= 10
