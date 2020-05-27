def convert_section_name_map(section_name_map_file):
    in_file = open(section_name_map_file, 'r', encoding='cp1252', errors='ignore')
    lines = in_file.readlines()

    out_file = open(section_name_map_file[:-4] + '.tsv', 'w')
    for line in lines:
        sub_strings = line.split('\t')
        if len(sub_strings) > 4:
            new_line = '\t'.join([sub_strings[0], sub_strings[1], sub_strings[2], sub_strings[4].strip()])
            out_file.write(new_line + '\n')

    out_file.close()


if __name__ == '__main__':
    convert_section_name_map('F:\\Users\\James\\Code\\nquiry\\NQUIRY_TOOLS\\resources\\rtf\\RtfSectionName.txt')