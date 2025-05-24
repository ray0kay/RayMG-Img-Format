from PIL import Image # type: ignore
import zlib
import sys

def convert(input: str, output: str):
    img = Image.open(input).convert('RGBA')
    width, height = img.size
    pixels = list(img.getdata())

    flat_pixels = []
    for pixel in pixels:
        flat_pixels.extend(pixel)

    compressed = zlib.compress(bytearray(flat_pixels))

    with open(output, 'wb') as f:
        f.write(b'RAY1')
        f.write(width.to_bytes(4, 'big'))
        f.write(height.to_bytes(4, 'big'))
        f.write(len(compressed).to_bytes(4, 'big'))
        f.write(compressed)

if len(sys.argv) > 1:
    convert(sys.argv[1], 'output.raymg')
else:
    sys.exit(1)