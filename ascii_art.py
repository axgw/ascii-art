from PIL import Image

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def get_pixel_matrix(img_file: str):
    img = Image.open(img_file).convert('RGB')
    width, height = img.size
    pixels = list(img.getdata())
    return [pixels[i:i + width] for i in range(0, len(pixels), width)]


def get_brightness_matrix(pixel_matrix: []):
    brightness_matrix = [[0 for _ in i] for i in pixel_matrix]
    for x, row in enumerate(pixel_matrix):
        for y, pixel in enumerate(row):
            brightness_matrix[x][y] = (round((pixel[0] + pixel[1] + pixel[2]) / 3.0))
    return brightness_matrix


def char_val_mapping(brightness_matrix: [], ascii_chars: []):
    ascii_matrix = [[0 for _ in i] for i in brightness_matrix]
    for x, row in enumerate(brightness_matrix):
        for y, pixel in enumerate(row):
            ascii_matrix[x][y] = ascii_chars[int(pixel / 255 * len(ascii_chars) - 1)]
    return ascii_matrix

