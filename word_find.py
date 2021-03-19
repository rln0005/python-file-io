import re
print('Opening origin.txt')
line_number = 0
with open('origin.txt', 'r') as find_in_stream:
    print('Opening word_find_output.txt')
    with open('word_find_output.txt', 'w') as find_out_stream:
        for line in find_in_stream:
            line = line.strip()
            line_number += 1
            search_string = r"(.\Sherit\w+)"
            search_obj = re.compile(search_string)
            herit = search_obj.findall(line)
            for found in herit:
                find_out_stream.write('{0}\t{1}\n'.format(line_number, found))
print("Done!")
print('origin.txt is closed?', find_in_stream.closed)
print('word_find_output.txt is closed?', find_out_stream.closed)

