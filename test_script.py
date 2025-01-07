import pytest
from calc import saludo

def test_saludo():
    assert saludo("Luis") == "Hello, Si funcionará!"
