class ChineseConverter():
    def __init__(self, traditional_chars_file, simplified_chars_file):
        with open(traditional_chars_file, 'r', encoding='utf8') as traditional_chars_file:
            traditional_chars = traditional_chars_file.read()
        with open(simplified_chars_file, 'r', encoding='utf8') as simplified_chars_file:
            simplified_chars = simplified_chars_file.read()
        self.simplified_to_traditional = dict()
        self.traditional_to_simplified = dict()
        for (s, t) in zip(simplified_chars, traditional_chars):
            self.simplified_to_traditional[s] = t
            self.traditional_to_simplified[t] = s

    def get_simplified_char(self, traditional_char):
        return self.traditional_to_simplified.get(traditional_char, traditional_char)

    def get_traditional_char(self, simplified_char):
        return self.simplified_to_traditional.get(simplified_char, simplified_char)

    def to_simplified(self, traditional_phrase):
        simplified = list()
        for t in traditional_phrase:
            simplified.append(self.get_simplified_char(t))
        return ''.join(simplified)

    def to_traditional(self, simplified_phrase):
        traditional = list()
        for s in simplified_phrase:
            traditional.append(self.get_traditional_char(s))
        return ''.join(traditional)


def test_chinese_convert():
    chinese_converter = ChineseConverter('/Users/james/Downloads/traditional_chinese.txt',
                                         '/Users/james/Downloads/simplified_chinese.txt')
    simplified_char = '爱'
    traditional_char = '愛'
    print('For simplified char "' + simplified_char + '" traditional char is "' +
          chinese_converter.get_traditional_char(simplified_char) + '".')
    print('For traditional char "' + traditional_char + '" simplified char is "' +
          chinese_converter.get_simplified_char(traditional_char) + '".')


if __name__ == '__main__':
    test_chinese_convert()
