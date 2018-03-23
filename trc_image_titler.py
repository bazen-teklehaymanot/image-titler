from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

SOURCE = 'E:\\Documents\\Work\\The Renegade Coder\\Assets\\Featured Images\\Sources\\hello-world-in-swift.jpg'
TITLE = "Hello World in Swift"


def split_string_by_nearest_middle_space(input_string):
    """
    Splits a string by the nearest middle space.

    :param input_string: some string
    :type input_string: str
    :return: a pair of strings
    :rtype: tuple
    """
    index = len(input_string) // 2
    curr_char = input_string[index]
    n = 1
    while not curr_char.isspace():
        index += (-1)**(n + 1) * n  # thanks wolfram alpha (1, -2, 3, -4, ...)
        curr_char = input_string[index]
        n += 1
    return input_string[:index], input_string[index + 1:]


top_half, bottom_half = split_string_by_nearest_middle_space(TITLE)
img = Image.open(SOURCE)
cropped_img = img.crop((0, 0, 1920, 1200))
draw = ImageDraw.Draw(cropped_img)
font = ImageFont.truetype("BERNHC.TTF", 114)
width, height = draw.textsize(TITLE, font)
print("Width: {0}, Height: {1}".format(width, height))
draw.text((1350, 150), top_half, fill=(255, 255, 255), font=font)
draw.text((1550, 300), bottom_half, fill=(255, 255, 255), font=font)
cropped_img.show()

