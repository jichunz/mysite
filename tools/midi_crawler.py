import requests

from tools.music_parser import MidiPageParser


def crawl_midis():
    response = requests.get('http://www.christianstudy.com/lifehymns.html')
    midi_page_parser = MidiPageParser()
    midi_page_parser.feed(response.text)


if __name__ == '__main__':
    crawl_midis()
