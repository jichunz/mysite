import shutil
from urllib.parse import urlsplit, urlunsplit
from urllib.request import urlopen

import requests

from tools.music_parser import SongListParser, SongPageParser


def crawl_songs(url):
    url_split_result = urlsplit(url)
    response = requests.get(url)
    song_list_parser = SongListParser()
    song_list_parser.feed(response.text)
    download_folder = '/Users/james/Downloads/Hymns/'
    for (number, title, song_page_url) in zip(song_list_parser.number_list, song_list_parser.title_list,
                                              song_list_parser.url_list):
        print(number + '-' + title + ': ' + song_page_url)
        song_page_url = urlunsplit([url_split_result[0], url_split_result[1], song_page_url, '', ''])
        response = requests.get(song_page_url)
        song_page_parser = SongPageParser()
        song_page_parser.feed(response.text)
        if song_page_parser.song_image_urls:
            page_number = 1
            for song_image_url in song_page_parser.song_image_urls:
                song_image_file_name = download_folder + str(number) + '-' + title
                if len(song_page_parser.song_image_urls) > 1:
                    song_image_file_name += '_' + str(page_number)
                page_number += 1
                song_image_file_name += '.png'
                with urlopen(song_image_url) as song_image_response, open(song_image_file_name, 'wb') as out_file:
                    shutil.copyfileobj(song_image_response, out_file)


if __name__ == '__main__':
    import sys

    if sys.argv is None or len(sys.argv) < 2:
        print('Usage: python music_crawler.py <URL>')
    else:
        crawl_songs(sys.argv[1])
