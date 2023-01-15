import PIL
from PIL import Image, ImageDraw, ImageFont


def compress_image(image_path, safe_location):
    img = Image.open(image_path)


def watermark_image(image_path, image = None, watermark_text = "Watermark", watermark_location = (5, 5), watermark_image_path = None, watermark_image_location = (5, 30), watermark_image_size = (50, 50), safe_location = None, return_image = True):
    # either use provided image or find image via provided path
    if image is not None:
        img = image
    else:
        img = Image.open(image_path)

    # Image will be modified
    watermarked = ImageDraw.Draw(img)
    watermarked.text(watermark_location, watermark_text)
    watermarked.bitmap()

    # Safe or return the image dependent on whether a location for saving is provided or not
    if safe_location is not None:
        # safe to path
        print()
        # check if image should also be returned in addition to be saved
        if return_image:
            return watermarked
    else:
        # return image
        if return_image:
            return watermarked

# Send a message when script is executed
if __name__ == "__main__":
    print("This script is just an addition for other projects. ")
