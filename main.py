from PIL import Image

ASCII_CHARS = '@%#*+=-:. '

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert('L')

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 32]
    return ascii_str

def process_image(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image)
    image = grayscale_image(image)
    ascii_str = pixels_to_ascii(image)
    img_width = image.width

    ascii_img = ''
    for i in range(0, len(ascii_str), img_width):
        ascii_img += ascii_str[i:i+img_width] + '\n'

    print(ascii_img)

# Example usage:
image_path = 'path/to/your/image.jpg'
process_image(image_path)
