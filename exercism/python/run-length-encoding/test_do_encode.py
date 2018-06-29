import pytest
from encode import do_encode

testdata = [
    ("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB", "12WB12W3B24WB"),
    ("AABCCCDEEEE", "2AB3CD4E"),
]


@pytest.mark.parametrize("input_string,expected", testdata)
def test_do_encode(input_string, expected):
    assert do_encode(string_input=input_string) == expected
