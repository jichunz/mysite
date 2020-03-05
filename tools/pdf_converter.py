from PIL import Image


def to_pdf(pdf_file_name, image_file_names):
    converted = [Image.open(i).convert('RGB') for i in image_file_names]
    append_images = converted[1:]
    converted[0].save(pdf_file_name, save_all=True, append_images=append_images)


def test_pdf_converter():
    to_pdf(r'/Users/james/Temp/hymns.pdf', [r'/Users/james/Downloads/Hymns/2-禰真偉大_1.png',
                                            r'/Users/james/Downloads/Hymns/2-禰真偉大_2.png',
                                            r'/Users/james/Downloads/Hymns/7-禰的信實廣大_1.png',
                                            r'/Users/james/Downloads/Hymns/7-禰的信實廣大_2.png'])


if __name__ == '__main__':
    test_pdf_converter()
