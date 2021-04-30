import numpy as np
from collections import Counter
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator


def generateWordCloud(word_list, mask_name, out_name):
    # Output path
    OUT_PATH = "static/assets/"+out_name+".svg";
    # Mask path
    IMG_PATH = "static/assets/" + mask_name + "-mask" + ".png";
    # Outline path
    BORDER_PATH = "static/assets/" + mask_name + "-outline" + ".svg";

    words = Counter(word_list)
    im = Image.open(IMG_PATH).convert("RGB")
    custom_mask = np.array(im)
    img_colors = ImageColorGenerator(custom_mask)

    # Word cloud generation - word frequency
    wc = WordCloud(
        background_color='rgba(255,255,255,1)', #F9F5F1
        mask=custom_mask,
        color_func=img_colors,
        mode="RGBA"
    ).generate_from_frequencies(words)

    
    # Convert to SVG and get body only (remove svg tags)
    svg_str = wc.to_svg().splitlines()
    del svg_str[-1]
    del svg_str[0]
    svg_str = '\n'.join(svg_str)

    # Load in outline SVG and merge word cloud body with outline
    # <cloud/> is a placeholder in the outlines to replace with the body
    border_file = open(BORDER_PATH, "r")
    border = border_file.read()
    border_file.close()

    # Merge word cloud body for final result
    result = border.replace('<cloud/>', svg_str)
    

    # Output wordcloud and border to assets
    out_file = open(OUT_PATH, "w")
    out_file.write(result)
    out_file.close()