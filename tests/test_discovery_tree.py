import pytest
import re


def test_sanity():
    assert 1 == 1


def is_entity(line: str) -> bool:
    pattern = r'(\s*)(Q|A)[.:]\s+([^\s])'
    match = re.match(pattern, line)
    return match is not None


@pytest.mark.parametrize(['line', 'expected'], [
    ('', False),
    ('x', False),
    ('A. ', False),
    ('A. 41', True),
    ('Q. WTF?', True),
    ('Q.         WTF?', True),
    ('    A. 41', True),
    ('A.          ', False),
    ('A 41', False),
    ('A: 41', True),
    ('A- 41', False),
])
def test_is_entity(line, expected):
    actual = is_entity(line)
    assert actual == expected
