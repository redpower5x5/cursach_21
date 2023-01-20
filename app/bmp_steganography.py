from io import BytesIO
from PIL import Image

def encode_image(img_data, msg):
	"""
	hide text in the red portion of each pixel
	(r, g, b) tuple in the image
	"""
	img = Image.open(BytesIO(img_data))
	length = len(msg)
	# limit length of message to 255
	if length > 255:
		print("text too long! (don't exeed 255 characters)")
		return False
	if img.mode != 'RGB':
		print("image mode needs to be RGB")
		return False
	# use a copy of image to hide the text in
	encoded = img.copy()
	width, height = img.size
	index = 0
	for row in range(height):
		for col in range(width):
			r, g, b = img.getpixel((col, row))
			# first value is length of msg
			if row == 0 and col == 0 and index < length:
				asc = length
			elif index <= length:
				c = msg[index -1]
				asc = ord(c)
			else:
				asc = r
			encoded.putpixel((col, row), (asc, g , b))
			index += 1
	buf = BytesIO()
	encoded.save(buf, format='BMP')
	return buf.getvalue()

def decode_image(img_data):
    """
    check the red portion of an image (r, g, b) tuple for
    hidden message characters (ASCII values)
    """
    img = Image.open(BytesIO(img_data))
    width, height = img.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                # need to add transparency a for some .png files
                r, g, b, a = img.getpixel((col, row))		
            # first pixel r value is length of message
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                msg += chr(r)
            index += 1
    return msg