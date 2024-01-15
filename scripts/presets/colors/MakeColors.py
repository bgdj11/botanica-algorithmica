import os
from PIL import Image
import numpy as np
import csv
import matplotlib.colors as mcolors

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

def is_bright(color, threshold=550):
    # Definisemo prag za svetle boje
    return sum(color) > threshold

def is_dark(color, dark_threshold=50, brown_threshold=100):
    # Definisemo prag za tamne boje (pokusavamo da sacuvamo nijanse braon)
    return sum(color) < dark_threshold and not (color[0] > brown_threshold and color[1] > brown_threshold / 2)

def is_vivid(color, saturation_threshold=0.7, value_threshold=0.7):
    # Pretvaranje boje u HSV format
    hsv_color = mcolors.rgb_to_hsv(color)
    # Izdvajanje komponenti zasicenosti i vrednosti
    saturation, value = hsv_color[1], hsv_color[2]

    return saturation > saturation_threshold and value > value_threshold


def make_colors():
    # Dobijanje putanje trenutnog fajla
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Kreiranje putanje do 'color_palette.png' relativno u odnosu na trenutni fajl
    img_path = os.path.join(current_dir, 'color_palette.png')
    img = Image.open(img_path)

    # Konvertovanje slike u niz piksela
    pixels = np.array(img)

    # Izvlacenje jedinstvenih boja
    unique_colors = np.unique(pixels.reshape(-1, 3), axis=0)

    # Filtriranje svetlih i suvise tamnih boja i konvertovanje preostalih u heksadecimalne
    filtered_colors = [color for color in unique_colors if not (is_bright(color) or is_dark(color) or is_vivid(color))]
    hex_colors = [rgb_to_hex(color) for color in filtered_colors]

    # Cuvanje boja u CSV fajlu
    output_csv_path = 'colors_preset.csv'
    with open(output_csv_path, 'w', newline='') as csvfile:
        color_writer = csv.writer(csvfile)
        color_writer.writerow(['Color'])
        for hex_color in hex_colors:
            color_writer.writerow([hex_color])

def filter_leaf_colors(color_list):
    leaf_colors = []

    for color in color_list:
        # Pretvaranje boje u HSV format
        hsv_color = mcolors.rgb_to_hsv(mcolors.to_rgb(color))

        # Suzenje opsega za nijansu (Hue) i dodavanje provera za zasicenost i vrednost
        hue = hsv_color[0] * 360
        saturation = hsv_color[1]
        value = hsv_color[2]

        if 80 <= hue <= 140 and saturation > 0.2 and value > 0.2:
            leaf_colors.append(color)

    return leaf_colors

# make_colors()