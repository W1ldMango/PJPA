"""
Implementujte alespoň čtyři testy dle zadání cv10
"""
import pytest
import ttgen


def test_correct_gen_value():
    """
    otestuje pokud vygeneruje se správný čas v určitém kroku
    """
    start = (19, 50, 10)
    stop = (21, 10, 00)
    step = (1, 15, 30)
    out = ''
    steps = ttgen.time_generator(start, stop, step)
    for i in steps:
        out += str(i)
    assert out == "(19, 50, 10)(21, 5, 40)"


def test_gen_over_midnight():
    """
    otestuje přechod přes půlnoc
    """
    start = (23, 59, 59)
    stop = (0, 10, 0)
    step = (0, 0, 1)
    steps = ttgen.time_generator(start, stop, step)
    next(steps)
    out = str(next(steps))
    assert out == "(0, 0, 0)"


def test_gen_stop_iteration():
    """
    otestuje pokud vyvolá se výjimka StopIteration
    """
    with pytest.raises(StopIteration):
        start = (19, 50, 10)
        stop = (21, 10, 00)
        step = (3, 15, 30)
        steps = ttgen.time_generator(start, stop, step)
        next(steps)
        next(steps)




def test_valid_random_time():
    """
    otestuje validitu vygenerovaného časového tuple
    """
    out = ttgen.random_time()
    assert (out[0] > 0) & (out[0] < 24) & (out[1] > 0) & (out[1] < 60) & (out[2] > 0) & (out[2] < 60)


def test_correct_gen_out():
    """
    otestuje jestli se vypiše čas, který se rovná konci
    """
    start = (23, 59, 59)
    stop = (0, 10, 0)
    step = (0, 10, 1)
    steps = ttgen.time_generator(start, stop, step)
    next(steps)
    out = str(next(steps))
    assert out == "(0, 10, 0)"

def test_correct_gen_out_1():
    """
    otestuje jestli se vypiše čas, který se rovná konci
    """
    start = (19, 50, 10)
    stop = (21, 10, 00)
    step = (1, 15, 30)
    steps = ttgen.time_generator(start, stop, step)
    next(steps)
    out = str(next(steps))
    assert out == "(21, 5, 40)"
