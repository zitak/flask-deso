from PIL import Image
import functionality.operations


def index(image, operation):

    image = Image.open(image)
    image = image.convert('RGB')
    pixels = image.load()
    (width, height) = image.size

    if operation == 'depth_9bits':
        functionality.operations.quantize(pixels, width, height, 9)
    elif operation == 'depth_12bits':
        functionality.operations.quantize(pixels, width, height, 12)
    elif operation == 'depth_15bits':
        functionality.operations.quantize(pixels, width, height, 15)
    elif operation == 'extract_red':
        functionality.operations.extraction(pixels, width, height, 'R')
    elif operation == 'extract_green':
        functionality.operations.extraction(pixels, width, height, 'G')
    elif operation == 'extract_blue':
        functionality.operations.extraction(pixels, width, height, 'B')
    elif operation == 'flip_vertical':
        functionality.operations.vertical_flip(pixels, width, height)
    elif operation == 'flip_horizontal':
        functionality.operations.horizontal_flip(pixels, width, height)

    return image
    # path = path.split('.')
    # image.save(path[0] + "new." + path[1])
