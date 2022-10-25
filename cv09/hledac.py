"""
Implementujte program dle zadání úlohy 9. na elearning.tul.cz

Vytvořte program, který prohledá zadaný textový
soubor a nejde v něm řádky, na kterých se vyskytuje hledaný vzor. Případně více
vzorů. Tyto řádky pak vypíše na obrazovku a přidat k ním jejich čísla v původním
souboru. 

Tak trochu se toto chování podobá unixovému příkazu grep, přesněji
řečeno grep -n.  Ten můžete případně použít pro kontrolu. Nicméně váš program
toho bude umět v mnoha ohledech méně a v jednom více (vyhledávání více vzorů
najednou). Nejde tedy o to vytvářet 100% kopii příkazu grep.

Program musí jít  ovládat z příkazové řádky. Základním parametrem zadávaným
vždy, je jméno souboru. Pokud jméno souboru není zadané program nemůže pracovat
a měl by v takovém případě zobrazit nápovědu.

Druhý parametr  parametr -s --search bude volitelný. Může být následován
libovolným počtem n slov. Samozřejmě, pokud je tam parametr -s musí tam být to
slovo alespoň jedno (tedy n >= 1).  Pokud není zadané hledané slovo, musí
program opět vypsat chybu nebo nápovědu.
 """

import argparse


def parse_input():
    """
    Parser input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="filename")
    parser.add_argument("-s", "--search", type=str, nargs="*", help="words to search")
    args = parser.parse_args()

    if args.filename is None:
        parser.error("Need to choose file")
    elif not args.search:
        parser.error("You must to choose words")
    return args


def find(input_lines, words):
    if words is None:
        for i in range(0, len(input_lines)):
            print(str(i + 1) + ":" + input_lines[i])
    else:
        for i in range(0, len(input_lines)):
            found = True
            for word in words:
                if word not in input_lines[i]:
                    found = False
                    break
            if found:
                print(str(i + 1) + ":" + input_lines[i])


def main():
    """
    Main
    """
    requested_task = parse_input()
    with open(requested_task.filename, "r") as file:
        source_data = file.readlines()
    find(source_data, requested_task.search)


if __name__ == '__main__':
    main()
