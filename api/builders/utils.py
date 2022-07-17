from PIL import ImageFont

import os


SIZES = {'title': 'api/builders/fonts/inter-500.ttf', 'artist': 'api/builders/fonts/inter-600.ttf', 'subtitle': 'api/builders/fonts/inter-500.ttf'}

def get_text_len(text, font_size, font_name):
    print(f":::current director - {os.getcwd()}")
    print(f"::::directory listing - {os.listdir()}")
    print(f"::::{os.listdir('api/builders/')}")
    font = ImageFont.truetype(SIZES[font_name], font_size)
    size = font.getsize(text)
    return size[0]


if __name__ == "__main__":
    print(get_text_len('W.A.V.E (Bonus Tracioi', 16, 'title'))