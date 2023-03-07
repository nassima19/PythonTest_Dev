# content of test_sample.py
import app
import unittest
import pytest

class RegisterNewInstructor(unittest.TestCase):
 def test_answer():
    assert app.inc(3) == 4