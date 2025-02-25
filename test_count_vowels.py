import pytest
from count_vowels import count_vowels

def test_only_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_no_vowels():
    assert count_vowels("bcdfg") == 0

def test_mixed_string():
    assert count_vowels("Hello World") == 3
    assert count_vowels("PyThOn PrOgRaMmInG") == 4
    assert count_vowels("12345!@#$%") == 0
    assert count_vowels("A Quick Brown Fox") == 5

if __name__ == "__main__":
    pytest.main()