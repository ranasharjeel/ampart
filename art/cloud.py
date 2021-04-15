import numpy as np
from collections import Counter
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator


IMG_PATH = "assets/"
OUT_PATH = "assets/img.png"

def generateWordCloud(word_list, mask_name, mode):
    # Edit image path
    IMG_PATH = "assets/" + mask_name + ".png";

    words = Counter(word_list)
    im = Image.open(IMG_PATH).convert("RGB")
    custom_mask = np.array(im)
    img_colors = ImageColorGenerator(custom_mask)

    wc = WordCloud(
        background_color='white',
        mask=custom_mask,
        contour_width=10,
        contour_color='black',
        color_func=img_colors
    )
    
    # Word cloud generation - MODE 0 (Frequencies)
    if mode == 0:
        wc.generate_from_frequencies(words)


    # Word cloud - MODE 1 (RAW)
    elif mode == 1:
        wc.generate(word_list)

    # Output wordcloud to assets
    wc.to_file(OUT_PATH)