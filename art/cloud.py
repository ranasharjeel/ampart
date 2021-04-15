import numpy as np
from collections import Counter
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator


IMG_PATH = "assets/note.png"
OUT_PATH = "assets/img.png"

def generateWordCloud(word_list):
    words = Counter(word_list)
    im = Image.open(IMG_PATH).convert("RGB")
    custom_mask = np.array(im)
    img_colors = ImageColorGenerator(custom_mask)

    # Word cloud
    wc = WordCloud(
        background_color='white',
        mask=custom_mask,
        contour_width=5,
        contour_color='black',
        color_func=img_colors
    ).generate_from_frequencies(words)


    # Output wordcloud to assets
    wc.to_file(OUT_PATH)