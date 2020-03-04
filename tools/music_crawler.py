import requests

from tools.music_parser import SongListingParser


def crawl_songs(url):
    response = requests.get(url)
    song_list_parser = SongListingParser()
    song_list_parser.feed(response.text)
    for (number, title, url) in zip(song_list_parser.number_list, song_list_parser.title_list,
                                    song_list_parser.url_list):
        print(number + '-' + title + ': ' + url)


if __name__ == '__main__':
    import sys

    if sys.argv is None or len(sys.argv) < 2:
        print('Usage: python music_crawler.py <URL>')
    else:
        crawl_songs(sys.argv[1])
