from PIL import Image, ImageDraw


def save_compressed_image(img, safe_location, image_codec="JPEG", save_quality=85):
    img.save(safe_location, image_codec, optimize=True, quality=save_quality)


def watermark_image(image_path, image = None, watermark_text = "Watermark", watermark_location = (5, 5), watermark_image_path = None, watermark_image_location = (30, 5), watermark_image_size = (50, 50), safe_location = None, return_image = True, save_compressed = False, save_image_codec = "JPEG", save_quality_level = 5):
    # TODO check, if every value is provided in the right format so it can be used. Else return an error message

    # either use provided image or find image via provided path
    if image is not None:
        img = image
    else:
        img = Image.open(image_path)

    # Image will be modified
    watermarked = ImageDraw.Draw(img)
    watermarked.text(watermark_location, watermark_text)
    if watermark_image_path is not None:
        watermarked.bitmap(watermark_image_location, Image.open(watermark_image_path).resize(watermark_image_size))

    # Safe or return the image dependent on whether a location for saving is provided or not
    if safe_location is not None:
        # safe to path
        if save_compressed:
            save_compressed_image(img, safe_location, save_image_codec, save_quality_level)
        else:
            img.save(safe_location)
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
