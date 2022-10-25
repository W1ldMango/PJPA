#!/bin/env python
# -*- coding: utf-8 -*-
"""
PJP - cvičení číslo 2
"""


def is_convex(a, b, c, d):
    """
    Druhým úkolem je vytvořit funkci, která ze čtyř zadaných bodů určí, 
    zda tvoří konvexní čtyřúhelník.
    
    Body na vstupu jsou zadávány jako tuple (x, y) kde x a y mohou být
    libovolná reálná čísla, tedy i záporná. Body mohou vytvořit čtyřúhelník,
    ale není to pravidlem.

    Je potřeba aby funkce hlídala i extrémní situace, jako například,
    že body čtyřúhelník vůbec nevytváří. 
    """

    t1 = ((d[0] - a[0]) * (b[1] - a[1]) - (d[1] - a[1]) * (b[0] - a[0]))
    t2 = ((d[0] - b[0]) * (c[1] - b[1]) - (d[1] - b[1]) * (c[0] - b[0]))
    t3 = ((d[0] - c[0]) * (a[1] - c[1]) - (d[1] - c[1]) * (a[0] - c[0]))
    t4 = ((a[0] - c[0]) * (b[1] - c[1]) - (a[1] - c[1]) * (b[0] - c[0]))

    if t1 * t2 * t3 * t4 > 0:
        return True
    return False


if __name__ == '__main__':
    is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0))
