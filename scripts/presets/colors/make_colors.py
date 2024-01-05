from PIL import Image
import numpy as np
import csv

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

def is_bright(color, threshold=600):
    # Definisemo prag za svetle boje
    return sum(color) > threshold

def is_dark(color, dark_threshold=50, brown_threshold=100):
    # Definisemo prag za tamne boje (pokusavamo da sacuvamo nijanse braon)
    return sum(color) < dark_threshold and not (color[0] > brown_threshold and color[1] > brown_threshold / 2)

# Ucitavanje slike
img_path = 'color_palette.png'
img = Image.open(img_path)

# Konvertovanje slike u niz piksela
pixels = np.array(img)

# Izvlacenje jedinstvenih boja
unique_colors = np.unique(pixels.reshape(-1, 3), axis=0)

# Filtriranje svetlih i suvise tamnih boja i konvertovanje preostalih u heksadecimalne
filtered_colors = [color for color in unique_colors if not (is_bright(color) or is_dark(color))]
hex_colors = [rgb_to_hex(color) for color in filtered_colors]

# Cuvanje boja u CSV fajlu
output_csv_path = 'colors_preset.csv'
with open(output_csv_path, 'w', newline='') as csvfile:
    color_writer = csv.writer(csvfile)
    color_writer.writerow(['Color'])
    for hex_color in hex_colors:
        color_writer.writerow([hex_color])
