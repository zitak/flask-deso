

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
                (red, green, blue) = (red, 0, 0)
            elif color == 'G':
                (red, green, blue) = (0, green, 0)
            elif color == 'B':
                (red, green, blue) = (0, 0, blue)

            pixels[x, y] = (red, green, blue)
