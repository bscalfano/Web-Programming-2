from exif import Image

with open('static/images/IMG_1409.jpeg', 'rb') as image_file:
    my_image = Image(image_file)
    if my_image.has_exif:
        print("Yeet")
    else:
        print("yote")
    print(dir(my_image))
    keys = list(dir(my_image))
    print(keys)
    for key in keys:
        try:
            print(key,": ",my_image[key])
        except:
            pass