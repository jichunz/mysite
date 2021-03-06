import os
import shutil
from urllib.parse import urlsplit, urlunsplit
from urllib.request import urlopen

import requests

from tools.chinese_converter import ChineseConverter
from tools.music_parser import SongListParser, SongPageParser
from tools.pdf_converter import to_pdf


def crawl_songs(url):
    url_split_result = urlsplit(url)
    response = requests.get(url)
    song_list_parser = SongListParser()
    song_list_parser.feed(response.text)
    png_folder = 'Output/Hymns/PNG'
    if not os.path.exists(png_folder):
        os.makedirs(png_folder)
    pdf_folder = 'Output/Hymns/PDF'
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
    chinese_converter = ChineseConverter('resources/traditional_chinese.txt',
                                         'resources/simplified_chinese.txt')
    for (number, title, song_page_url) in zip(song_list_parser.number_list, song_list_parser.title_list,
                                              song_list_parser.url_list):
        title = chinese_converter.to_traditional(title)
        song_page_url = urlunsplit([url_split_result[0], url_split_result[1], song_page_url, '', ''])
        grab_song(pdf_folder, png_folder, number, title, song_page_url)


def grab_song(pdf_folder, png_folder, number, title, song_page_url):
    print(number + '-' + title + ': ' + song_page_url)
    response = requests.get(song_page_url)
    song_page_parser = SongPageParser()
    song_page_parser.feed(response.text)
    if song_page_parser.song_image_urls:
        page_number = 1
        song_image_file_names = list()
        for song_image_url in song_page_parser.song_image_urls:
            song_image_file_name = os.path.join(png_folder, str(number) + '-' + title)
            if len(song_page_parser.song_image_urls) > 1:
                song_image_file_name += '_' + str(page_number)
            page_number += 1
            song_image_file_name += '.png'
            song_image_file_names.append(song_image_file_name)
            with urlopen(song_image_url) as song_image_response, open(song_image_file_name, 'wb') as out_file:
                shutil.copyfileobj(song_image_response, out_file)
        to_pdf(os.path.join(pdf_folder, str(number) + '-' + title + '.pdf'), song_image_file_names)


if __name__ == '__main__':
    crawl_songs('https://www.zanmeishi.com/songbook/hymns-for-gods-people.html')
