from PIL import Image # type: ignore
import zlib
import sys

def convert(input: str, output: str):
    with open(input, 'rb') as f:
        magic = f.read(4)
        if magic != b'RAY1':
            raise ValueError('Not a valid .raymg file')

        width = int.from_bytes(f.read(4), 'big')
        height = int.from_bytes(f.read(4), 'big')
        size = int.from_bytes(f.read(4), 'big')
        compressed_data = f.read(size)

    raw_data = zlib.decompress(compressed_data)
    pixels = [tuple(raw_data[i:i+4]) for i in range(0, len(raw_data), 4)]
    image = Image.new('RGBA', (width, height))
    image.putdata(pixels)
    image.save(output)

if len(sys.argv) > 1:
    convert(sys.argv[1], 'output.png')
else:
    sys.exit(1)