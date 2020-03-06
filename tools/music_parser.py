import os
import shutil
from html.parser import HTMLParser
from urllib.request import urlopen


class SongListParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.started_song_list_header = False
        self.started_song_list = False
        self.started_song = False
        self.processing_song = False
        self.number_list = list()
        self.title_list = list()
        self.url_list = list()

    def handle_starttag(self, tag, attrs):
        if tag == 'h3':
            self.started_song_list_header = True
        elif tag == 'ul':
            if self.started_song_list_header:
                self.started_song_list = True
        elif tag == 'li':
            if self.started_song_list:
                self.started_song = True
        elif tag == 'a':
            if self.started_song:
                self.processing_song = True
                for name, value in attrs:
                    if name == 'href':
                        self.url_list.append(value)
                        print('Started a song at "' + value + '"!')

    def handle_data(self, data):
        if self.started_song:
            if self.processing_song:
                self.title_list.append(data)
                print('Started a song with title "' + data + '"')
            else:
                text = str(data).strip()
                if text:
                    self.number_list.append(text[1:-1])
                    print('Started a song with number "' + text[1:-1] + '"')

    def handle_endtag(self, tag):
        if tag == 'a':
            if self.processing_song:
                self.processing_song = False
        elif tag == 'li':
            if self.started_song:
                self.started_song = False
        elif tag == 'ul':
            if self.started_song_list:
                self.started_song_list = False
                print('Running int </ul>! Ending song list!')
                self.started_song_list = False


class SongPageParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.song_image_urls = list()
        self.started_img_tab = False
        self.processing_img_ref = False

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for name, value in attrs:
                if name == 'class' and value == 'img_tab':
                    self.started_img_tab = True
        elif tag == 'a':
            if self.started_img_tab:
                self.processing_img_ref = True
                for name, value in attrs:
                    if name == 'href':
                        self.song_image_urls.append(value)

    def handle_endtag(self, tag):
        if tag == 'div':
            if self.started_img_tab:
                self.started_img_tab = False
        elif tag == 'a':
            if self.processing_img_ref:
                self.processing_img_ref = False


class MidiPageParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.table_index = -1
        self.started_song_list = False
        self.row_index = -1
        self.started_song = False
        self.column_index = -1
        self.song_title = None
        self.song_url = None

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.table_index += 1
            if self.table_index == 2:
                self.started_song_list = True
        elif tag == 'tr':
            if self.started_song_list:
                self.row_index += 1
                if self.row_index > 0:
                    self.started_song = True
        elif tag == 'td':
            if self.started_song:
                self.column_index += 1
        elif tag == 'a':
            if self.started_song:
                if self.column_index == 2:
                    for name, value in attrs:
                        if name == 'href' and value[-4:] == '.mid':
                            self.song_url = value

    def handle_endtag(self, tag):
        if tag == 'table':
            if self.started_song_list:
                self.started_song_list = False
        elif tag == 'tr':
            if self.started_song:
                # Download the midi file
                print('On row ' + str(self.row_index) + ' found song with title "' + self.song_title +
                      '" and URL "' + self.song_url + '".')
                self.download_midi('http://www.christianstudy.com', self.song_title, self.song_url, 'Output/Hymns/MIDI')

                self.started_song = False
                self.column_index = -1
                self.song_title = None
                self.song_url = None

    def handle_data(self, data):
        data = data.strip()
        if self.started_song:
            if self.column_index == 0 and data:
                self.song_title = data if not self.song_title else self.song_title + data

    def download_midi(self, base_url, song_title, song_url, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        full_song_url = base_url + song_url
        song_file_name = os.path.join(output_folder, song_title + '.midi')
        with urlopen(full_song_url) as song_midi_response, open(song_file_name, 'wb') as out_file:
            shutil.copyfileobj(song_midi_response, out_file)
