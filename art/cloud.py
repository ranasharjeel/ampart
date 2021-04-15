import numpy as np
from collections import Counter
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator


def generateWordCloud(word_list, mask_name, out_name):
    # Output path
    OUT_PATH = "static/"+out_name+".png";
    # Mask path
    IMG_PATH = "static/" + mask_name + ".png";

    words = Counter(word_list)
    im = Image.open(IMG_PATH).convert("RGB")
    custom_mask = np.array(im)
    img_colors = ImageColorGenerator(custom_mask)

    # Word cloud generation - word frequency
    wc = WordCloud(
        background_color='white',
        mask=custom_mask,
        contour_width=10,
        contour_color='black',
        color_func=img_colors
    ).generate_from_frequencies(words)


    # Output wordcloud to assets
    wc.to_file(OUT_PATH)