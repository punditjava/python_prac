def write_to_file(output_name, dictionary):
    with open("%s" % output_name, 'w') as ofile:
        ofile.write(str(len(dictionary)) + '\n')
        for x in sorted(dictionary.keys()):
            ofile.write(x + ' - ' + ', '.join(sorted(dictionary[x])) + '\n')


def read_from_file(input_name):
    with open("%s" % input_name, 'r') as ifile:
        dictionary = {}
        for i in range(int(ifile.readline())):
            words = ifile.readline().split(' - ')
            values = words[1].rstrip().split(', ')
            for word in values:
                if word in dictionary:
                    dictionary[word] += [words[0]]
                else:
                    dictionary[word] = [words[0]]
    return dictionary


def get_new_dictionary(input_dict_name, output_dict_name):
    new_dict = read_from_file(input_dict_name)
    write_to_file(output_dict_name, new_dict)
