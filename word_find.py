
print('Opening origin.txt')
line_number = 0
with open('origin.txt', 'r') as find_in_stream:
    print('Opening word_find_output.txt')
    with open('word_find_output.txt', 'w') as find_out_stream:
        for line in find_in_stream:
            line = line.strip()
            word_list = line.split()
            line_number += 1
            for word in word_list:
                #import re
                #search_string = '(herit)'
                #search_obj = re.compile(search_string)
                #match = list(filter(search_obj.match, word_list))
                #search_obj.findall(word_list)
                find_out_stream.write('{0}\t{1}\n'.format(line_number, word))

print("Done!")
print('origin.txt is closed?', find_in_stream.closed)
print('word_find_output.txt is closed?', find_out_stream.closed)

