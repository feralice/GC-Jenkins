import sys
import os

# tava dando problema pra encontrar os testes tive que fazer isso abaixo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from temperature_converter import fahrenheit_to_celsius, celsius_to_fahrenheit

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == pytest.approx(0)
    assert fahrenheit_to_celsius(212) == pytest.approx(100)
    assert fahrenheit_to_celsius(-40) == pytest.approx(-40)
    assert fahrenheit_to_celsius(98.6) == pytest.approx(37)
    assert fahrenheit_to_celsius(0) == pytest.approx(-17.7778, abs=1e-4)

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == pytest.approx(32)
    assert celsius_to_fahrenheit(100) == pytest.approx(212)
    assert celsius_to_fahrenheit(-40) == pytest.approx(-40)
    assert celsius_to_fahrenheit(37) == pytest.approx(98.6)
    assert celsius_to_fahrenheit(-17.7778) == pytest.approx(0, abs=1e-4)