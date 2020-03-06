import requests

from tools.music_parser import MidiPageParser


def crawl_midis():
    response = requests.get('http://www.christianstudy.com/lifehymns.html')
    with open('Output/Hymns/big5.html', 'w') as out_file:
        out_file.write(response.text)
    with open('Output/Hymns/big5.html', 'r', encoding='big5') as in_file, open('Output/Hymns/utf8.html', 'w',
                                                                               encoding='utf8') as out_file:
        out_file.write(in_file.read())

    midi_page_parser = MidiPageParser()

    with open('Output/Hymns/utf8.html', 'r', encoding='utf8') as in_file:
        page_content = in_file.read()
        midi_page_parser.feed(page_content)


if __name__ == '__main__':
    crawl_midis()
