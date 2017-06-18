from PIL import Image
import functionality.operations


def index(path, operation=4, bits=24, color='R'):

    image = Image.open(path)
    image = image.convert('RGB')
    pixels = image.load()
    (width, height) = image.size

    if operation == 1:
        functionality.operations.quantize(pixels, width, height, bits)
    elif operation == 2:
        functionality.operations.extraction(pixels, width, height, color)
    elif operation == 3:
        functionality.operations.vertical_flip(pixels, width, height)
    elif operation == 4:
        functionality.operations.horizontal_flip(pixels, width, height)

    path = path.split('.')
    image.save(path[0] + "new." + path[1])
