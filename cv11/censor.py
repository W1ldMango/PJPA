# -*- coding: utf-8 -*-

"""
@TODO - vyřešit úkol 11. - filtrování textu

Podrobné zadání jako obvykle na https://elearning.tul.cz

"""

import re
import argparse


def input_parse():
    """
    Parsing form console.
    """
    parser = argparse.ArgumentParser(
        description='Censorship of selected words.'
    )
    parser.add_argument("-i", "--input", metavar="", help="file to censor")
    parser.add_argument("-l", "--list", metavar="", help="file with list of censored words")
    parser.add_argument("-c", "--clean", action="store_true", help="clear html marks")
    parser.add_argument("-o", "--output", metavar="",
                        help="output file (if not selected, program will print the result to console")

    task = parser.parse_args()

    if task.input is None:
        parser.error("Missing input file!")
    if task.list is None:
        parser.error("Missing list of censored words!")

    return task


def load_input(file_name):
    """
    Loading lines from a file.
    """

    with open(file_name, "r") as file:
        return file.read().splitlines()



def clean_html(input_data):
    """
    Removing HTML parts from text.
    """
    clean_data = []

    for line in input_data:
        line = re.sub(re.compile(
            '<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});'), '', line)
        if line != "":
            clean_data.append(line)

    return clean_data


def print_censored_text(data, output_file):
    """
    Checking parameter c and selecting printing to file or console.
    """
    if output_file is None:
        print_to_console(data)
    else:
        print_to_file(data, output_file)


def censor(data, censor_list):
    """
    Replacing selected words by #s.
    """
    censored_data = []

    for line in data:

        for word in censor_list:
            hash_censor = ""
            remain_hashs = len(word)
            while remain_hashs != 0:
                hash_censor += "#"
                remain_hashs -= 1
            line = line.replace(word, hash_censor)

        censored_data.append(line)

    return censored_data


def print_to_console(data):
    """
    Printing lines to console.
    """
    for line in data:
        print(line)


def print_to_file(data, file_name):
    """
    Printing lines to selected file.
    """
    with open(file_name, "w+") as file:
        for line in data:
            file.write(line + "\n")


def main():
    """
    Main body of code created primarily for testing.
    """
    requested_task = input_parse()
    input_text = load_input(requested_task.input)
    censor_words = load_input(requested_task.list)

    if requested_task.clean:
        input_text = clean_html(input_text)

    censored_text = censor(input_text, censor_words)

    print_censored_text(censored_text, requested_task.output)


if __name__ == '__main__':
    main()
