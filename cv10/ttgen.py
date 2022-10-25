"""
Implementujte funkce time_generator a random_time dle zadání cv10.
S jejich pomocí následně vygenerujte soubor sample.txt.

Kompletní zadání je na elearing.tul.cz.
"""
import random


def time_generator(start, stop, step):
    """
    time_generator(start, stop, step) -> time tuple
    start: time tuple (hodiny, minuty, sekundy)
    stop: time tuple
    step: time tuple
    generuje rozsah časů mezi start a stop s krokem step
    """
    _hour = start[0]
    _min = start[1]
    _sek = start[2]
    yield start
    larger = True
    if (start[0] < stop[0]) | ((start[0] == stop[0]) & (start[1] < stop[1])) | (
            (start[0] == stop[0]) & (start[1] == stop[1]) & (start[2] < stop[2])):
        larger = False
    while True:
        _hour += step[0]
        _min += step[1]
        _sek += step[2]
        if _sek >= 60:
            _sek -= 60
            _min += 1
        if _min >= 60:
            _min -= 60
            _hour += 1
        if (_hour >= 24) & (larger is False):
            return StopIteration
        if _hour >= 24:
            _hour -= 24
            larger = False
        if ((_hour > stop[0]) | ((_hour == stop[0]) & (_min > stop[1])) |
                ((_hour == stop[0]) & (_min == stop[1]) & (_sek > stop[2]))) & (larger is False):
            return StopIteration
        time_step = (_hour, _min, _sek)
        yield time_step


def random_time():
    """ 
    random_time -> time tuple

    náhodně vygenerovaný validní time tuple (hodiny, minuty, sekundy)
    """
    random_tuple = [0, 0, 0]
    random_tuple[0] = random.randint(0, 23)  # podle zadaní tady je 24 ale to neni logicky
    random_tuple[1] = random.randint(0, 59)
    random_tuple[2] = random.randint(0, 59)
    return tuple(random_tuple)


def output(fname="sample.txt"):
    """
    zapíše soubor náhodně vygenerovaných časů a naměřených teplot v těchto časech
    """

    start = random_time()
    stop = random_time()
    step = random_time()
    krok = time_generator(start, stop, step)
    with open(fname, "w+") as my_file:
        my_file.write(str(start).strip('[]').replace(',', ':').replace(' ', '')
                      + "\n" + str(stop).strip('[]').replace(',', ':').replace(' ', '')
                      + "\n" + str(step).strip('[]').replace(',', ':').replace(' ', '') + "\n\n")
        for kroks in krok:
            my_file.write(str(kroks).strip('()[]').replace(',', ':').replace(' ', '')
                          + ", " + str(round(random.uniform(36, 41), 2)) + "\n")


if __name__ == '__main__':
    output()
