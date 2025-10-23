import pytest
from hello import my_function

def test_my_function():
    assert my_function() == "Hello, GitHub Actions!"
