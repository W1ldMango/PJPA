# -*- coding: utf-8 -*-
"""
Úkol 6.
Vaším dnešním úkolem je vytvořit program, který o zadaném textu zjistí některé
údaje a vypíše je na standardní výstup. Hlavním smyslem cvičení je procvičit
si práci s regulárními výrazy, takže pro plný bodový zisk je nutné použít k
řešení právě tento nástroj.

Program musí pracovat s obecným textem, který bude zadaný v souboru. Jméno
souboru bude zadáno jako vstupní parametr funkce main, která by měla být
vstupním bodem programu. Samozřejmě, že funkce main by neměla řešit problém
kompletně a měli byste si vytvořit další pomocné funkce. Můžete předpokládat,
že soubor bude mít vždy kódování utf-8 a že bude psaný anglicky, tedy jen
pomocí ASCII písmen, bez české (či jiné) diakritiky. 

Konkrétně musí program zjistit a vypsat:

1. Počet slov, která obsahují nejméně dvě samohlásky (aeiou) za sebou. Například
slovo bear.

2. Počet slov, která obsahují alespoň tři samohlásky - například slovo atomic.

3. Počet slov, která mají šest a více znaků - například slovo terrible.

4. Počet řádků, které obsahují nějaké slovo dvakrát. 

Podrobnější zadání včetně příkladu je jako obvykle na elearning.tul.cz
"""
import re



def main(file_name):
    text = data_processing(file_name)
    print("1. ", count_double(text))
    print("2. ", count_triple(text))
    print("3. ", count_six(text))
    print("4. ", count_words(file_name))


def data_processing(file_name):
    with open(file_name, "r+") as file:
        text = file.readlines()
    words_array = []
    for line in text:
        for word in line.split():
            words_array.append(clean(word))
    return words_array


def clean(word):
    chars = ".,!?;"
    for char in chars:
        if word[len(word) - 1] == char:
            word = word[:-1]
            break
    return word.lower()


def count_double(text):
    good = []
    for word in text:
        if re.search("[aeiyou]{2}", word) and word not in good:
            good.append(word)

    return len(good)


def count_triple(text):
    good = []
    for word in text:
        count = 0
        for char in word:
            if re.search("[aeiyou]", char):
                count += 1
            if count > 2 and word not in good:
                good.append(word)
                break
    return len(good)


def count_six(text):
    good = []
    for word in text:
        if re.search("[a-zA-Z]{6,}", word) and word not in good:
            good.append(word)
    return len(good)


def count_words(file_name):
    with open(file_name, "r+") as file:
        text = file.readlines()
    count = 0
    for line in text:
        for word in line.split():
            word = clean(word)
            if len(re.findall("\\b" + word + "\\b", line.lower())) > 1:
                count += 1
                break
    return count


if __name__ == '__main__':
    main('cv06_test.txt')
