from PIL import Image

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def get_pixel_matrix(img_file: str):
    img = Image.open(img_file).convert('RGB')
    width, height = img.size
    pixels = list(img.getdata())
    return [pixels[i:i + width] for i in range(0, len(pixels), width)]


def get_brightness_matrix(pixel_matrix: []):
    matrix_brightness = []
    for row in pixel_matrix:
        row_brightness = []
        for pixel in row:
            row_brightness.append(round((pixel[0] + pixel[1] + pixel[2]) / 3.0))
        matrix_brightness.append(row_brightness)
    return matrix_brightness


# no sé lo que estoy haciendo





