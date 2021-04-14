#!/usr/bin/pytest-3 -vv

import pytest

from src.dummy import big_bada_bum

test_data = [n for n in range(500)]


@pytest.mark.parametrize("n", test_data)
def test_big_bada_bum(n):
    assert big_bada_bum(n) == (True if (n % 2 == 0) else False)
