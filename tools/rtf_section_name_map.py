import csv


def convert_section_name_map(section_name_map_file):
    in_file = open(section_name_map_file, 'r', encoding='cp1252', errors='ignore')
    lines = in_file.readlines()

    with open(section_name_map_file[:-4] + '.csv', 'w', newline='') as out_file:
        csv_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line in lines:
            sub_strings = line.split('\t')
            if len(sub_strings) > 4:
                csv_writer.writerow([sub_strings[0], sub_strings[1], sub_strings[2], sub_strings[4]])


if __name__ == '__main__':
    convert_section_name_map('F:\\Users\\James\\Code\\nquiry\\NQUIRY_TOOLS\\resources\\rtf\\RtfSectionName.txt')
