"""
Vytvorte funkce encrypt a decrypt pro Caesarovu sifru.
Kompletni zadani v elearningu.
"""


def encrypt(word, offset):
    """
    :param word - slovo k zasifrovani
    :param offset - znakovy posun
    :return: zasifrovane slovo
    """

    result = ""
    for symb in word:
        asc_symb = ord(symb)
        if not symb.isalpha():
            result += symb
        elif symb.isupper():
            asc_symb += offset
            while asc_symb > 90:
                asc_symb -= 26
            result += chr(asc_symb)
        else:
            asc_symb += offset
            while asc_symb > 122:
                asc_symb -= 26
            result += chr(asc_symb)



    return result


def decrypt(word, offset):
    """
    :param word - zasifrovane slovo
    :param offset - znakovy posun
    :return: desifrovane slovo
    """
    result = ""

    for symb in word:
        asc_symb = ord(symb)
        if not symb.isalpha():
            result += symb
        elif symb.isupper():
            asc_symb -= offset
            while asc_symb < 65:
                asc_symb += 26
            result += chr(asc_symb)
        else:
            asc_symb -= offset
            while asc_symb < 97:
                asc_symb += 26
            result += chr(asc_symb)

    return result


