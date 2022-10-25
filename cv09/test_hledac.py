"""

implementujte testy pro program hledac.py

pokrytí kódu musí být minimálně 75%
"""

import sys
import pytest
import hledac

lines = ["brachiosaurus", "tyranosaurus", "albertosaurus", "velociraptor"]


def test_find_1(capfd):
    """
    Testing printing the whole file.
    """
    hledac.find(lines, None)
    out, __ = capfd.readouterr()
    assert out == "1:brachiosaurus\n2:tyranosaurus\n3:albertosaurus\n4:velociraptor\n"


def test_find_2(capfd):
    """
    Testing key sensitivity.
    """
    words = "BRA"
    hledac.find(lines, words)
    out, __ = capfd.readouterr()
    assert out == ""


def test_input_1():
    '''
    Testing input with missing file.
    '''
    sys.argv = ['hledac.py']
    with pytest.raises(SystemExit):
        hledac.parse_input()


def test_input_2():
    '''
    Testing input with missing words.
    '''
    sys.argv = ['hledac.py', '--f', 'test.txt', '--s']
    with pytest.raises(SystemExit):
        hledac.parse_input()


def test_input_3():
    """
    Parser with both parrameter, one word.
    """
    sys.argv = ['hledac.py', '--f', 'test.txt', "--s", "word"]
    file = "test.txt"
    search = ["word"]
    assert hledac.parse_input().filename == file and hledac.parse_input().search == search


