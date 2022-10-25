# -*- coding: utf-8 -*-

"""
@TODO: zde napiste svoje unit testy pro modul censor.py
"""
import sys
import pytest
import censor


def test_missing_arguments():
    '''
    Testing input with missing arguments.
    '''
    sys.argv = ['censor.py']
    with pytest.raises(SystemExit):
        censor.input_parse()


def test_missing_file_name_1():
    '''
    Testing missing all file names.
    '''
    sys.argv = ['censor.py', '--i', '--l']
    with pytest.raises(SystemExit):
        censor.input_parse()


def test_missing_file_name_2():
    '''
    Testing missing input file name.
    '''
    sys.argv = ['censor.py', '--i', 'test.html', '--l']
    with pytest.raises(SystemExit):
        censor.input_parse()


def test_missing_file_name_3():
    '''
    Testing missing list file name.
    '''
    sys.argv = ['censor.py', '--i', '--l', 'test.txt']
    with pytest.raises(SystemExit):
        censor.input_parse()


def test_missing_file_name_4():
    '''
    Testing missing output file name.
    '''
    sys.argv = ['censor.py', '--i', 'test.html', '--l', 'test.txt', '--o']
    with pytest.raises(SystemExit):
        censor.input_parse()


def test_correct_parser_1():
    """
    Correct parser.
    """
    sys.argv = ['censor.py', '--i', 'test.html', '--l', 'test.txt']
    file = "test.html"
    censor_list = "test.txt"
    assert censor.input_parse().input == file and censor.input_parse().list == censor_list


def test_correct_parser_2():
    """
    Correct parser.
    """
    sys.argv = ['censor.py', '--i', 'test.html', '--l', 'test.txt', '--c']
    file = "test.html"
    censor_list = "test.txt"
    assert censor.input_parse().input == file and censor.input_parse().list == censor_list


def test_correct_parser_3():
    """
    Correct parser.
    """
    sys.argv = ['censor.py', '--i', 'test.html', '--l', 'test.txt', '--o', 'out_text.txt']
    file = "test.html"
    censor_list = "test.txt"
    out_file = "out_text.txt"
    assert censor.input_parse().input == file and censor.input_parse().list == censor_list and censor.input_parse().output == out_file


def test_load_input():
    """
    Testing loading from non-existing file.
    """
    with pytest.raises(FileNotFoundError):
        censor.load_input('not_exist.html')


def test_clean_html():
    """
    Testing function for removing html parts.
    """
    original = ["<h1>Ahoj</h1> <p>text</p>", "kakao"]
    cleaned = ["Ahoj text", "kakao"]
    assert censor.clean_html(original) == cleaned


def test_censor():
    """
    Testing consoring.
    """
    original = ["kakao bagr"]
    cens_list = ["kakao"]
    censored = ["##### bagr"]
    assert censor.censor(original, cens_list) == censored


def test_param_o_1(capfd):
    """
    Testing choosing between file and console.
    """
    text = ["test", "test2"]
    censor.print_censored_text(text, None)
    out, __ = capfd.readouterr()
    assert out != ""


def test_param_o_2(capfd):
    """
    Testing choosing between file and console.
    """
    text = ["test", "test2"]
    censor.print_censored_text(text, "test_out.txt")
    out, __ = capfd.readouterr()
    assert out == ""


def test_print_to_console(capfd):
    """
    Testing printing to console.
    """
    text = ["test", "test2"]
    censor.print_to_console(text)
    out, __ = capfd.readouterr()
    assert out == 'test\ntest2\n'


def test_print_to_file():
    """
    Testing printing to file.
    """
    text = ["test", "test2"]
    censor.print_to_file(text, "test_out_2.txt")
    with open("test_out_2.txt", "r") as file:
        printed_text = file.read()
    assert printed_text == 'test\ntest2\n'
