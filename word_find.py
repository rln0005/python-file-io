
### search a file line by line for a matching regex and generate an output file with the matches and line numbers
import sys
import re

def regex_compile(search_string):
    """
    Used to compile regex search string to object.
    ------------Parameters----------
    search_string : str : a regex pattern string to be used to search for
    ------------Yields--------------
    A compiled regex object that can be used in regex matching commands.
    """
    search_obj = re.compile(search_string)
    return search_obj

def line_strip(input, output):
    """
    Strips input file into lines with line numbers and finds all occurrences of regex_compile and writes the line number and regex-matching word to output file.
    ------------Parameters------------
    input : str : a .txt file to be read from
    output : str : a .txt file to be written to
    ------------Yields----------------
    Output file written with the line number and word that matches regex_compile from input
    """
    line_number = 0
    for line in input:
        line = line.strip()
        line_number += 1
        found = regex_compile(search_string).findall(line)
        for i in found:
            output.write('{0}\t{1}\n'.format(line_number, i))


if __name__ == '__main__':
    with open('origin.txt', 'r') as input:
        with open('output.txt', 'w') as output:
            search_string = r"(.\Sherit\w+)"
            regex_compile(search_string)
            line_strip(input, output)
    input.closed
    output.closed
