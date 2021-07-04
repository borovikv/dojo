import time

import pytest

import find_palindromes as subject


@pytest.mark.parametrize(
    'method,string,expected,time_expected', [
        (subject.count_palindromes, 'popop', 9, 0.01),
        (subject.count_palindromes, 'pop' * 500, 376250, 20),

        (subject.count_palindromes_n2, 'popop', 9, 0.01),
        (subject.count_palindromes_n2, 'pop' * 500, 376250, 20),
    ],
    ids=['popop', 'performance', 'popop_n2', 'performance_n2']
)
def test_count_palindromes(method,string,expected,time_expected):
    start = time.time()
    assert expected == method(string)
    end = time.time()
    print(end - start)
    assert end - start <= time_expected
