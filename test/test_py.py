# content of test_sample.py
import app

def test_add():
    assert app.add(3,4) == 7


def test_sus():
    assert app.sus(9,4) == 5


def test_multiplication():
    assert app.multiplication(3,4) == 12

def test_fact():
     assert app.fact(3)==6