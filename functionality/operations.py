

def horizontal_flip(pixels, width, height):
    for y in range(0, height // 2):
        for x in range(0, width):
            tmp = pixels[x, y]
            pixels[x, y] = pixels[x, height - y - 1]
            pixels[x, height - y - 1] = tmp


def vertical_flip(pixels, width, height):
    for y in range(0, height):
        for x in range(0, width // 2):
            tmp = pixels[x, y]
            pixels[x, y] = pixels[width - x - 1, y]
            pixels[width - x - 1, y] = tmp


def extraction(pixels, width, height, color):
    for y in range(0, height):
        for x in range(0, width):
            (red, green, blue) = pixels[x, y]

            if color == 'R':
                (red, green, blue) = (0, green, blue)
            elif color == 'G':
                (red, green, blue) = (red, 0, blue)
            elif color == 'B':
                (red, green, blue) = (red, green, 0)

            pixels[x, y] = (red, green, blue)


def quantize(pixels, width, height, bits):
    offset = 2 ** (8 - (bits // 3))

    for y in range(0, height):
        for x in range(0, width):
            (red, green, blue) = pixels[x, y]

            red = (red // offset) * offset
            green = (green // offset) * offset
            blue = (blue // offset) * offset

            pixels[x, y] = (red, green, blue)