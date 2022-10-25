# -*- coding: utf-8 -*-

"""
Cvičení 7. - práce s daty

Vaším dnešním úkolem je spojit dohromady data, uložená ve dvou různých
souborech. První soubor obsahuje výsledky závodu - jména a časy závodníků. Druhý
pak obsahuje databázi závodníků uloženou jako JSON - mimo jiné jejich id. Cílem
je vytvořit  program, který tyto data propojí, tedy ke každému závodníkovi ve
štafetě najde jeho id. Případně také nenajde, data nejsou ideální. I tuto
situaci ale musí program korektně ošetřit.  Výsledky programu bude potřeba
zapsat do dvou souborů.

Kompletní zadání je jako vždy na https://elearning.tul.cz/

"""
import json
import re
from bs4 import BeautifulSoup


def output_json(result_list):
    """
    Uloží list slovníků do souboru output.json tak jak je požadováno 
    v zadání.
    """
    with open('output.json', 'w') as output:
        output.write(json.dumps(result_list, indent=4, sort_keys=True))


def read_data():
    """
    Read data from json and html files
    """
    with open("competitors.json", "r") as json_file:
        json_data_file = json.load(json_file)
    with open("result.html", "r") as html_file:
        html_data_file = BeautifulSoup(html_file, "html.parser")
    return html_data_file, json_data_file


def pretty_data(input_data):
    """
    Make data in files easy to use
    """
    pretty = []
    pattern = r'\d+[)]+\s+[\w ]+\s[0-9:]+\s[(][\w ,-]+[)]'
    reg = re.findall(pattern, input_data)

    for i in reg:
        split = re.split("[(]", i)
        names = re.split(", ", split[1].replace(")", ""))
        time = re.split(" ", split[0].replace(")", ""))

        for j in names:
            temp = [time[0], time[len(time) - 2], j]
            pretty.append(temp)

    return pretty


def create_list(input_pr_data, input_json_data):
    """
    Create lists of result with id or not
    """
    results = []

    for i in input_pr_data:
        found = False
        for j in input_json_data:
            if j["firstname"] + " " + j["lastname"] == i[2]:
                result = {
                    "id": j["id"], "result": i[0], "time": i[1]
                }
                results.append(result)
                found = True
                break
        if not found:
            result = {
                "id": False, "result": i[0], "time": i[1], "no_match": i[2]
            }
            results.append(result)

    return results


def write_errors(input_data):
    with open("errors.txt", "w") as errors_file:
        for i in input_data:
            if i["id"] is False:
                errors_file.write(i["no_match"])
                errors_file.write("\n")


def write_compare(input_data):
    output = []
    for i in input_data:
        if i["id"] is not False:
            result = [i["id"], i["result"]]
            output.append(result)
    output.sort()

    with open("compare.txt", "w") as compare_file:
        for i in output:
            compare_file.write(str(i[0]) + " " + i[1] + "\n")


if __name__ == '__main__':
    html_data, json_data = read_data()
    separated_p = html_data.find_all('p')
    html_women = str(separated_p[18])
    html_men = str(separated_p[20])
    html_full = html_women + html_men
    pr = pretty_data(html_full)
    data = create_list(pr, json_data)

    output_json(data)
    write_compare(data)
    write_errors(data)
