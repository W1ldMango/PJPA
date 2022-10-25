# -*- coding: utf-8 -*-

"""
Úkol 5.
Napište program, který načte soubor large.txt a pro každé dveře vyhodnotí,
zda je možné je otevřít nebo ne. Tedy vyhodnotí, zda lze danou množinu uspořádat
požadovaným způsobem. Výstup z programu uložte do souboru vysledky.txt ve
formátu 1 výsledek =  1 řádek. Na řádek napište vždy počet slov v množině a True
nebo False, podle toho, zda řešení existuje nebo neexistuje.

Podrobnější zadání včetně příkladu je jako obvykle na elearning.tul.cz
"""

def read_data(path):
    with open(path, "r") as file:
        lines = [line.rstrip('\n') for line in file]
        return lines

def write_file(text):
    with open("vysledky.txt", "a") as file:
        file.write(text)

def clean_file():
    with open("vysledky.txt","w") as file:
        pass
    with open("vysledky.txt", "r+") as file:
        return file.truncate()

def get_result():
    input_data = "large.txt"
    clean_file()
    lines = read_data(input_data)
    door_count = int(lines[0])
    count = 0

    for i in range(door_count):
        letters = [[0 for x in range(26)] for y in range(3)]
        count += 1

        word_count = int(lines[count])
        output = str(word_count) + " "

        for j in range(count + 1, count + word_count + 1):

            first = ord(lines[j][0])-97
            last = ord(lines[j][-1])-97
            letters[0][first] += 1
            letters[1][last] += 1
            if first == last:
                letters[2][first] += 1
        result = test_sec(letters)
        output += str(result) + "\n"
        write_file(output)
        count += word_count



def test_sec(letters):
    temp = [0 for x in range(3)]
    result = True
    for first_letter, last_letter, doubles in zip(letters[0], letters[1], letters[2]):

        if doubles != 0 and (first_letter == last_letter == doubles):
            result = False
            break

        letter = first_letter - last_letter

        if letter != 0:
            if letter == 1:
                temp[0] += 1
                continue

            if letter == -1:
                temp[1] += 1
                continue

            temp[2] += 1

    if result and temp[0] <= 1 and temp[1] <= 1 and temp[2] == 0:
        pass
    else:
        result = False
    return result


if __name__ == '__main__':
    get_result()
